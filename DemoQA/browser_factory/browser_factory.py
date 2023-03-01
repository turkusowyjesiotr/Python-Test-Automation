from browser_factory.singleton import Singleton
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService


class BrowserFactory(metaclass=Singleton):
    def __init__(self, browser):
        self.browser = browser
        self.driver = None

        if self.browser == 'chrome':
            self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        elif self.browser == 'firefox':
            self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        else:
            raise Exception(f'No browser as {self.browser} is available.')

    def get_driver(self):
        if self.driver is not None:
            return self.driver
        else:
            raise Exception('Driver not initialized')
