from base.base_element import BaseElement


class TextField(BaseElement):
    def __init__(self, locator, name):
        super().__init__(locator, name)

    def send_text(self, text):
        element = self.get_element()
        element.send_keys(text)
