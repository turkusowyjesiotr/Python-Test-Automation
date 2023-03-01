from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from models.game_model import GameModel


class SteamGameSearch:
    def __init__(self, driver):
        self.driver = driver
        self.header_search_bar = (By.XPATH, '//input[@id="store_nav_search_term"]')
        self.result_search_bar = (By.XPATH, '//input[@id="term"]')
        self.search_results_container = (By.XPATH, '//div[@id="search_result_container"]')
        self.search_results_titles = (By.XPATH, '//span[@class="title"]')
        self.search_results_platforms = (By.XPATH, './/span[contains(@class, "platform_img")]')
        self.search_results_release_dates = (By.XPATH, '//div[contains(@class, "search_released")]')
        self.search_results_reviews = (By.XPATH, '//span[contains(@class, "search_review_summary")]')
        self.search_results_prices = (By.XPATH, '//div[contains(@class, "search_price_discount_combined")]')
        self.game_info = (By.XPATH, '//div[@class="responsive_search_name_combined"]')

    def search_game(self, game_name):
        self.driver.find_element(*self.header_search_bar).send_keys(game_name + Keys.ENTER)

    def is_result_page_open(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.search_results_container))
        return element

    def search_box_contains_game(self):
        return self.driver.find_element(*self.result_search_bar).get_attribute('value')

    def search_results_first_title(self):
        results = self.driver.find_elements(*self.search_results_titles)
        return results[0].text

    def get_game_information(self, index: int):
        title = self.driver.find_elements(*self.search_results_titles)[index].text
        searched_games = self.driver.find_elements(*self.game_info)
        platforms = []
        spans = searched_games[index].find_elements(*self.search_results_platforms)
        for span in spans:
            class_name = span.get_attribute('class')
            platforms.append(class_name)
        release_date = self.driver.find_elements(*self.search_results_release_dates)[index].text
        reviews = self.driver.find_elements(*self.search_results_reviews)[index].get_attribute('data-tooltip-html')
        price = self.driver.find_elements(*self.search_results_prices)[index].get_attribute('data-price-final')
        return GameModel(title, platforms, release_date, reviews, price)

    def is_game_information_in_results(self, saved_game_information):
        game_name = saved_game_information.title
        titles = self.driver.find_elements(*self.search_results_titles)
        index = 0
        for title in titles:
            if game_name == title.text:
                index = titles.index(title)
        return saved_game_information == self.get_game_information(index)
