class Browser:
    def __init__(self, driver):
        self.driver = driver

    def change_window(self):
        original_window = self.driver.current_window_handle
        for window_handle in self.driver.window_handles:
            if window_handle != original_window:
                self.driver.switch_to.window(window_handle)
                break

    def get_driver(self):
        return self.driver
