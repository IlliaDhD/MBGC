import logging

from mbgc.api.monoapi import MonoApi
from mbgc.data_processing.dataprocessor import DataProcessor

if __name__ == "__main__":
    monoApi = MonoApi()
    transactions = monoApi.get_transactions()
    logging.info("MonoApi: Obtained transactions: {}".format(transactions))
    data_processor = DataProcessor(transactions)
    data_processor.process_data()