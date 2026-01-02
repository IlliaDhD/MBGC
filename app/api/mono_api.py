import requests
from requests import HTTPError
from typing import List, Dict, Any

from config import Config


logger = Config.get_logger("MonoAPI")


def get_transactions(from_time: float, to_time: float) -> List[Dict[str, Any]]:
    url = Config.get_mono_url(from_time, to_time)
    headers = {"X-Token": Config.api_token}

    try:
        response = requests.get(url=url, headers=headers)
        response.raise_for_status()

        return response.json()
    except HTTPError as http_err:
        logger.error(f"HTTP error occurred: {http_err.response.status_code} {http_err.response.json()}")
        raise http_err
