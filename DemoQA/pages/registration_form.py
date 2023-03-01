from base.base_form import BaseForm


class RegistrationForm(BaseForm):
    def __init__(self, locator, name):
        super().__init__()
        self.locator = locator
        self.name = name
