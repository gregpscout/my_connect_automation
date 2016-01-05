Feature: Scout Connect Smoke Test

Background:
    Given I am on the Scout Connect login page
    When I log in with username "scout_dev@goscoutgo.com" and password "scouttest7"
    Then element "logout" should be available on page

Scenario: Verify logout
    When I choose to log out
    Then I should see text "Log in"
    And element "Forgot password" should be available on page

Scenario: Check elements on login page
    When I choose to log out
    Then I should see "copyright" on page
    And I should see "logo" on page

Scenario: Verify login with incorrect credentials returns correct error messages
    When I choose to log out
    And I log in with username "incorrect@goscoutgo.com" and password "incorrect"
    Then element "Forgot password" should be available on page
    And I should see text "Your login credentials are incorrect."

    When I click on "scout_support@goscoutgo.com"
    And I return to the last active browser window
    Then I should not see text "404"
    And I should not see text "500"

    When I return to the last active browser window
    And I log in with username "scout_dev@goscoutgo.com" and password "scouttest7"
    Then element "logout" should be available on page
    And I should see text "Jobs Marketplace"

    And I should see "logo" on page
    And I should see "copyright" on page
    And element "help" should be available on page
    And element "feedback" should be available on page
    And element "logout" should be available on page


Scenario: Search for jobs containing certain text in their title
    Given I am on Jobs Marketplace page
    When I search for jobs containing "Test" in their title
    Then I should not see text "0 jobs that contain "Test""

    And I should see "logo" on page
    And I should see "copyright" on page
    And element "help" should be available on page
    And element "feedback" should be available on page
    And element "logout" should be available on page


Scenario: Search for a job and verify the job details page
    Given I am on Jobs Marketplace page
    When I search for jobs containing "Shell Test Manager" in their title
    Then I should see text "jobs that contain"

    When I click on a job where the title contains "Shell Test Manager"

    Then I should see text "Job Details"
    And I should see text "TALENTDRIVE2"
    And I should see text "Shell Test Manager A"
    And I should see text "portland, OR"
    And I should see text "$110,000 - $119,999"
    And I should see text "Fee: 5%"
    And I should see text "open to bid"
    And I should see text "days old"
    And I should see text "Job req ID: 4031"
    And I should see text "Job description"
    And I should see text "Even more stuff about the job"
    And I should see text "Additional Information"

    And I should see "logo" on page
    And I should see "copyright" on page
    And element "help" should be available on page
    And element "feedback" should be available on page
    And element "logout" should be available on page

@submit
Scenario: Submit a candidate
    Given I am on Jobs Marketplace page
    When I search for jobs containing "Shell Test Manager" in their title
    Then I should see text "jobs that contain"

    When I click on a job where the title contains "Shell Test Manager"
    And I click to submit a candidate to the job
    
    Then I should see "logo" on page
    And I should see "copyright" on page
    And element "help" should be available on page
    And element "feedback" should be available on page
    And element "logout" should be available on page

    When I fill in information for a new candidate
    And I select fee "27%"
    And I upload resume file with path "/Users/ramona.suciu/Desktop/resumes/supervisor coordinator.pdf"
    And I agree to the candidate requirements
    And I click on "Submit Candidate" button
    Then I should see a successful alert message

@submit
Scenario: Verify candidate submission
    Given I am on Jobs Marketplace page
    When I search for jobs containing "Shell Test Manager" in their title
    Then I should see text "jobs that contain"

    When I click on a job where the title contains "Shell Test Manager"
    Then I should see my candidate submitted

Scenario: Error messages are displayed when candidate info is missing
    Given I am on Jobs Marketplace page
    When I search for jobs containing "Shell Test Manager" in their title
    Then I should see text "jobs that contain"

    When I click on a job where the title contains "Shell Test Manager"
    
    And I click to submit a candidate to the job
    And I do not provide all information required for a new candidate
    And I agree to the candidate requirements
    And I click on "Submit Candidate" button

    Then I should see an error alert message
    And I should see text "Your candidate could not be submitted, please correct the fields below and try again."
    And I should see text "Please enter First Name and try again."
    And I should see text "Please enter Last Name and try again."
    And I should see text "Please enter an email and try again."
    And I should see text "No file chosen"
    And I should see text "Resume file required."

@error
Scenario: Error message is displayed if the resume provided is not an accepted file format
    Given I am on Jobs Marketplace page
    When I search for jobs containing "Shell Test Manager" in their title
    Then I should see text "jobs that contain"

    When I click on a job where the title contains "Shell Test Manager"
    And I click to submit a candidate to the job

    When I fill in information for a new candidate
    And I select fee "27%"
    And I upload resume file with path "/Users/ramona.suciu/Desktop/resumes/marketing_executive.jpg"
    And I agree to the candidate requirements
    And I click on "Submit Candidate" button

    Then I should see an error alert message
    And I should see text "Your candidate could not be submitted, please correct the fields below and try again."
    And I should see text "Only pdf, doc, and docx files accepted."
    And I should see text "Please check the format of the resume file and try again."

Scenario: Error message is displayed if the resume is a file larger than 500 KB
    Given I am on Jobs Marketplace page
    When I search for jobs containing "Shell Test Manager" in their title
    Then I should see text "jobs that contain"

    When I click on a job where the title contains "Shell Test Manager"
    And I click to submit a candidate to the job

    When I fill in information for a new candidate
    And I select fee "27%"
    And I upload resume file with path "/Users/ramona.suciu/Desktop/resumes/large_resume.pdf"
    And I agree to the candidate requirements
    And I click on "Submit Candidate" button

    Then I should see an error alert message
    And I should see text "Your candidate could not be submitted, please correct the fields below and try again."
    And I should see text "Only pdf, doc, and docx files accepted."
    And I should see text "Your file is over 500kb, please try again."

@filters-wip
Scenario: Pagination and filters
    Given I am on Jobs Marketplace page
    When I select filter "sortdays-posted-desc"
    Then I should see job "Test Job 3PG Performance C - 10"
    And the URL should match "/#/jobs/all/1?sort=days-posted-asc&q=3PG"

    When I click on "3"
    Then the URL should match "/#/jobs/all/3?sort=days-posted-asc&q=3PG"

    When I select filter "sortfee-desc"
    Then the URL should match "/#/jobs/all/1?sort=days-posted-asc&q=3PG"