from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from browser_factory.singleton import Singleton


class WaitsUtil(metaclass=Singleton):
    driver = None

    def __init__(self):
        self.timeout = 10
        self.wait = WebDriverWait(self.driver, self.timeout)

    def wait_for_element_presence(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        return element

    def wait_for_element_to_be_clickable(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        return element

    def wait_for_alert(self):
        alert = self.wait.until(EC.alert_is_present())
        return alert

    @staticmethod
    def get_waits():
        return WaitsUtil()
