from src.config import url
from src.pages.abstract_page import AbstractPage
from playwright.sync_api import Page, Locator
from src.framework.step_with_logging import step_with_logging


class AccountCreatedPage(AbstractPage):
    _URL = "{}/account_created".format(url.MAIN_PAGE)
    _DATA_QA_BUTTON_CONTINUE = "continue-button"
    _DATA_QA_ACCOUNT_CREATED = "account-created"

    def __init__(self, page: Page):
        super().__init__(page)

    @property
    def account_created_title(self) -> "Locator":
        return self.find_by_data_qa(self._DATA_QA_ACCOUNT_CREATED)

    @step_with_logging("Click to button for continue usage")
    def continue_usage(self) -> None:
        self.find_by_data_qa(self._DATA_QA_BUTTON_CONTINUE).click()
