import requests

from config_reader import Config
from src.file_handler import JSONFile
from src.http_manager import RequestAPI


class GitHubService:
    def __init__(self, session: requests.Session) -> None:
        self.s = RequestAPI(session)
        self.s.headers = {"Accept": "application/vnd.github+json"}
        self.base_url = Config.get_base_url()
        self.auth_headers = Config.get_auth_headers()


class UsersAPI(GitHubService):
    """
    https://docs.github.com/en/rest/users/users?apiVersion=2022-11-28
    """

    def authorization(self):
        return self.s.get(f"{self.base_url}user", headers=self.auth_headers)

    def auth_invalid_token(self):
        return self.s.get(f"{self.base_url}user", headers={"Authorization": "Bearer INVALID_ACCESS_TOKEN"})

    def auth_missing_token(self):
        return self.s.get(f"{self.base_url}user", headers={})


class RepositoriesAPI(GitHubService):
    """
    https://docs.github.com/en/rest/repos/repos?apiVersion=2022-11-28
    """

    def get_all_repos(self, owner):
        return self.s.get(f"{self.base_url}users/{owner}/repos", headers=self.auth_headers)


class BranchesAPI(GitHubService):
    """
    https://docs.github.com/en/rest/branches/branches?apiVersion=2022-11-28
    """

    def get_all_branches(self, owner, repo):
        return self.s.get(f"{self.base_url}repos/{owner}/{repo}/branches", headers=self.auth_headers)


class PullsAPI(GitHubService):
    """
    https://docs.github.com/en/rest/pulls/pulls?apiVersion=2022-11-28
    """

    def get_all_pr(self, owner, repo):
        return self.s.get(f"{self.base_url}repos/{owner}/{repo}/pulls", headers=self.auth_headers)

    def create_pr(self, owner, repo):
        payload = JSONFile("create_pr.json").read()
        return self.s.post(f"{self.base_url}repos/{owner}/{repo}/pulls", headers=self.auth_headers, json=payload)

    def approve_pr(self, owner, repo, pull_number):
        payload = JSONFile("approve_pr.json").read()
        return self.s.post(f"{self.base_url}repos/{owner}/{repo}/pulls/{pull_number}/reviews",
                           headers=self.auth_headers,
                           json=payload)

    def delete_pr(self, owner, repo, pull_number):
        return self.s.delete(f"{self.base_url}repos/{owner}/{repo}/pulls/{pull_number}", headers=self.auth_headers)
