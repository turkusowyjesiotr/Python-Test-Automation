from selenium.webdriver.common.by import By
from base.base_form import BaseForm
from web_elements.card import Card
from web_elements.button import Button
from web_elements.text import Text
from utils.logger import Logger


class AlertPage(BaseForm):
    log = Logger.logger()
    alerts_card = Card((By.XPATH, '//div[@class="card-body"]/h5[contains(text(), "Alerts")]'), 'alerts_card')
    alert_button = Button((By.XPATH, '//span[contains(text(), "Alerts")]'), 'alert_button')
    click_to_see_alert_button = Button((By.ID, 'alertButton'), 'click_to_see_alert_button')
    confirm_button = Button((By.ID, 'confirmButton'), 'confirm_button')
    confirm_result = Text((By.ID, 'confirmResult'), 'confirm_result')
    prompt_button = Button((By.ID, 'promtButton'), 'prompt_button')
    prompt_result = Text((By.XPATH, '//span[@id="promptResult"]'), 'prompt_result')

    def __init__(self):
        super().__init__()

    def is_main_page_open(self):
        self.log.info('Alert Page test')
        self.log.info('Opening main page')
        self.log.info(f'Asserting that we are on main page by searching for {self.alerts_card.name} element')
        return self.is_form_open(self.alerts_card.locator)

    def click_alerts_card(self):
        self.log.info(f'Clicking on {self.alerts_card.name} element')
        self.alerts_card.click_element()

    def click_alerts_button(self):
        self.log.info(f'Clicking on {self.alert_button.name} element')
        self.alert_button.click_element()

    def is_alert_form_open(self):
        self.log.info(f'Checking if alert form is open')
        return self.click_to_see_alert_button.is_element_present()

    def click_button_to_see_alert(self):
        self.log.info(f'Clicking on {self.click_to_see_alert_button.name} element')
        self.click_to_see_alert_button.click_element()

    def click_confirm_box_will_appear_button(self):
        self.log.info(f'Clicking on {self.confirm_button.name} element')
        self.confirm_button.click_element()

    def is_confirm_result_present(self):
        self.log.info(f'Checking if {self.confirm_result.name} element is present')
        return self.confirm_result.is_element_present()

    def click_prompt_button(self):
        self.log.info(f'Clicking {self.prompt_button.name} element')
        self.prompt_button.click_element()

    def is_random_input_displayed(self):
        self.log.info(f'Checking if our input is displayed')
        return self.prompt_result.get_text()
