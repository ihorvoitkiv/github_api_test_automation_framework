import pytest
import requests

from config_reader import Config


@pytest.fixture(scope='session')
def session():
    return requests.Session()


@pytest.fixture(scope='session')
def auth_headers():
    # Secure way to store sensitive data via env. variable:
    # access_token = os.environ.get('ACCESS_TOKEN')
    return Config.get_auth_headers()


@pytest.fixture(scope='session')
def user_creds():
    return Config.get_user_options()
