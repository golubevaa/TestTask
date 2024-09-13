from src.config import url
from src.pages.abstract_page import AbstractPage
from playwright.sync_api import Page, Locator


class DeleteAccountPage(AbstractPage):
    _URL = "{}/delete_account".format(url.MAIN_PAGE)
    _DATA_QA_ACCOUNT_DELETED = "account-deleted"

    def __init__(self, page: Page):
        super().__init__(page)

    @property
    def account_deleted_label(self) -> "Locator":
        return self.find_by_data_qa(self._DATA_QA_ACCOUNT_DELETED)
