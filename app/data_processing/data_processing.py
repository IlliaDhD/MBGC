from logging import getLogger
from datetime import datetime
from typing import List, Tuple, Dict, Any

from config import config

logger = getLogger(__name__)


def map_unix_to_iso(data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    for transaction in data:
        transaction['time'] = datetime.fromtimestamp(
            float(transaction['time']))

    logger.info(f"Mapped {len(data)} transactions timestamps to ISO format")

    return data


def map_coins(data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    for transaction in data:
        transaction['operationAmount'] = float(
            transaction['operationAmount']) / 100

    logger.info(f"Mapped operationAmount for {len(data)} transactions")

    return data


def map_description_to_category(
    data: List[Dict[str, Any]],
    categories: dict[str, str],
    mappers: dict[str, str]
) -> Tuple[List[Dict[str, Any]], List[str]]:
    new_institutions: List[str] = []
    for transaction in data:
        description: str = transaction['description']
        category_id: str = mappers.get(description)

        if category_id is None:
            new_institutions.append(description)
            transaction['operationCategory'] = config.default_category
        else:
            transaction['operationCategory'] = categories[category_id]

    logger.info("Found {} new institutions: {}".format(
        len(new_institutions), new_institutions))

    return data, new_institutions
