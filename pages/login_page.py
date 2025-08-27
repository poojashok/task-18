from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

class LoginPage(BasePage):
    # Locators for login elements
    USERNAME_INPUT = (By.XPATH, "//input[@placeholder='Enter your mail']")
    PASSWORD_INPUT = (By.XPATH, "//input[@placeholder='Enter your password ']")
    SUBMIT_BTN = (By.XPATH, "//button[contains(@class, 'sign-in-pad') and contains(@class, 'primary-btn')]")

    def login(self, username: str, password: str):
        self.wait.until(EC.presence_of_element_located(self.USERNAME_INPUT)).send_keys(username) # Wait until username input is present
        self.wait.until(EC.presence_of_element_located(self.PASSWORD_INPUT)).send_keys(password) # Wait until password input is present
        self.safe_click(self.SUBMIT_BTN)   # Click the submit button
