from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver: WebDriver, timeout: int = 10):
        self.driver = driver # Store the driver instance for page-level actions
        self.wait = WebDriverWait(driver, timeout)  # Explicit wait setup to handle dynamic elements


    def safe_click(self, locator):
        try:
            # Wait until the target element is clickable
            element = self.wait.until(EC.element_to_be_clickable(locator))
            # Scroll the element into view before clicking
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            element.click()
        except ElementClickInterceptedException:
            # If the click is intercepted, force a JS click
            self.driver.execute_script("arguments[0].click();", element)
        return element