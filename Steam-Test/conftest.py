import pytest
import json
from selenium import webdriver
from utils.singleton import WebDriver


@pytest.fixture(scope='session')
def get_browser_config():
    with open('data/config_data.json', 'r') as file:
        browser_config = json.load(file)
        argument = browser_config['options']
    options = webdriver.ChromeOptions()
    options.add_argument(argument)
    return options


@pytest.fixture(scope='session')
def web_driver(get_browser_config):
    driver = WebDriver(get_browser_config).get_driver()
    yield driver
    driver.quit()


@pytest.fixture(scope='session')
def json_utils():
    with open('data/test_data.json', 'r') as file:
        test_data = json.load(file)
        return test_data


@pytest.fixture(scope='class')
def setup(request, web_driver, json_utils):
    test_data = json_utils
    base_url = test_data['base_url']
    web_driver.maximize_window()
    web_driver.get(base_url)
    request.cls.driver = web_driver
    return test_data
