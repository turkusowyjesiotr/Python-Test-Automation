from selenium.webdriver.common.by import By
from base.base_form import BaseForm
from web_elements.card import Card
from web_elements.button import Button
from web_elements.text_field import TextField
from web_elements.table_row import TableRow
from pages.registration_form import RegistrationForm
from utils.logger import Logger


class TablesPage(BaseForm):
    log = Logger.logger()
    elements_card = Card((By.XPATH, '//div[@class="card-body"]/h5[contains(text(), "Elements")]'), 'elements_card')
    web_tables_button = Button((By.XPATH, '//span[contains(text(), "Web Tables")]'), 'web_tables_button')
    add_button = Button((By.ID, 'addNewRecordButton'), 'add_button')
    registration_form = RegistrationForm((By.ID, 'userForm'), 'registration_form')
    first_name = TextField((By.ID, 'firstName'), 'first_name_textfield')
    last_name = TextField((By.ID, 'lastName'), 'last_name_textfield')
    email = TextField((By.ID, 'userEmail'), 'email_textfield')
    age = TextField((By.ID, 'age'), 'age_textfield')
    salary = TextField((By.ID, 'salary'), 'salary_textfield')
    department = TextField((By.ID, 'department'), 'department_textfield')
    form_submit_button = Button((By.ID, 'submit'), 'form_submit_button')
    added_table_row = TableRow((By.XPATH, '//div[contains(@role, "row")][4]'), 'added_table_row')
    delete_row_button = Button((By.ID, 'delete-record-4'), 'delete_row_button')

    def __init__(self):
        super().__init__()

    def is_main_page_open(self):
        self.log.info('Iframe Page test')
        self.log.info('Opening main page')
        self.log.info(f'Asserting that we are on main page by searching for {self.elements_card.name} element')
        return self.is_form_open(self.elements_card.locator)

    def click_elements_card(self):
        self.log.info(f'Clicking on {self.elements_card.name} element')
        self.elements_card.click_element()

    def click_web_tables_button(self):
        self.log.info(f'Clicking on {self.web_tables_button.name} element')
        self.web_tables_button.click_element()

    def is_web_tables_page_open(self):
        self.log.info(f'Checking if web tables page is open with presence of {self.add_button.name} element')
        return self.add_button.is_element_present()

    def click_add_button(self):
        self.log.info(f'Clicking {self.add_button.name} element')
        self.add_button.click_element()

    def is_registration_form_open(self):
        self.log.info(f'Checking if registration form is open with presence of {self.registration_form.name} element')
        return self.registration_form.is_form_open(self.registration_form.locator)

    def fill_in_registration_form(self, user_model):
        self.first_name.send_text(user_model.first_name)
        self.log.info(f'Sending value: {user_model.first_name} to {self.first_name.name}')
        self.last_name.send_text(user_model.last_name)
        self.log.info(f'Sending value: {user_model.last_name} to {self.last_name.name}')
        self.email.send_text(user_model.email)
        self.log.info(f'Sending value: {user_model.email} to {self.email.name}')
        self.age.send_text(user_model.age)
        self.log.info(f'Sending value: {user_model.age} to {self.age.name}')
        self.salary.send_text(user_model.salary)
        self.log.info(f'Sending value: {user_model.salary} to {self.salary.name}')
        self.department.send_text(user_model.department)
        self.log.info(f'Sending value: {user_model.department} to {self.department.name}')
        self.form_submit_button.click_element()
        self.log.info(f'Clicking {self.form_submit_button.name} element')

    def user_info_correctly_displayed(self):
        self.log.info(f'Checking for information that test added in {self.added_table_row.name} element')
        row_info = self.added_table_row.get_text().split('\n')
        return row_info

    def click_delete_user_info_row(self):
        self.log.info(f'Clicking {self.delete_row_button.name} element')
        self.delete_row_button.click_element()

    def is_user_info_row_deleted(self):
        self.log.info(f'Checking that information was deleted from {self.added_table_row.name} element')
        return self.added_table_row.get_text()
