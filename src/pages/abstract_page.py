import logging
from abc import ABC
from playwright.sync_api import Page, expect, Locator
from src.locators.locators import DATA_QA_PATTERN, NAME_PATTERN, VALUE_PATTERN, CLASS_PATTERN
from src.framework.step_with_logging import step_with_logging
from allure import step


class AbstractPage(ABC):
    _URL = ""
    _CHECK_VISIBILITY_CSS = ".shop-menu"

    def __init__(self, page: Page):
        self._page = page
        self.logger = logging.getLogger(__name__)

    def open_page(self) -> None:
        step_description = "Open {}".format(self._URL)
        with step(step_description):
            self._page.goto(self._URL)
            self.logger.info(step_description)
            expect(self._page.locator(self._CHECK_VISIBILITY_CSS)).to_be_visible()

    @step_with_logging("Searching element by text = {}")
    def get_element_by_text(self, text: str) -> "Locator":
        return self._page.get_by_text(text)

    @step_with_logging("Searching element by data-qa = {}")
    def find_by_data_qa(self, dataqa: str) -> "Locator":
        return self._page.locator(DATA_QA_PATTERN.format(dataqa))

    @step_with_logging("Searching element by name = {}")
    def find_by_name(self, name: str) -> "Locator":
        return self._page.locator(NAME_PATTERN.format(name))

    @step_with_logging("Searching element by value = {}")
    def find_by_value(self, value: str) -> "Locator":
        return self._page.locator(VALUE_PATTERN.format(value))

    @step_with_logging("Searching element by class_name = {}")
    def find_by_class(self, class_name: str) -> "Locator":
        return self._page.locator(CLASS_PATTERN.format(class_name))
