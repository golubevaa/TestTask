from playwright.sync_api import Page, Locator
from src.config import url
from src.pages.abstract_page import AbstractPage
from src.framework.step_with_logging import step_with_logging
from allure import step


class LoginPage(AbstractPage):
    _URL = "{}/login".format(url.MAIN_PAGE)
    _LABEL_SIGNUP = "signup-form"
    _INPUT_NAME = "signup-name"
    _INPUT_EMAIL = "signup-email"
    _SIGNUP_BUTTON = "signup-button"

    def __init__(self, page: Page):
        super().__init__(page)

    @property
    def signup_title(self) -> "Locator":
        return self.find_by_class(self._LABEL_SIGNUP)

    @step("Filling name and email")
    def perform_sign_up_preparations(self, name: str, email: str) -> None:
        self.fill_input_name(name)
        self.fill_input_email(email)
        self.signup()

    @step_with_logging("Fill name input with value '{}'")
    def fill_input_name(self, name: str) -> None:
        self.find_by_data_qa(self._INPUT_NAME).fill(name)

    @step_with_logging("Fill email input with value '{}'")
    def fill_input_email(self, email: str) -> None:
        self.find_by_data_qa(self._INPUT_EMAIL).fill(email)

    @step_with_logging("Click on 'Signup' button")
    def signup(self) -> None:
        self.find_by_data_qa(self._SIGNUP_BUTTON).click()
