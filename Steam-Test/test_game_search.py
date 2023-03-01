import pytest
from pages.steam_game_search import SteamGameSearch
from utils.browser import Browser


@pytest.mark.usefixtures('setup')
class TestGameSearch:
    def test_game_search(self, setup):
        game_name = setup['game_name']
        browser = Browser(self.driver)
        page = SteamGameSearch(browser.get_driver())
        page.search_game(game_name)
        assert page.is_result_page_open(), 'Result page is not open'
        assert game_name in page.search_box_contains_game(), 'Searched name not in search box on result page'
        assert game_name == page.search_results_first_title(), 'First name not equal to searched name'
        first_result = page.get_game_information(0)
        second_result = page.get_game_information(1)
        second_game = second_result.title
        page.search_game(second_game)
        assert second_game in page.search_box_contains_game(), 'Searched name from saved results not in search box'
        assert page.is_game_information_in_results(first_result), 'Stored data is not matching result list'
        assert page.is_game_information_in_results(second_result), 'Stored data is not matching result list'
