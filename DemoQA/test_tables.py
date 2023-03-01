import string
import pytest
from pages.tables_page import TablesPage
from models.user_model import UserModel
from utils.json_util import JsonUtil


def get_test_data():
    test_data = JsonUtil('data/test_data.json').get_json_data()
    return test_data


def create_user_models():
    user_data = get_test_data()
    user_one_args = list(user_data['users'][0].values())
    user_two_args = list(user_data['users'][1].values())
    user_one = UserModel(*user_one_args)
    user_two = UserModel(*user_two_args)
    return user_one, user_two


@pytest.mark.parametrize('user', [*create_user_models()])
@pytest.mark.usefixtures('setup')
class TestTables:
    def test_tables(self, user):
        page = TablesPage()
        assert page.is_main_page_open(), 'Main page is not open'
        page.click_elements_card()
        page.click_web_tables_button()
        assert page.is_web_tables_page_open(), 'Web Tables page is not open'
        page.click_add_button()
        assert page.is_registration_form_open(), 'Registration form is not open'
        page.fill_in_registration_form(user)
        user_info = sorted(user.get_user_info_list())
        displayed_info = sorted(page.user_info_correctly_displayed())
        assert user_info == displayed_info, 'User info does not match displayed info'
        page.click_delete_user_info_row()
        displayed_info_after_delete = sorted(page.user_info_correctly_displayed())
        assert user_info != displayed_info_after_delete, 'Number of rows did not change'
        assert page.is_user_info_row_deleted() not in string.ascii_letters, 'User info is not deleted'
