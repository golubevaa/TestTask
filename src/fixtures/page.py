import pytest

import src.config as config
from playwright.sync_api import Browser, BrowserContext, Page, sync_playwright

@pytest.fixture()
def page() -> Page:
    playwright = sync_playwright().start()
    if config.playwright.BROWSER == 'firefox':
        browser = get_firefox_browser(playwright)
        context = get_context(browser)
        page_data = context.new_page()
    elif config.playwright.BROWSER == 'chrome':
        browser = get_chrome_browser(playwright)
        context = get_context(browser)
        page_data = context.new_page()
    else:
        browser = get_chrome_browser(playwright)
        context = get_context(browser)
        page_data = context.new_page()
    yield page_data
    for context in browser.contexts:
        context.close()
    browser.close()
    playwright.stop()

def get_chrome_browser(playwright) -> Browser:
    return playwright.chromium.launch(
        headless=config.playwright.IS_HEADLESS
    )

def get_firefox_browser(playwright) -> Browser:
    return playwright.firefox.launch(
        headless=config.playwright.IS_HEADLESS
    )

def get_context(browser) -> BrowserContext:
    context = browser.new_context(
        viewport=config.playwright.PAGE_VIEWPORT_SIZE
    )
    context.set_default_timeout(
        timeout=config.playwright.DEFAULT_TIMEOUT
    )
    return context