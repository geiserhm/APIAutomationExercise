import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utils.config import BASE_URL


@pytest.fixture(scope="session")
def driver():
    # Ignore SSL errors
    chrome_options = Options()
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--ignore-ssl-errors=yes")
    chrome_options.add_argument("--allow-insecure-localhost")

    driver = webdriver.Chrome(options=chrome_options)
    driver.get(BASE_URL)
    return driver

@pytest.fixture(scope="session")
def teardown(driver):
    yield
    driver.quit()