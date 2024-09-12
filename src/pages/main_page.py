from src.config import url
from src.pages.abstract_page import AbstractPage


class MainPage(AbstractPage):
    _URL = url.MAIN_PAGE
    _SIGNUP_LOGIN_TEXT = "Signup / Login"

    def click_on_sign_up_button(self) -> None:
        self.get_element_by_text(self._SIGNUP_LOGIN_TEXT).click()

