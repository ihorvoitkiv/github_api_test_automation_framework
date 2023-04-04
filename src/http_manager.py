import functools
import logging

import requests

logger = logging.getLogger(__name__)


def log_request(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        request_method = func.__name__.upper()
        request_url = args[1]

        logging.info(f"------------------------- Request -------------------------")
        logging.info(f"Method {request_method}, URL: {request_url}")
        logging.debug(f"Headers:\n{kwargs.get('headers')}")
        logging.debug(f"Params:\n{kwargs.get('params')}")
        logging.debug(f"Data:\n{kwargs.get('data')}")
        logging.debug(f"JSON:\n{kwargs.get('json')}")

        try:
            response = func(*args, **kwargs)
            logging.info(f"------------------------- Response -------------------------")
            logging.info(f"Status code: {response.status_code}, {response.reason}")
            logging.debug(f"Body:\n{response.text}")
            logging.debug(f"Headers:\n{response.headers}")
            return response
        except Exception as e:
            logging.error(f"Error requesting {request_method}: {e}")
            raise
        finally:
            logging.info(f"{'=' * 100}\n")

    return wrapper


class RequestAPI:
    def __init__(self, session: requests.Session) -> None:
        self.s = session

    @log_request
    def get(self, url, params=None, headers=None, *args, **kwargs) -> requests.Response:
        response = self.s.get(url, params=params, headers=headers, *args, **kwargs)
        return response

    @log_request
    def post(self, url, data=None, json=None, headers=None, *args, **kwargs) -> requests.Response:
        response = self.s.post(url, data=data, json=json, headers=headers, *args, **kwargs)
        return response

    @log_request
    def put(self, url, data=None, json=None, headers=None, *args, **kwargs) -> requests.Response:
        response = self.s.put(url, data=data, json=json, headers=headers, *args, **kwargs)
        return response

    @log_request
    def delete(self, url, headers=None, *args, **kwargs) -> requests.Response:
        response = self.s.delete(url, headers=headers, *args, **kwargs)
        return response
