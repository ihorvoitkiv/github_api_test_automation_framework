import functools
import logging

import requests

import pprint

logger = logging.getLogger(__name__)


def log_request(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        request_method = func.__name__.upper()
        request_url = args[1]
        logger.info(f"{'-' * 25} Request {'-' * 25}")
        logger.info(f"Request: {request_method} {request_url}")
        logger.debug(f"Headers:\n{pprint.pformat(kwargs.get('headers', {}))}")
        logger.debug(f"Params:\n{pprint.pformat(kwargs.get('params', {}))}")
        logger.debug(f"Data:\n{pprint.pformat(kwargs.get('data'))}")
        logger.debug(f"JSON:\n{pprint.pformat(kwargs.get('json'))}")
        try:
            response = func(*args, **kwargs)
            logger.info(f"{'-' * 25} Response {'-' * 25}")
            logger.info(f"Response: {response.status_code} {response.reason}")
            logger.debug(f"Headers:\n{pprint.pformat(dict(response.headers))}")
            logger.debug(f"Body:\n{pprint.pformat(response.text)}")
            return response
        except Exception as e:
            logger.error(f"Error requesting {request_method}: {e}")
        finally:
            logger.info("=" * 100)

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
