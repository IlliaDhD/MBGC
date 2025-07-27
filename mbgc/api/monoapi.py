from mbgc.utils.config import Config
import logging
import requests
import time
import pandas as pd

class MonoApi:

    def __init__(self):
        self._api_token: str = Config.api_token
        self._request_period: int = int(Config.request_period)
        self._mono_account_id: int = int(Config.mono_account_id)

        self.to_time: int = int(time.time())
        self.from_time: int = self.to_time - self._request_period

        logging.info(f"MonoApi Request Period: {self.from_time} to {self.to_time}")

    def get_transactions(self) -> pd.DataFrame:

        url = f"https://api.monobank.ua/personal/statement/{self._mono_account_id}/{self.from_time}/{self.to_time}"
        headers = {"X-Token" : self._api_token}

        response = requests.get(url=url, headers=headers)

        if response.status_code != 200:
            raise Exception(f"MonoApi response status code: {response.status_code}. Program is shutting down.")
        else: logging.info(f"MonoApi response succeeded!")

        return pd.DataFrame(response.json())


