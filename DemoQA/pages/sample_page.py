from base.base_form import BaseForm


class SamplePage(BaseForm):
    def __init__(self, locator, name):
        super().__init__()
        self.locator = locator
        self.name = name
