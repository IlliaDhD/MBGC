import os
import logging

class Config:

    logging.basicConfig(format='[%(levelname)s] %(message)s', level=logging.INFO)

    api_token = os.environ.get("API_TOKEN")
    request_period = os.environ.get("MONO_REQUEST_PERIOD")
    mono_account_id = os.environ.get("MONO_ACCOUNT_ID")