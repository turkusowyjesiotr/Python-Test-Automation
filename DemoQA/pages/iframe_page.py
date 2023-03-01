from selenium.webdriver.common.by import By
from base.base_form import BaseForm
from web_elements.card import Card
from web_elements.button import Button
from web_elements.text import Text
from web_elements.frame import Frame
from utils.logger import Logger


class IframePage(BaseForm):
    log = Logger.logger()
    alerts_card = Card((By.XPATH, '//div[@class="card-body"]/h5[contains(text(), "Alerts")]'), 'alerts_card')
    nested_frames_button = Button((By.XPATH, '//span[contains(text(), "Nested Frames")]'), 'nested_frames_button')
    parent_frame = Frame((By.ID, 'frame1'), 'parent_frame')
    parent_frame_text = Text((By.XPATH, '//body'), 'parent_frame_text')
    child_frame = Frame((By.XPATH, '//iframe[contains(@srcdoc, "Child Iframe")]'), 'child_frame')
    child_frame_text = Text((By.XPATH, '//body/p'), 'child_frame_text')
    frames_button = Button((By.XPATH, '//span[contains(text(), "Frames")]'), 'frames_button')
    upper_frame = Frame((By.ID, 'frame1'), 'upper_frame')
    upper_frame_text = Text((By.ID, 'sampleHeading'), 'upper_frame_text')
    lower_frame = Frame((By.ID, 'frame2'), 'lower_frame')
    lower_frame_text = Text((By.ID, 'sampleHeading'), 'lower_frame_text')

    def __init__(self):
        super().__init__()

    def is_main_page_open(self):
        self.log.info('Iframe Page test')
        self.log.info('Opening main page')
        self.log.info(f'Asserting that we are on main page by searching for {self.alerts_card.name} element')
        return self.is_form_open(self.alerts_card.locator)

    def click_alerts_card(self):
        self.log.info(f'Clicking {self.alerts_card.name} element')
        self.alerts_card.click_element()

    def click_nested_frames_button(self):
        self.log.info(f'Clicking {self.nested_frames_button.name} element')
        self.nested_frames_button.click_element()

    def is_page_with_nested_frames_open(self):
        self.log.info(f'Checking if page with nested frames is open with {self.parent_frame.name} presence')
        return self.parent_frame.is_element_present()

    def get_parent_frame_text(self, driver):
        self.log.info(f'Switching frame to {self.parent_frame.name}')
        driver.switch_to.frame(self.parent_frame.get_element())
        frame_text = self.parent_frame_text.get_text()
        self.log.info(f'Checking for {self.parent_frame_text.name} element text')
        return frame_text

    def get_child_frame_text(self, driver):
        self.log.info(f'Switching frame to {self.child_frame.name}')
        driver.switch_to.frame(self.child_frame.get_element())
        frame_text = self.child_frame_text.get_text()
        self.log.info(f'Checking for {self.child_frame_text.name} element text')
        return frame_text

    def click_frames_button(self, driver):
        self.log.info(f'Clicking {self.frames_button.name} element')
        driver.switch_to.default_content()
        self.frames_button.click_element()

    def is_page_with_frames_open(self):
        self.log.info(f'Checking if page with frames is open with presence of {self.upper_frame.name} element')
        return self.upper_frame.is_element_present()

    def get_upper_frame_text(self, driver):
        self.log.info(f'Switching frame to {self.upper_frame.name}')
        driver.switch_to.frame(self.upper_frame.get_element())
        self.log.info(f'Checking for {self.upper_frame_text.name} element text')
        frame_text = self.upper_frame_text.get_text()
        driver.switch_to.default_content()
        return frame_text

    def get_lower_frame_text(self, driver):
        self.log.info(f'Switching frame to {self.lower_frame.name}')
        driver.switch_to.frame(self.lower_frame.get_element())
        self.log.info(f'Checking for {self.lower_frame_text.name} element text')
        frame_text = self.lower_frame_text.get_text()
        driver.switch_to.default_content()
        return frame_text
