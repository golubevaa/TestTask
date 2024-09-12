from playwright.sync_api import Page, expect, Locator

DATA_QA_PATTERN = "[data-qa=\"{}\"]"

# def find_by_data_qa(dataqa: str) -> "Locator":
#     return page.locator(self._DATA_QA_PATTERN.format(dataqa))