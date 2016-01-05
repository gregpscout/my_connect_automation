Feature: Password reset

@password_reset
Scenario: Reset password
    Given I am on the password reset page
    Then I should see text "Create new password"
    And I should see text "Your password must be at least 8 characters long, contain letters and numbers, and not be easily guessed."
    And I should see "logo" on page
    And I should see "copyright" on page

    When I set a new password "scouttest7"
    Then I should see a successful alert message

@password_reset
Scenario: Passwords is not at least 8 characters long
    Given I am on the password reset page
    When I set a new password "test"
    Then I should see an error alert message
    And I should see text "Your password must be at least 8 characters long, contain letters and numbers, and not be easily guessed. Please try again!"

@password_reset
Scenario: Passwords do not match
    Given I am on the password reset page
    When I set new password "scouttest1" and confirm password "scouttest2"
    Then I should see an error alert message
    And I should see text "Your passwords do not match!"