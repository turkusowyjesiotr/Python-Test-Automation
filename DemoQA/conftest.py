import pytest
from config.config_manager import ConfigManager
from browser_factory.browser_factory import BrowserFactory
from utils.waits_util import WaitsUtil
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture(scope='session')
def get_config():
    config = ConfigManager('data/config.json').get_config()
    return config


@pytest.fixture(scope='session')
def web_driver(get_config):
    browser_name = get_config['browser_name']
    driver = BrowserFactory(browser_name).get_driver()
    waits = WaitsUtil()
    waits.wait = WebDriverWait(driver, waits.timeout)
    yield driver
    driver.quit()


@pytest.fixture()
def setup(request, web_driver, get_config):
    base_url = get_config['base_url']
    web_driver.maximize_window()
    web_driver.get(base_url)
    request.cls.driver = web_driver
    yield
