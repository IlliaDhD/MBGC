import logging
from datetime import datetime

import pandas as pd

from mbgc.data_processing.jsonwriter import JsonWriter
from mbgc.utils.config import Config


class DataProcessor:
    def __init__(self, data: pd.DataFrame):
        self.data: pd.DataFrame = data[["time", "description", "operationAmount"]]
        self.jsonWriter: JsonWriter = JsonWriter()

    def process_data(self) -> None:
        logging.info("Processing data")
        self._map_timestamp()
        self._coins_to_money()
        self._description_to_category()

        self.data.to_csv(Config.result_csv_path, sep='\t', encoding='utf-8', index=False, header=True)
        logging.info(f"Wrote results to csv: \"results.csv\"")

    def _map_timestamp(self):
        self.data["time"] = self.data["time"].apply(lambda x: datetime.fromtimestamp(float(x)))
        logging.info("DataProcessor: Mapped timestamp to datetime\n {}".format(self.data))

    def _coins_to_money(self):
        self.data["operationAmount"] = self.data["operationAmount"].apply(lambda x: float(x) / 100)
        logging.info("DataProcessor: Mapped coins to money\n {}".format(self.data))


    def _description_to_category(self):
        category_id_mappers: pd.DataFrame = pd.read_json(Config.category_mapper_json_path)
        categories: pd.DataFrame = pd.read_json(Config.categories_json_path)
        category_mappers: pd.DataFrame = pd.merge(category_id_mappers, categories, on="id", how="right")
        categories_map: dict[str, str] = dict(
            zip(category_mappers["institution"], category_mappers["name"])
        )

        self.data["operationCategory"] = self.data["description"].apply(lambda institution: categories_map.get(str(institution)))

        undefined_categories: pd.Series = self.data[self.data["operationCategory"].isna()]["description"].drop_duplicates()
        logging.info(f"DataProcessor:{undefined_categories}")
        self.jsonWriter.update_json_with_undefined_categories(undefined_categories)
        self.data["operationCategory"] = self.data["operationCategory"].fillna(Config.default_category)

        logging.info("DataProcessor: Added operationCategory column")
        logging.info(self.data)

