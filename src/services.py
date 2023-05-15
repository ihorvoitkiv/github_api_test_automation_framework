import requests
from config_reader import Config
from src.file_handler import JSONFile
from src.http_manager import RequestAPI


class URLs:
    BASE_URL = Config.get_base_url()
    USERS_URL = BASE_URL + 'users/'
    REPO_URL = USERS_URL + "{owner}/repos/"
    BRANCHES_URL = BASE_URL + "repos/{owner}/{repo}/branches/"
    PULL_URL = BASE_URL + "repos/{owner}/{repo}/pulls/"


class GitHubService(RequestAPI):
    def __init__(self, session: requests.Session) -> None:
        super().__init__(session)
        self.session.headers = {"Accept": "application/vnd.github+json"}
        self.auth_headers = Config.get_auth_headers()


class UsersAPI(GitHubService):
    """
    https://docs.github.com/en/rest/users/users?apiVersion=2022-11-28
    """

    def authorization(self):
        return self.get(URLs.USERS_URL, headers=self.auth_headers)

    def auth_invalid_token(self):
        return self.get(URLs.USERS_URL, headers={"Authorization": "Bearer INVALID_ACCESS_TOKEN"})

    def auth_missing_token(self):
        return self.get(URLs.USERS_URL, headers={})


class RepositoriesAPI(GitHubService):
    """
    https://docs.github.com/en/rest/repos/repos?apiVersion=2022-11-28
    """

    def get_all_repos(self, owner):
        return self.get(URLs.REPO_URL.format(owner), headers=self.auth_headers)


class BranchesAPI(GitHubService):
    """
    https://docs.github.com/en/rest/branches/branches?apiVersion=2022-11-28
    """

    def get_all_branches(self, owner, repo):
        return self.get(URLs.BRANCHES_URL.format(owner, repo), headers=self.auth_headers)


class PullsAPI(GitHubService):
    """
    https://docs.github.com/en/rest/pulls/pulls?apiVersion=2022-11-28
    """

    def get_all_pr(self, owner, repo):
        return self.get(URLs.PULL_URL.format(owner, repo), headers=self.auth_headers)

    def create_pr(self, owner, repo):
        payload = JSONFile("create_pr.json").read()
        return self.post(URLs.PULL_URL.format(owner, repo), headers=self.auth_headers, json=payload)

    def approve_pr(self, owner, repo, pull_number):
        payload = JSONFile("approve_pr.json").read()
        return self.post(URLs.PULL_URL.format(owner, repo) + f"{pull_number}/reviews",
                         headers=self.auth_headers,
                         json=payload)

    def delete_pr(self, owner, repo, pull_number):
        return self.delete(URLs.PULL_URL.format(owner, repo) + f"{pull_number}",
                           headers=self.auth_headers)
