from config_reader import Config
from src.file_handler import JSONFile
from src.services import UsersAPI, RepositoriesAPI, BranchesAPI, PullsAPI

user_data = Config.get_user_options()
owner, repo = user_data.get('owner'), user_data.get('repo')
pr_data = JSONFile('create_pr.json').read()


def test_authorization(session):
    response = UsersAPI(session).authorization()
    assert response.status_code == 200
    assert response.json()["login"] == owner


def test_invalid_authorization(session):
    response = UsersAPI(session).auth_invalid_token()
    assert response.status_code == 401
    assert response.json()["message"] == "Bad credentials"


def test_missing_authorization(session):
    response = UsersAPI(session).auth_missing_token()
    assert response.status_code == 401
    assert response.json()["message"] == "Requires authentication"


def test_get_all_repositories(session):
    response = RepositoriesAPI(session).get_all_repos(owner)
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert all("name" in repo_name for repo_name in response.json())


def test_get_all_branches(session):
    response = BranchesAPI(session).get_all_branches(owner, repo)
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert all("name" in branch for branch in response.json())


def test_list_pull_requests(session):
    response = PullsAPI(session).get_all_pr(owner, repo)
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert all("title" in pr for pr in response.json())


def test_create_pull_request(session):
    response = PullsAPI(session).create_pr(owner, repo)
    assert response.status_code == 201
    response_json = response.json()
    assert response_json.get("title") == pr_data.get("title")
    assert response_json.get("state") == "open"
    assert response_json["head"]["ref"] == pr_data.get("head")
    assert response_json["base"]["ref"] == pr_data.get("base")


def test_approve_pull_request(session):
    # ToDo: Here should be test precondition
    response = PullsAPI(session).approve_pr(owner, repo, pull_number=7)
    assert response.status_code == 200
    assert response.json()["state"] == "APPROVED"


def test_delete_pull_request(session):
    # ToDo: clarify endpoint doc
    response = PullsAPI(session).delete_pr(owner, repo, pull_number=7)
    assert response.status_code == 204
