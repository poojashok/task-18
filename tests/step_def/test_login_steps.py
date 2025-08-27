import time
import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage


# ==============================
# Feature Scenarios
# ==============================
# Load all scenarios from the specified feature file
scenarios("../features/login_and_logout.feature")


# ==============================
# Fixtures
# ==============================
@pytest.fixture
def dashboard(driver):
    """
    Provides a reusable DashboardPage instance.
    """
    return DashboardPage(driver)


# ==============================
# Step Definitions
# ==============================

@given("I launch the Zen portal")
def launch_portal(driver, credentials):
    """
    Launch the target application using the configured base URL.
    """
    driver.get(credentials["base_url"])


@when("I login with valid credentials")
def login_with_valid(driver, credentials):
    """
    Log in using valid credentials defined in the configuration.
    """
    LoginPage(driver).login(credentials["username"], credentials["password"])
    print(f"Current URL after login attempt: {driver.current_url}")


@then("I should be redirected to dashboard")
def then_dashboard_is_loaded(driver):
    """
    Validate that the user is redirected to the dashboard page.
    """
    time.sleep(5)  # Consider replacing with explicit wait for stability
    print(f"Current URL after login: {driver.current_url}")
    assert "dashboard" in driver.current_url, "Dashboard redirection failed."


@then("I logout successfully")
def logout_successfully(dashboard, driver):
    """
    Perform logout and verify navigation back to login page.
    """
    dashboard.logout()
    time.sleep(5)  # Consider replacing with explicit wait for stability
    assert "login" in driver.current_url, "Logout did not redirect to login page."


@when(parsers.parse('I login with "{username}" and "{password}"'))
def login_with_invalid(driver, username, password):
    """
    Attempt login with dynamic invalid credentials.
    """
    LoginPage(driver).login(username, password)


@then("I should see login error")
def validate_login_error(driver):
    """
    Validate that login fails and user remains on the login page.
    """
    assert "login" in driver.current_url, "Expected login failure, but navigation occurred."


@then("username and password fields should be displayed")
def validate_fields_displayed(driver):
    """
    Validate that username and password fields are visible.
    """
    LoginPage(driver).wait.until(EC.visibility_of_element_located(LoginPage.USERNAME_INPUT))
    LoginPage(driver).wait.until(EC.visibility_of_element_located(LoginPage.PASSWORD_INPUT))


@then("submit button should be clickable")
def validate_submit_clickable(driver):
    """
    Validate that the login submit button is clickable.
    """
    LoginPage(driver).wait.until(EC.element_to_be_clickable(LoginPage.SUBMIT_BTN))
