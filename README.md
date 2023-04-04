GitHub REST API (https://docs.github.com/en/rest?apiVersion=2022-11-28) Test Automation Framework<br/>

FRAMEWORK DESCRIPTION
========================
.gitignore - Specifies intentionally untracked files to ignore for Git. <br/> 
Additional information - https://git-scm.com/docs/gitignore <br/>
<br/>
config.ini - File with project configurations. Contains "base_url", "access_token", "owner", "repo" options. The settings are read by the config_reader.py file using configparser.<br/>
Additional information - https://docs.python.org/3/library/configparser.html<br/>
<br/>
config_reader.py - Class to get configs from config.ini file <br/>
pytest.ini - File with PyTest configuration. Used for pytest live logging. <br/>
Additional information - https://docs.pytest.org/en/7.1.x/how-to/logging.html <br/>
<br/>
README.md - Read me file <br/>
requirements.txt - File containing a list of all used Python packages <br/>
Additional information - https://docs.python.org/3/tutorial/venv.html#managing-packages-with-pip <br/>
<br/>
src directory <br/>
src/http_manager.py - core RequestAPI helper class that encapsulates CRUD requests methods with logging decorator<br/>
src/file_handler.py - classes to work with files<br/>
src/services.py - List of Services classes<br/>
src/data_generation.py - API Data provider class to generate precondition test data<br/>
src/data - Directory  with test data files<br/>
<br/>

test_api - Directory with api test files<br/>
test_api/test_service.py - File with services test functions<br/>
test_api/conftest.py - File with pytest fixtures<br/>


LOCAL EXECUTION
========================
BEFORE START
-------------------------
1. Install PyCharm IDE - https://www.jetbrains.com/pycharm/
2. Install Python 3.6+ - https://www.python.org/downloads/
3. Open PyCharm and clone github_rest_api_test_framework from GitHub
4. Go to github_rest_api_test_framework project root folder and install all requirements from requirements.txt file into virtual env via Pycharm GUI helper <br/>
or Terminal: https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/
https://gitlab.com/neuroflow1/qa-mobile-automation
5. Check configs:
<br/>config.ini<br/>
"base_url" - default base url of GitHub REST API<br/>
"access_token" - access token to github profile account auth:<br/> 
https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token<br/>
"owner" - GitHub profile username<br/> 
"repo" - GitHub profile repo <br/>
	
START TEST
-------------------------
1. To execute from IDE (PyCharm) set up pytest as default test runner<br/>
2. To execute from terminal use command: <br/>
   - pytest 'test_file'::'test_method'<br/>
   Additional information - https://docs.pytest.org/en/stable/usage.html <br/>
3. Execute tests from: <br/>
test_api <br/>
test_api/test_service<br/>

MORE INFO:
========================
1. Python - https://www.python.org/about/
2. PyTest - https://docs.pytest.org/en/stable/contents.html
3. Requests - https://requests.readthedocs.io/en/latest/
