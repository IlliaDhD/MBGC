import time

import pandas as pd

from app.api.common import bounds_from_period, bounds_from_days_number
from app.api.monoapi import get_transactions
from app.data_processing.dataprocessing import *
from app.data_processing.saving import save_to_csv, add_new_institutions
from config import Config

def form_filename(time_bounds: List[Tuple[float, float]]) -> str:
    start = datetime.fromtimestamp(time_bounds[-1][0]).date()
    end = datetime.fromtimestamp(time_bounds[0][1]).date()

    return f"{start}-{end}.csv"

if __name__ == "__main__":
    logger = Config.get_logger("Main")
    transactions = DataFrame(columns=['time', 'operationAmount', 'description'])

    if Config.request_days_number:
        time_bounds = bounds_from_days_number(int(Config.request_days_number))
    else:
        time_bounds = bounds_from_period(Config.request_period or Config.month_unix_period)

    for from_time, to_time in time_bounds:
        # Obtains row transactions
        new_transactions = get_transactions(from_time=from_time, to_time=to_time).loc[:, ['time', 'operationAmount', 'description']]
        transactions = pd.concat([transactions, new_transactions], ignore_index=True)
        time.sleep(5) # due to API limitations
    # Saves only required columns
    logger.info("MonoApi: Obtained transactions: {}".format(transactions))

    # Maps data into required format
    processed, new_institutions = map_description_to_category(
        map_coins(
            map_unix_to_iso(transactions)
        )
    )

    # Saves data
    add_new_institutions(new_institutions)
    save_to_csv(form_filename(time_bounds), processed)
