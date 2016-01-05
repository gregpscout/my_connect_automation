from behave import *
from pages.connect import ConnectBasePage
from pages.connect import ConnectLoginPage
from pages.connect import ConnectJobsPage
from pages.connect import ConnectJobDetailsPage
from pages.connect import ConnectSubmitCandidatePage
from pages.connect import ConnectPasswordReset
from pages.connect import ConnectFilters


@given('I am on the Scout Connect login page')
def load_connect_login_page(context):
    context.driver.get(ConnectLoginPage.CONNECT_LOGIN_PAGE)


@given('I am on Jobs Marketplace page')
def load_connect_marketplace_page(context):
    context.driver.get(ConnectJobsPage.CONNECT_JOBS_PAGE)


@when('I log in with username "{username}" and password "{password}"')
def log_in_connect(context, username, password):
    ConnectLoginPage().login(context, username, password)


@when('I choose to log out')
def log_out(context):
    ConnectJobsPage().log_out(context)
    ConnectBasePage().check_success_alert(context)


@when('I set a new password "{password}"')
def reset_password(context, password):
    ConnectPasswordReset().reset_password(context, password)


@when('I set new password "{password_1}" and confirm password "{password_2}"')
def password_not_match(context, password_1, password_2):
    ConnectPasswordReset().password_not_match(context, password_1, password_2)


@when('I search for jobs containing "{text}" in their title')
def search_jobs(context, text):
    ConnectJobsPage().wait_for_search_field(context)
    ConnectJobsPage().search_jobs(context, text)


@when('I click on a job where the title contains "{title}"')
def select_job(context, title):
    ConnectJobsPage().select_job(context, title)


@when('I click on "{locator}"')
def click_link(context, locator):
    ConnectBasePage().click_link(context, locator)


@when('I click to submit a candidate to the job')
def submit_a_candidate(context):
    ConnectJobDetailsPage().submit_a_candidate(context)


@when('I return to the last active browser window')
def switch_to_last_window(context):
    ConnectBasePage().switch_to_last_active_window(context)


@when('I fill in information for a new candidate')
def fill_in(context):
    ConnectSubmitCandidatePage().fill_in_candidate_info(context)


@when('I do not provide all information required for a new candidate')
def missing_info(context):
    ConnectSubmitCandidatePage().missing_info(context)


@when('I upload resume file with path "{path}"')
def upload_resume(context, path):
    ConnectSubmitCandidatePage().upload_resume(context, path)


@when('I select fee "{fee}"')
def choose_fee(context, fee):
    ConnectSubmitCandidatePage().choose_fee(context, fee)


@when('I agree to the candidate requirements')
def agree_reqs(context):
    ConnectSubmitCandidatePage().agree_reqs(context)


@when('I click on "Submit Candidate" button')
def click_submit(context):
    ConnectSubmitCandidatePage().click_submit(context)


@when('I select filter "{filter_selector}"')
def select_filter(context, filter_selector):
    ConnectFilters().select_filter(context, filter_selector)


@then('I should see my candidate submitted')
def verify_candidate_submitted(context):
    ConnectJobDetailsPage().assert_candidate_submission(context)


@then('Element "{locator}" should have gone stale')
def link_has_gone_stale(context, locator):
    ConnectBasePage().link_has_gone_stale(context, locator)


@then('Element "{locator}" should be available on page')
def element_is_visible(context, locator):
    ConnectBasePage().element_is_present(context, locator)


@then('I should see a successful alert message')
def success_alert(context):
    ConnectBasePage().check_success_alert(context)


@then('I should see an error alert message')
def error_alert(context):
    ConnectBasePage().check_error_alert(context)


@then('I should see text "{text}"')
def verify_logged_out(context, text):
    ConnectBasePage().get_text(context, text)


@then('I should see "{locator}" on page')
def assert_elements_on_page(context, locator):
    ConnectLoginPage().login_element_is_present(context, locator)


@then('I should not see text "{text}"')
def text_is_not_visible(context, text):
    ConnectBasePage().text_not_visible(context, text)


@then('I should see job "{job_title}"')
def assert_result(context, job_title):
    ConnectBasePage().element_is_present(context, job_title)


@then('The URL should match "{url}"')
def match_url(context, url):
    assert url == ConnectBasePage().get_current_url(context)
