from src.config import url
from src.pages.abstract_page import AbstractPage
from playwright.sync_api import Page, Locator
from src.framework.step_with_logging import step_with_logging


class DeleteAccountPage(AbstractPage):
    _URL = "{}/delete_account".format(url.MAIN_PAGE)
    _DATA_QA_ACCOUNT_DELETED = "account-deleted"
    _DATA_QA_CONTINUE = "continue-button"

    def __init__(self, page: Page):
        super().__init__(page)

    @property
    def account_deleted_label(self) -> "Locator":
        return self.find_by_data_qa(self._DATA_QA_ACCOUNT_DELETED)

    @step_with_logging("Click to 'continue' button")
    def click_to_continue_button(self) -> None:
        self.find_by_data_qa(self._DATA_QA_CONTINUE).click()
