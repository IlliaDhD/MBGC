import os
import logging

class Config:

    logging.basicConfig(format='[%(levelname)s] %(message)s', level=logging.INFO)

    api_token = os.environ.get("API_TOKEN")
    request_period = os.environ.get("MONO_REQUEST_PERIOD")
    mono_account_id = os.environ.get("MONO_ACCOUNT_ID")

    default_category = os.environ.get("DEFAULT_CATEGORY")
    default_category_id = os.environ.get("DEFAULT_CATEGORY_ID")

    categories_json_path = os.environ.get("CATEGORIES_JSON_PATH")
    category_mapper_json_path = os.environ.get("CATEGORIES_MAPPER_JSON_PATH")
    result_csv_path = os.environ.get("RESULT_CSV_PATH")