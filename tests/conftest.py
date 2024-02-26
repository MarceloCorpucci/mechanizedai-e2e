import os
import logging
import pytest
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from config.env_mapper import ENV_MAPPER
from core.pages.login_page import LoginPage


def pytest_addoption(parser):
    parser.addoption("--target-env", action="store", default="SANDBOX", help="Target environment to be used during "
                                                                             "test execution.")


@pytest.fixture
def load_environment_variables(request):
    target_env = request.config.getoption('--target-env')
    logging.debug(f'Target Environment: {target_env}')

    path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', ENV_MAPPER[target_env]))
    logging.debug(f'.env file path: {path}')
    load_dotenv(path)


@pytest.fixture
def once_user_is_logged_in(load_environment_variables):
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get(os.getenv('BASE_URL'))
    login_page = LoginPage(driver)
    return login_page.login_using(os.getenv('TEST_USER'), os.getenv('TEST_PASSWORD'))
