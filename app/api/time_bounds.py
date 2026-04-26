from logging import getLogger
import time
from typing import Tuple, List

from config import config

logger = getLogger(__name__)


def bounds_from_month_number(month_number: int) -> List[Tuple[float, float]]:
    period = month_number * config.month_unix_period
    logger.info(f"Defining bounds for {month_number} month ")

    return bounds_from_period(period)


def bounds_from_days_number(days_number: int) -> List[Tuple[float, float]]:
    period = days_number * config.day_unix_period
    logger.info(f"Defining bounds for {days_number} days")

    return bounds_from_period(period)


def bounds_from_period(period: float) -> List[Tuple[float, float]]:
    current_time = time.time()
    result = []

    logger.info(f"Defining bounds for a period: {period}")

    while period > 0:
        if period >= config.month_unix_period:
            period -= config.month_unix_period
            from_time = current_time - config.month_unix_period
            result.append((from_time, current_time))
            current_time = from_time
        else:
            from_time = current_time - period
            result.append((from_time, current_time))
            break

    logger.info(f"{result} requests will be performed")

    return result
