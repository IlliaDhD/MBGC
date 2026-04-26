from typing import List, Dict, Any
from logging import getLogger

from requests import HTTPError, get

from config import config


logger = getLogger("MonoAPI")


def get_transactions(from_time: float, to_time: float) -> List[Dict[str, Any]]:
    url = config.get_mono_url(from_time, to_time)
    headers = {"X-Token": config.api_token}

    try:
        response = get(url=url, headers=headers)
        response.raise_for_status()

        return response.json()
    except HTTPError as http_err:
        logger.error("HTTP error occurred: {} {}".format(
            http_err.response.status_code, http_err.response.json()))
        raise
