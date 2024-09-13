import os

class Playwright:
    PAGE_VIEWPORT_SIZE = {'width': 1920, 'height': 1080}
    BROWSER = os.getenv('BROWSER') if os.getenv('BROWSER') is not None else 'chrome'
    IS_HEADLESS = os.getenv('HEADLESS') if os.getenv('HEADLESS') is not None else False
    DEFAULT_TIMEOUT = 10000