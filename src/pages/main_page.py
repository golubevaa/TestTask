from playwright.sync_api import Page, Locator
from allure import step

from src.config import url
from src.pages.abstract_page import AbstractPage


class MainPage(AbstractPage):
    _URL = url.MAIN_PAGE
    _SIGNUP_LOGIN_TEXT = "Signup / Login"
    _DELETE_ACCOUNT = "Delete Account"
    _LOGIN_LABEL = "Logged in as {}"

    def __init__(self, page: Page):
        super().__init__(page)

    @step("Click on 'Signup' button")
    def click_on_sign_up_button(self) -> None:
        self.logger.info("click on 'Signup' button")
        self.get_element_by_text(self._SIGNUP_LOGIN_TEXT).click()

    @step("Click on 'Signup' button")
    def delete_account(self):
        self.logger.info("click on 'Delete Account' button")
        self.get_element_by_text(self._DELETE_ACCOUNT).click()

    def login_label(self, username: str) -> "Locator":
        return self.get_element_by_text(self._LOGIN_LABEL.format(username))
