Feature: Zen Portal Login and Logout
# This feature verifies the login and logout functionality of the Zen Portal,
# includes positive and negative test cases, as well as UI validation.

  Scenario: Successful Login
    # Positive test case
    # Test scenario to validate that a user with valid credentials can login and access the dashboard before logging out
    Given I launch the Zen portal
    When I login with valid credentials
    Then I should be redirected to dashboard
    And I logout successfully

  Scenario Outline: Unsuccessful Login
    # Negative test case
    # Data-driven scenario to test invalid login attempts with incorrect credentials.
    Given I launch the Zen portal
    When I login with "<username>" and "<password>"
    Then I should see login error
    # A table of invalid credentials
    Examples:
      | username      | password   |
      | wrong@a.com   | invalid123 |

  Scenario: UI Field Validation
    #  Sanity check for the login page UI elements
    Given I launch the Zen portal
    Then username and password fields should be displayed
    And submit button should be clickable