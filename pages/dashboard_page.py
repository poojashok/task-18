from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

class DashboardPage(BasePage):
    # Locators for dashboard elements
    DASHBOARD_HEADER = (By.XPATH, "//p[text()='Dashboard']")
    PROFILE_ICON = (By.CSS_SELECTOR, ".profile-click-icon-div img")
    LOGOUT_BTN = (By.XPATH, "//div[text()='Log out']")

    def is_loaded(self):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.DASHBOARD_HEADER))
            # Wait until dashboard header becomes visible
        except:
            return False

    def logout(self):
        # Click profile icon to reveal logout option
        self.safe_click(self.PROFILE_ICON)
        # Then click the logout button
        self.safe_click(self.LOGOUT_BTN)