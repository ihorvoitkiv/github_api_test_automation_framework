import pytest
import requests

from config_reader import Config


@pytest.fixture(scope="function")
def session() -> requests.Session:
    session = requests.Session()
    yield session
    session.close()


@pytest.fixture(scope='session')
def auth_headers():
    # Secure way to store sensitive data via env. variable:
    # access_token = os.environ.get('ACCESS_TOKEN')
    return Config.get_auth_headers()


@pytest.fixture(scope='session')
def user_creds():
    return Config.get_user_options()
