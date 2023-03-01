from utils.waits_util import WaitsUtil


class BaseForm:
    def __init__(self):
        self.waits = WaitsUtil.get_waits()

    def is_form_open(self, unique_locator):
        return self.waits.wait_for_element_presence(unique_locator)
