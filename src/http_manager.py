import functools
import logging
import pprint
import requests

logger = logging.getLogger(__name__)


def log_request(func):
    """Decorator function that logs the details of an HTTP request and response."""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        request_method: str = func.__name__.upper()
        request_url: str = args[1]
        logger.info('-' * 25 + ' REQUEST ' + '-' * 25 + '->')
        logger.info(f'Method: {request_method}, URL: {request_url}')
        logger.debug(f'Headers:\n{pprint.pformat(kwargs.get("headers", {}))}')
        logger.debug(f'Params:\n{pprint.pformat(kwargs.get("params", {}))}')
        logger.debug(f'JSON:\n{pprint.pformat(kwargs.get("json"))}')
        logger.debug(f'Data:\n{pprint.pformat(kwargs.get("data"))}')
        try:
            response = func(*args, **kwargs)
            logger.info('<-' + '-' * 25 + ' RESPONSE ' + '-' * 25)
            logger.info(f'Status code: {response.status_code}, reason: {response.reason}')
            logger.debug(f'Headers:\n{pprint.pformat(dict(response.headers))}')
            logger.debug(f'Body:\n{pprint.pformat(response.text)}')
            return response
        except Exception as e:
            logger.error(f'Error requesting {request_method}: {e}')

    return wrapper


class RequestAPI:
    """
    Wrapper class for making HTTP requests using session object with logging functionality.
    """

    def __init__(self, session: requests.Session) -> None:
        """
        Initialize a RequestAPI object with a requests.Session object.

        Args:
            session (requests.Session): A requests.Session object allows persistence of certain parameters,
            such as headers or cookies, across multiple requests made with this RequestAPI instance.
            The session object is created via a pytest session fixture in the conftest.py module.
        """
        self.session = session

    @log_request
    def get(self, url: str, params: dict = None, headers: dict = None, *args, **kwargs) -> requests.Response:
        return self.session.get(url, params=params, headers=headers, *args, **kwargs)

    @log_request
    def post(self, url: str, data=None, json=None, headers: dict = None, *args, **kwargs) -> requests.Response:
        return self.session.post(url, data=data, json=json, headers=headers, *args, **kwargs)

    @log_request
    def put(self, url: str, data=None, json=None, headers: dict = None, *args, **kwargs) -> requests.Response:
        return self.session.put(url, data=data, json=json, headers=headers, *args, **kwargs)

    @log_request
    def delete(self, url: str, headers: dict = None, *args, **kwargs) -> requests.Response:
        return self.session.delete(url, headers=headers, *args, **kwargs)

