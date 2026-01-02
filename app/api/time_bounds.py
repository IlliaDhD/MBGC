import logging
import time
from typing import Tuple, List

from config import Config


def bounds_from_month_number(month_number: int) -> List[Tuple[float, float]]:
    period = month_number * Config.month_unix_period
    logging.info(f"Defining bounds for {month_number} month ")

    return bounds_from_period(period)


def bounds_from_days_number(days_number: int) -> List[Tuple[float, float]]:
    period = days_number * Config.day_unix_period
    logging.info(f"Defining bounds for {days_number} days")

    return bounds_from_period(period)


def bounds_from_period(period: float) -> List[Tuple[float, float]]:
    current_time = time.time()
    result = []

    logging.info(f"Defining bounds for a period: {period}")

    while period > 0:
        if period >= Config.month_unix_period:
            period -= Config.month_unix_period
            from_time = current_time - Config.month_unix_period
            result.append((from_time, current_time))
            current_time = from_time
        else:
            from_time = current_time - period
            result.append((from_time, current_time))
            break

    logging.info(f"{result} requests will be performed")

    return result
