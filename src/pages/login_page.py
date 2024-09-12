from playwright.sync_api import Page, expect, Locator
from src.config import url
from src.pages.abstract_page import AbstractPage


class LoginPage(AbstractPage):
    _URL = "{}/login".format(url.MAIN_PAGE)
    _SIGNUP_LOGIN_TEXT = "Signup / Login"
    _INPUT_NAME = "signup-name"
    _INPUT_EMAIL = "signup-email"
    _SIGNUP_BUTTON = "signup-button"

    def fill_input_name(self, text: str) -> None:
        self.find_by_data_qa(self._INPUT_NAME).fill(text)

    def fill_input_email(self, text: str) -> None:
        self.find_by_data_qa(self._INPUT_EMAIL).fill(text)

    def signup(self):
        self.find_by_data_qa(self._SIGNUP_BUTTON).click()