from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class WebDriver:

    class __WebDriver:
        def __init__(self, options):
            self.driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))

    driver = None

    def __init__(self, options):
        if not self.driver:
            WebDriver.driver = WebDriver.__WebDriver(options).driver

    def get_driver(self):
        return self.driver

