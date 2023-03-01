from selenium.webdriver.common.by import By
from base.base_form import BaseForm
from web_elements.card import Card
from web_elements.button import Button
from web_elements.link import Link
from pages.sample_page import SamplePage
from utils.logger import Logger


class HandlesPage(BaseForm):
    log = Logger.logger()
    alerts_card = Card((By.XPATH, '//div[@class="card-body"]/h5[contains(text(), "Alerts")]'), 'alerts_card')
    browser_windows_button = Button((By.XPATH, '//span[contains(text(), "Browser Windows")]'), 'browser_windows_button')
    new_tab_button = Button((By.ID, 'tabButton'), 'new_tab_button')
    sample_page = SamplePage((By.ID, 'sampleHeading'), 'sample_page_heading')
    elements_button = Button((By.XPATH, '//div[@class="header-wrapper"]//div[contains(text(), "Elements")]'), 'elements_button')
    links_button = Button((By.XPATH, '//span[contains(text(), "Links")]'), 'links_button')
    home_link = Link((By.ID, 'simpleLink'), 'home_link')

    def __init__(self):
        super().__init__()

    def is_main_page_open(self):
        self.log.info('Handles Page test')
        self.log.info('Opening main page')
        self.log.info(f'Asserting that we are on main page by searching for {self.alerts_card.name} element')
        return self.is_form_open(self.alerts_card.locator)

    def click_alerts_card(self):
        self.log.info(f'Clicking on {self.alerts_card.name} element')
        self.alerts_card.click_element()

    def click_browser_windows_button(self):
        self.log.info(f'Clicking on {self.browser_windows_button.name} element')
        self.browser_windows_button.click_element()

    def is_page_with_browser_windows_open(self):
        self.log.info(f'Checking if page with browser windows is open with presence of {self.new_tab_button.name} element')
        return self.new_tab_button.is_element_present()

    def click_new_tab_button(self):
        self.log.info(f'CLicking {self.new_tab_button.name} element')
        self.new_tab_button.click_element()

    def is_sample_page_open(self):
        self.log.info(f'Checking if new tab is open with presence of {self.sample_page.name} element')
        return self.sample_page.is_form_open(self.sample_page.locator)

    def click_elements_button(self):
        self.log.info(f'Clicking {self.elements_button.name} element')
        self.elements_button.click_element()

    def click_links_button(self):
        self.log.info(f'Clicking {self.links_button.name} element')
        self.links_button.click_element()

    def is_links_page_open(self):
        self.log.info(f'Checking if links page is open with presence of {self.home_link.name} element')
        return self.home_link.is_element_present()

    def click_home_link(self):
        self.log.info(f'Clicking {self.home_link.name} element')
        self.home_link.click_element()
