from abc import ABC
from playwright.sync_api import Page, expect, Locator

class AbstractPage(ABC):
    _URL = ""
    _CHECK_VISIBILITY_CSS = ".shop-menu"
    _BY_DATA_QA = "[data-qa=\"{}\"]"
    _BY_NAME = "[name=\"{}\"]"
    _BY_VALUE = "[value=\"{}\"]"

    def __init__(self, page: Page):
        self._page = page

    def open_page(self) -> None:
        self._page.goto(self._URL)
        expect(self._page.locator(self._CHECK_VISIBILITY_CSS)).to_be_visible()

    def get_element_by_text(self, text: str) -> "Locator":
        return self._page.get_by_text(text)

    def find_by_data_qa(self, dataqa: str) -> "Locator":
        return self._page.locator(self._BY_DATA_QA.format(dataqa))

    def find_by_name(self, name: str) -> "Locator":
        return self._page.locator(self._BY_NAME.format(name))

    def find_by_value(self, value: str) -> "Locator":
        return self._page.locator(self._BY_VALUE.format(value))
