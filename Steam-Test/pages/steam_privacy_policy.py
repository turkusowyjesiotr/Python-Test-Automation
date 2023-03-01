from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class SteamPrivacyPolicy:
    def __init__(self, driver):
        self.driver = driver
        self.original_window = self.driver.current_window_handle
        self.refuse_cookies = (By.XPATH, '//div[@id="rejectAllButton"]')
        self.privacy_policy_btn = (By.XPATH, '//div[@id="footer_text"]//a[contains(@href, "privacy")]')
        self.languages_list = (By.XPATH, '//div[@id="languages"]')
        self.languages_list_elements = (By.XPATH, '//div[@id="languages"]/a')
        self.revision_date = (By.XPATH, '//div[@id="newsColumn"]/i[last()]')

    def scroll_to_privacy_policy(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.refuse_cookies))
        element.click()
        privacy_button = self.driver.find_element(*self.privacy_policy_btn)
        privacy_button.click()

    def is_privacy_policy_in_new_tab(self):
        new_url = self.driver.current_url
        open_tabs = len(self.driver.window_handles)
        return 'privacy' in new_url, open_tabs == 2

    def switch_language_list_displayed(self):
        return self.driver.find_element(*self.languages_list)

    def all_supported_languages_displayed(self):
        languages_elements = self.driver.find_elements(*self.languages_list_elements)
        languages_list = []
        for element in languages_elements:
            language = element.get_attribute('href').split('/')[-2]
            languages_list.append(language)
        return sorted(languages_list)

    def revision_year(self):
        return self.driver.find_element(*self.revision_date).text
