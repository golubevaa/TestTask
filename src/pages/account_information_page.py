from faker.proxy import Faker
from src.config import url
from src.pages.abstract_page import AbstractPage
from playwright.sync_api import Page, Locator
from src.framework.step_with_logging import step_with_logging
from allure import step


class AccountInformationPage(AbstractPage):
    _URL = "{}/signup".format(url.MAIN_PAGE)
    _CLASS_TITLE = "login-form"
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

    @property
    def enter_account_info_title(self) -> "Locator":
        return self.find_by_class(self._CLASS_TITLE)

    @step("Filling profile with personal data")
    def enter_account_information(self, gender: str, person: Faker, day: str, month: str, year: str) -> None:
        self.select_gender(gender)
        self.fill_password(person.password())
        self.select_date_of_birth(day, month, year)
        self.select_offers_checkbox()
        self.select_newsletter_checkbox()

    @step("Filling profile with address info")
    def enter_address_information(self, name: str, person: Faker, country: str) -> None:
        self.fill_first_name(name)
        self.fill_last_name(person.last_name())
        self.fill_company(person.company())
        self.fill_address(person.address())
        self.fill_sec_address(person.secondary_address())
        self.select_country(country)
        self.fill_state(person.state())
        self.fill_city(person.city())
        self.fill_zipcode(person.zipcode())
        self.fill_phone(person.phone_number())

    @step_with_logging("Filling password with value {}")
    def fill_password(self, password: str) -> None:
        self.find_by_data_qa(self._DATA_QA_INPUT_PASSWORD).fill(password)

    @step_with_logging("Check gender by value: '{}'")
    def select_gender(self, gender: str) -> None:
        self.find_by_value(gender).click()

    @step_with_logging("Select day of birth with day = '{}', month = '{}', year = '{}'")
    def select_date_of_birth(self, day: str, month: str, year: str):
        self.find_by_data_qa(self._DATA_QA_DROPBOX_DAY).select_option(day)
        self.find_by_data_qa(self._DATA_QA_DROPBOX_MONTH).select_option(month)
        self.find_by_data_qa(self._DATA_QA_DROPBOX_YEAR).select_option(year)

    @step_with_logging("Checking newsletter checkbox")
    def select_newsletter_checkbox(self) -> None:
        self.find_by_name(self._NAME_CHECKBOX_NEWS).click()

    @step_with_logging("Checking offers checkbox")
    def select_offers_checkbox(self) -> None:
        self.find_by_name(self._NAME_CHECKBOX_OFFERS).click()

    @step_with_logging("Fill first name input with value '{}'")
    def fill_first_name(self, first_name: str) -> None:
        self.find_by_data_qa(self._DATA_QA_INPUT_FIRST_NAME).fill(first_name)

    @step_with_logging("Fill last name input with value '{}'")
    def fill_last_name(self, last_name: str) -> None:
        self.find_by_data_qa(self._DATA_QA_INPUT_LAST_NAME).fill(last_name)

    @step_with_logging("Fill company input with value '{}'")
    def fill_company(self, company: str) -> None:
        self.find_by_data_qa(self._DATA_QA_INPUT_COMPANY).fill(company)

    @step_with_logging("Fill address input with value '{}'")
    def fill_address(self, address: str) -> None:
        self.find_by_data_qa(self._DATA_QA_INPUT_ADDRESS).fill(address)

    @step_with_logging("Fill secondary address input with value '{}'")
    def fill_sec_address(self, sec_address: str) -> None:
        self.find_by_data_qa(self._DATA_QA_INPUT_SEC_ADDRESS).fill(sec_address)

    @step_with_logging("fill state input with value '{}'")
    def fill_state(self, state: str) -> None:
        self.find_by_data_qa(self._DATA_QA_INPUT_STATE).fill(state)

    @step_with_logging("fill city input with value '{}'")
    def fill_city(self, city: str) -> None:
        self.find_by_data_qa(self._DATA_QA_INPUT_CITY).fill(city)

    @step_with_logging("Fill zipcode input with value '{}'")
    def fill_zipcode(self, zipcode: str) -> None:
        self.find_by_data_qa(self._DATA_QA_INPUT_ZIPCODE).fill(zipcode)

    @step_with_logging("Fill phone input with value '{}'")
    def fill_phone(self, phone: str) -> None:
        self.find_by_data_qa(self._DATA_QA_INPUT_PHONE).fill(phone)

    @step_with_logging("select country with option '{}'")
    def select_country(self, country: str) -> None:
        self.find_by_data_qa(self._DATA_QA_INPUT_COUNTRY).select_option(country)

    @step_with_logging("click to button 'Create Account'")
    def create_account(self) -> None:
        self.find_by_data_qa(self._DATA_QA_BUTTON_CREATE_ACCOUNT).click()
