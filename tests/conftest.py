import os
import pytest
from dotenv import load_dotenv
from selene import browser

load_dotenv()
DOMAIN_URL = 'https://demowebshop.tricentis.com/'
LOGIN = os.getenv('LOGIN')
PASSWORD = os.getenv('PASSWORD')


@pytest.fixture(scope='function', autouse=True)
def setup_browser():
    browser.open(DOMAIN_URL)
    browser.config.base_url = "DOMAIN_URL"
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    yield browser

    browser.quit()