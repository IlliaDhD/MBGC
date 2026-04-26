import os

from dotenv import load_dotenv


class Config:
    month_unix_period = 2629743
    day_unix_period = 86400

    def __init__(self):
        load_dotenv()

        self.api_token = os.getenv("API_TOKEN")
        self.mono_account_id = os.getenv("MONO_ACCOUNT_ID", 0)

        self.request_period = float(
            os.getenv("MONO_REQUEST_PERIOD", self.month_unix_period))
        self.request_days_number = os.getenv("MONO_REQUEST_PERIOD_DAYS")

        self.default_category = os.getenv("DEFAULT_CATEGORY", "test")
        self.default_category_id = os.getenv("DEFAULT_CATEGORY_ID")

        self.categories_json_path = os.getenv("CATEGORIES_JSON_PATH")
        self.category_mapper_json_path = os.getenv(
            "CATEGORIES_MAPPER_JSON_PATH")
        self.result_csv_path = os.getenv("RESULT_CSV_PATH")

    def get_mono_url(self, from_time: float, to_time: float) -> str:
        return "https://api.monobank.ua/personal/statement/{}/{}/{}".format(
            self.mono_account_id, int(from_time), int(to_time))


config = Config()
