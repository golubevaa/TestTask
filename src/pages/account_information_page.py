from src.config import url
from src.pages.abstract_page import AbstractPage
from random import choice
from playwright.sync_api import Page

GENDER_VALUES = ("Mr", "Mrs")
MONTHS = ("January", "February", "March", "April", "May", "June",
          "July", "September", "October", "November", "December")
DAYS = [str(i) for i in range(1, 32)]
YEARS = [str(i) for i in range(1900, 2021)]
COUNTRY = ("India","United States", "Canada", "Australia", "Israel", "New Zealand", "Singapore")

class AccountInformationPage(AbstractPage):
    _URL = "{}/signup".format(url.MAIN_PAGE)
    _DATA_QA_INPUT_PASSWORD = "password"
    _DATA_QA_RADIO_TITLE = "title"
    _DATA_QA_DROPBOX_DAY = "days"
    _DATA_QA_DROPBOX_MONTH = "months"
    _DATA_QA_DROPBOX_YEAR = "years"
    _DATA_QA_INPUT_FIRST_NAME = "first_name"
    _DATA_QA_INPUT_LAST_NAME = "last_name"
    _DATA_QA_INPUT_ADDRESS = "address"
    _DATA_QA_INPUT_SEC_ADDRESS = "address2"
    _DATA_QA_INPUT_COMPANY = "company"
    _DATA_QA_INPUT_COUNTRY = "country"
    _DATA_QA_INPUT_STATE = "state"
    _DATA_QA_INPUT_CITY = "city"
    _DATA_QA_BUTTON_CREATE_ACCOUNT = "create-account"
    _DATA_QA_INPUT_ZIPCODE = "zipcode"
    _DATA_QA_INPUT_PHONE = "mobile_number"
    _NAME_CHECKBOX_NEWS = "newsletter"
    _NAME_CHECKBOX_OFFERS = "optin"
    _NAME_CHECKBOX_GENDER = "title"

    def __init__(self, page: Page):
        super().__init__(page)

    def fill_password(self, password: str) -> None:
        self.find_by_data_qa(self._DATA_QA_INPUT_PASSWORD).fill(password)

    def select_gender(self):
        current_gender = choice(GENDER_VALUES)
        self.find_by_value(current_gender).click()

    def select_date_of_birth(self):
        day = choice(DAYS)
        month = choice(MONTHS)
        year = str(choice(YEARS))
        self.find_by_data_qa(self._DATA_QA_DROPBOX_DAY).select_option(day)
        self.find_by_data_qa(self._DATA_QA_DROPBOX_MONTH).select_option(month)
        self.find_by_data_qa(self._DATA_QA_DROPBOX_YEAR).select_option(year)

    def select_newsletter_checkbox(self) -> None:
        self.find_by_name(self._NAME_CHECKBOX_NEWS).click()

    def select_offers_checkbox(self) -> None:
        self.find_by_name(self._NAME_CHECKBOX_OFFERS).click()

    def fill_first_name(self, first_name: str):
        self.find_by_data_qa(self._DATA_QA_INPUT_FIRST_NAME).fill(first_name)

    def fill_last_name(self, last_name: str):
        self.find_by_data_qa(self._DATA_QA_INPUT_LAST_NAME).fill(last_name)

    def fill_company(self, company: str):
        self.find_by_data_qa(self._DATA_QA_INPUT_COMPANY).fill(company)

    def fill_address(self, address: str) -> None:
        self.find_by_data_qa(self._DATA_QA_INPUT_ADDRESS).fill(address)

    def fill_sec_address(self, sec_address: str) -> None:
        self.find_by_data_qa(self._DATA_QA_INPUT_SEC_ADDRESS).fill(sec_address)

    def fill_state(self, state: str) -> None:
        self.find_by_data_qa(self._DATA_QA_INPUT_STATE).fill(state)

    def fill_city(self, city: str) -> None:
        self.find_by_data_qa(self._DATA_QA_INPUT_CITY).fill(city)

    def fill_zipcode(self, zipcode: str) -> None:
        self.find_by_data_qa(self._DATA_QA_INPUT_ZIPCODE).fill(zipcode)

    def fill_phone(self, phone: str) -> None:
        self.find_by_data_qa(self._DATA_QA_INPUT_PHONE).fill(phone)

    def select_country(self):
        country = choice(COUNTRY)
        self.find_by_data_qa(self._DATA_QA_INPUT_COUNTRY).select_option(country)

    def create_account(self):
        self.find_by_data_qa(self._DATA_QA_BUTTON_CREATE_ACCOUNT).click()
