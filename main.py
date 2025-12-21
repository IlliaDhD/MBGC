import time

from app.api.monoapi import get_transactions
from app.data_processing.dataprocessing import *
from app.data_processing.saving import save_to_csv, add_new_institutions
from config import Config


def define_time_bounds(requested_period: float) -> Tuple[float, float]:
    to_time = time.time()
    from_time = to_time - requested_period
    return from_time, to_time


if __name__ == "__main__":
    logger = Config.get_logger("Main")
    from_time, to_time = define_time_bounds(requested_period=Config.request_period)

    # Data obtaining
    raw_transactions = get_transactions(from_time=from_time, to_time=to_time)
    transactions = raw_transactions.loc[:, ['time', 'operationAmount', "description"]]
    logger.info("MonoApi: Obtained transactions: {}".format(transactions))

    # Data processing
    processed, new_institutions = map_description_to_category(
        map_coins(
            map_unix_to_iso(transactions)
        )
    )

    # Data saving
    add_new_institutions(new_institutions)
    save_to_csv(f"{datetime.fromtimestamp(to_time).date()}.csv", processed)
