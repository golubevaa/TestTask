from select import select

from src.config import url
from src.pages.abstract_page import AbstractPage
from playwright.sync_api import Page

class AccountCreatedPage(AbstractPage):
    _URL = "{}/account_created".format(url.MAIN_PAGE)
    _DATA_QA_BUTTON_CONTINUE = "continue-button"

    def __init__(self, page: Page):
        super().__init__(page)

    def continue_usage(self) -> None:
        self.find_by_data_qa(self._DATA_QA_BUTTON_CONTINUE).click()

