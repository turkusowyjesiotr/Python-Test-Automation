from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import NoAlertPresentException
from utils.waits_util import WaitsUtil


class Browser:
    def __init__(self, driver):
        self.driver = driver
        self.waits = WaitsUtil()
        self.alert = Alert(self.driver)

    def get_driver(self):
        return self.driver

    def is_alert_present(self):
        try:
            self.driver.switch_to.alert
        except NoAlertPresentException:
            return False

    def get_alert(self):
        alert = self.waits.wait_for_alert()
        return alert.text

    def ok_alert(self):
        alert = Alert(self.driver)
        alert.accept()

    def send_keys_to_alert(self, keys):
        alert = self.waits.wait_for_alert()
        alert.send_keys(keys)

    def switch_tab(self):
        if len(self.driver.window_handles) == 1:
            self.driver.switch_to.window(self.driver.window_handles[0])
        else:
            original_window = self.driver.current_window_handle
            for window_handle in self.driver.window_handles:
                if window_handle != original_window:
                    self.driver.switch_to.window(window_handle)
                    break

    def close_tab(self):
        self.driver.close()
