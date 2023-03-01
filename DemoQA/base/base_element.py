from utils.waits_util import WaitsUtil
from selenium.webdriver.remote.webelement import WebElement


class BaseElement:
    def __init__(self, locator, name):
        self.locator = locator
        self.name = name
        self.waits = WaitsUtil.get_waits()

    def get_element(self):
        element = self.waits.wait_for_element_presence(self.locator)
        return element

    def click_element(self):
        element = self.waits.wait_for_element_to_be_clickable(self.locator)
        element.click()

    def is_element_present(self):
        return self.waits.wait_for_element_presence(self.locator)

    def get_text(self):
        element = self.is_element_present()
        return element.text

    def get_attribute(self, attribute):
        element = self.get_element()
        result = element.get_attribute(attribute)
        return result
