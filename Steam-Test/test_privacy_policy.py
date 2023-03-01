import pytest
import datetime
from pages.steam_privacy_policy import SteamPrivacyPolicy
from utils.browser import Browser


@pytest.mark.usefixtures('setup')
class TestPrivacyPolicy:
    def test_privacy_policy(self, setup):
        languages = sorted(setup['languages'])
        browser = Browser(self.driver)
        page = SteamPrivacyPolicy(browser.get_driver())
        page.scroll_to_privacy_policy()
        browser.change_window()
        assert all(page.is_privacy_policy_in_new_tab()), 'Privacy Policy not opened in new tab'
        assert page.switch_language_list_displayed(), 'Switch language list not displayed'
        assert languages == page.all_supported_languages_displayed(), 'Not all supported languages in the list'
        today = datetime.date.today()
        assert str(today.year) in page.revision_year(), 'Policy revision is not signed in the current year'
