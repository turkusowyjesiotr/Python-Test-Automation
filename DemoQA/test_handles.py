import pytest
from pages.handles_page import HandlesPage
from utils.browser import Browser


@pytest.mark.usefixtures('setup')
class TestHandles:
    def test_handles(self):
        browser = Browser(self.driver)
        page = HandlesPage()
        assert page.is_main_page_open(), 'Main page is not open'
        page.click_alerts_card()
        page.click_browser_windows_button()
        assert page.is_page_with_browser_windows_open(), 'Page with browser windows is not open'
        page.click_new_tab_button()
        browser.switch_tab()
        assert page.is_sample_page_open(), 'Sample page is not open'
        browser.close_tab()
        browser.switch_tab()
        assert page.is_page_with_browser_windows_open(), 'Page with browser windows is not open'
        page.click_elements_button()
        page.click_links_button()
        assert page.is_links_page_open(), 'Links page is not open'
        page.click_home_link()
        browser.switch_tab()
        assert page.is_main_page_open(), 'Main page is not open'
        browser.switch_tab()
        assert page.is_links_page_open(), 'Links page is not open'
