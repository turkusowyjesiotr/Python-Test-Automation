import pytest
from pages.alert_page import AlertPage
from utils.browser import Browser
from utils.random_utils import RandomUtils


@pytest.mark.usefixtures('setup')
class TestAlerts:
    def test_alerts(self):
        browser = Browser(self.driver)
        page = AlertPage()
        assert page.is_main_page_open(), 'Main page is not open'
        page.click_alerts_card()
        page.click_alerts_button()
        assert page.is_alert_form_open(), 'Alert form is  not open'
        page.click_button_to_see_alert()
        assert browser.get_alert() == 'You clicked a button', 'Alert is not open'
        browser.ok_alert()
        assert browser.is_alert_present() is False, 'Alert is not closed'
        page.click_confirm_box_will_appear_button()
        assert browser.get_alert() == 'Do you confirm action?', 'Alert is not open'
        browser.ok_alert()
        assert page.is_confirm_result_present(), 'You selected OK is not displayed'
        page.click_prompt_button()
        random = RandomUtils()
        random_string = random.get_random_string()
        browser.send_keys_to_alert(random_string)
        browser.ok_alert()
        assert random_string in page.is_random_input_displayed(), 'Random string does not match displayed string'
