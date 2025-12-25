import os, logging

class Config:

    logging.basicConfig(format='[%(levelname)s] %(message)s', level=logging.INFO)

    api_token = os.environ.get("API_TOKEN")
    mono_account_id = os.environ.get("MONO_ACCOUNT_ID") or 0

    month_unix_period = 2629743
    day_unix_period = 86400
    request_period = float(os.environ.get("MONO_REQUEST_PERIOD") or month_unix_period)
    request_days_number = os.environ.get("MONO_REQUEST_PERIOD_DAYS")

    default_category = os.environ.get("DEFAULT_CATEGORY") or "default"
    default_category_id = os.environ.get("DEFAULT_CATEGORY_ID")

    categories_json_path = os.environ.get("CATEGORIES_JSON_PATH")
    category_mapper_json_path = os.environ.get("CATEGORIES_MAPPER_JSON_PATH")
    result_csv_path = os.environ.get("RESULT_CSV_PATH")

    @classmethod
    def get_mono_url(cls, from_time: float, to_time: float) -> str:
        return f"https://api.monobank.ua/personal/statement/{cls.mono_account_id}/{int(from_time)}/{int(to_time)}"

    @staticmethod
    def get_logger(name: str) -> logging.Logger:
        logger = logging.getLogger(name)
        logger.setLevel(logging.INFO)
        return logger