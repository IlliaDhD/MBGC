import json
from pandas import DataFrame

from config import Config
from app.api.mono_api import get_transactions
from app.data_processing.data_processing import *
from app.data_processing.saving import save_to_csv, add_new_institutions
from app.api.time_bounds import bounds_from_period, bounds_from_days_number


def form_filename(time_bounds: List[Tuple[float, float]]) -> str:
    start = datetime.fromtimestamp(time_bounds[-1][0]).date()
    end = datetime.fromtimestamp(time_bounds[0][1]).date()

    return f"{start}-{end}.csv"


if __name__ == "__main__":
    logger = Config.get_logger("Main")
    transactions = []

    if Config.request_days_number:
        time_bounds = bounds_from_days_number(int(Config.request_days_number))
    else:
        time_bounds = bounds_from_period(Config.request_period or Config.month_unix_period)

    logger.info(f"Requesting transactions for period: {time_bounds}")
    for from_time, to_time in time_bounds:
        # Obtains row transactions
        transactions_list = get_transactions(from_time=from_time, to_time=to_time)

        new_transactions = [{
            'time'           : transaction['time'],
            'operationAmount': transaction['operationAmount'],
            'description'    : transaction['description']
        } for transaction in transactions_list]

        transactions += new_transactions

    logger.info("Obtained transactions: {}".format(transactions))

    # Maps data into required format
    with open(Config.categories_json_path, "r", encoding="utf-8") as categories_file:
        categories: dict[str, str] = json.load(categories_file)
    with open(Config.category_mapper_json_path, "r", encoding="utf-8") as mappers_file:
        mappers: dict[str, str] = json.load(mappers_file)

    processed, new_institutions = map_description_to_category(
        map_coins(map_unix_to_iso(transactions)),
        categories,
        mappers,
    )

    # Saves data
    add_new_institutions(new_institutions)
    save_to_csv(form_filename(time_bounds), DataFrame(processed))
