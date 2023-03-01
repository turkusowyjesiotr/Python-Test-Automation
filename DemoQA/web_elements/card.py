from base.base_element import BaseElement


class Card(BaseElement):
    def __init__(self, locator, name):
        super().__init__(locator, name)
