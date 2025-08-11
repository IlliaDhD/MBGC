import json
import logging

import pandas as pd

from mbgc.utils.config import Config


class JsonWriter:

    def __init__(self):
        pass

    @staticmethod
    def update_json_with_undefined_categories(data: pd.Series) -> None:
        with open(Config.category_mapper_json_path, "r", encoding="utf-8") as f:
            logging.info(f"JsonWriter: Started updating categories file with {len(data)} entries")

            records: json = json.load(f)
            data.rename("institution", inplace=True)
            mappings: pd.DataFrame = pd.DataFrame(data)
            mappings["id"] = float(Config.default_category_id)

            logging.info("JsonWriter: Created new category mappings: {}".format(mappings))
            new_records: dict[str : float] = mappings.to_dict("records")

            records.extend(new_records)

        with open(Config.category_mapper_json_path, "w", encoding="utf-8") as f:
            json.dump(records, f, indent=2, ensure_ascii=False)
            logging.info("Json:Writer: Wrote new category mappings: {}".format(mappings))
