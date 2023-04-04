import configparser
import os


class Config:
    CONFIG_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.ini')
    _config = None

    @staticmethod
    def _get_config():
        if Config._config is None:
            Config._config = configparser.ConfigParser()
            Config._config.read(Config.CONFIG_FILE)
        return Config._config

    @staticmethod
    def get_base_url():
        return Config._get_config().get('github', 'base_url')

    @staticmethod
    def get_auth_headers():
        # Secure way to store sensitive data via env. variable:
        # token = os.environ.get('ACCESS_TOKEN')
        token = Config._get_config().get('github', 'access_token')
        return {'Authorization': f'Bearer {token}'}

    @staticmethod
    def get_user_options():
        config = Config._get_config()
        owner, repo = config.get('github', 'owner'), config.get('github', 'repo')
        return {'owner': owner, 'repo': repo}

