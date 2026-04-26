import json
from typing import List
from logging import getLogger

from pandas import DataFrame

from config import config

logger = getLogger(__name__)


def add_new_institutions(names: List[str]) -> None:
    with open(
       config.category_mapper_json_path, "r", encoding="utf-8") as json_file:
        records: json = json.load(json_file)
        for name in names:
            records[name] = config.default_category_id

    with open(
       config.category_mapper_json_path, "w", encoding="utf-8") as json_file:
        json.dump(records, json_file, ensure_ascii=False, indent=2)

    logger.info("Wrote new institutions to the mappers file")


def save_to_csv(filename: str, data: DataFrame) -> None:
    file_path = f"{config.result_csv_path}/{filename}"
    data.to_csv(file_path, sep='\t', encoding='utf-8',
                index=False, header=True)
    logger.info(f"Wrote results the file: {file_path}")
