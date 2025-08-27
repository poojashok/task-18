import pytest
from selenium import webdriver
from config import BASE_URL, USERNAME, PASSWORD, HEADLESS

@pytest.fixture(scope="session")
def driver():
    options = webdriver.ChromeOptions()  # Initialize Chrome WebDriver, Session scope ensures reuse across all tests.
    options.add_argument("--start-maximized")  # Launches browser in full screen
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit() # Clean up after test session

@pytest.fixture(scope="session")
def credentials():
    # Loads user credentials and base URL from config. and Raises errors if essential values are missing
    if not BASE_URL:
        raise ValueError("BASE_URL is missing or not loaded properly")
    if not USERNAME or not PASSWORD:
        raise ValueError("USERNAME or PASSWORD is missing")

    return {
        "base_url": BASE_URL,
        "username": USERNAME,
        "password": PASSWORD
    }