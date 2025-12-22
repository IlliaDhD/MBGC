import json
from datetime import datetime
from typing import List, Tuple
from pandas import DataFrame

from config import Config

logger = Config.get_logger("DataProcessing")

def map_unix_to_iso(data: DataFrame) -> DataFrame:
    data.loc[:, "time"] = data.loc[:, "time"].apply(func=lambda x: datetime.fromtimestamp(float(x)))
    logger.info(f"With mapped timestamps:\n{data}")
    return  data


def map_coins(data: DataFrame) -> DataFrame:
    data.loc[:, 'operationAmount'] = data.loc[:, 'operationAmount'].apply(lambda x: float(x) / 100)
    logger.info(f"Mapped operationAmount for {len(data)}:\n{data}")
    return data


def map_description_to_category(data: DataFrame) -> Tuple[DataFrame, List[str]]:
    categories: dict[str, str] = json.load(open(Config.categories_json_path, "r", encoding="utf-8"))
    mappers = json.load(open(Config.category_mapper_json_path, "r", encoding="utf-8"))

    new_institutions: List[str] = []
    for index, series in data.iterrows():
        description: str = series.get("description")
        category_id = mappers.get(description)

        if category_id is None:
            new_institutions.append(description)
            series["operationCategory"] = Config.default_category
        else:
            series["operationCategory"] = categories[category_id]

    logger.info(f"Found new institutions: {new_institutions}")
    return data, new_institutions



