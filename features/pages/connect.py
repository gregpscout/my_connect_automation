from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import staleness_of
from selenium.common.exceptions import NoSuchElementException
# from selenium.common.exceptions import StaleElementReferenceException
# from selenium.common.exceptions import TimeoutException

from faker import Faker
fake = Faker()


class ConnectBasePage():
    _body = (By.CSS_SELECTOR, "body")
    _success_alert = (By.ID, "successMsg")
    _error_alert = (By.ID, "errorMsg")
    _scout_logo_selector = (By.ID, "logo")

    def get_text(self, context, text_to_find):
        page_text = context.driver.find_element(*self._body).text
        assert text_to_find in page_text

    def text_not_visible(self, context, text_to_find):
        page_text = context.driver.find_element(*self._body).text
        assert text_to_find not in page_text

    def click_link(self, context, locator):
        locator = (By.LINK_TEXT, locator)
        context.driver.find_element(*locator).click()

    def check_success_alert(self, context):
        WebDriverWait(context.driver, 10)\
            .until((EC.visibility_of_element_located
                   (self._success_alert)))

    def check_error_alert(self, context):
        WebDriverWait(context.driver, 10)\
            .until((EC.visibility_of_element_located
                   (self._error_alert)))

    def switch_to_last_active_window(self, context):
        context.driver.switch_to_window(context.driver.window_handles[0])
        context.driver.execute_script('window.focus()')
        context.driver.find_element(*self._scout_logo_selector).click()

    def link_has_gone_stale(self, context, link_text):
        _link_text_selector = (By.LINK_TEXT, link_text)
        try:
            element = context.driver.find_element(*_link_text_selector)
            WebDriverWait(context.driver, 10).until(
                staleness_of(element))
            return ConnectJobsPage()
        except NoSuchElementException:
            context.driver.quit()

    def element_is_present(self, context, locator):
        locator = (By.LINK_TEXT, locator)

        try:
            WebDriverWait(context.driver, 10).until(
                EC.presence_of_element_located(locator)
            )
        except:
            retry_count = 0
            while retry_count < 5:
                sleep(1)
            retry_count += 1

    def get_current_url(self, context):
        return context.driver.current_url


class ConnectLoginPage():
    _connect_username_selector = (By.ID, "emailInput")
    _connect_password_selector = (By.ID, "passwordInput")
    # _login_button_connect = (By.CLASS_NAME, "btn")
    _forgot_password_selector = (By.LINK_TEXT, "Forgot password")
    _copyright_selector = (By.ID, "copyright")
    _scout_logo_selector = (By.ID, "scout")

    CONNECT_LOGIN_PAGE = "http://127.0.0.1:4000/#/login"

    def login(self, context, connect_username, connect_password):
        context.driver.find_element(*self._connect_username_selector) \
            .clear()
        context.driver.find_element(*self._connect_username_selector) \
            .send_keys(connect_username)

        context.driver.find_element(*self._connect_password_selector) \
            .clear()
        context.driver.find_element(*self._connect_password_selector) \
            .send_keys(connect_password + Keys.RETURN)
        # context.driver.find_element(*self._login_button_connect).click()
        return ConnectJobsPage()

    def login_element_is_present(self, context, locator):
        locator = (By.ID, locator)

        try:
            WebDriverWait(context.driver, 10).until(
                EC.presence_of_element_located(locator)
            )
        except:
            retry_count = 0
            while retry_count < 5:
                sleep(1)
            retry_count += 1


class ConnectPasswordReset():
    _new_password = (By.ID, "inputPassword")
    _new_password_confirm = (By.ID, "inputPasswordConfirm")
    _submit_button = (By.CLASS_NAME, "btn")

    def reset_password(self, context, new_password):
        context.driver.find_element(*self._new_password)\
            .send_keys(new_password)
        context.driver.find_element(*self._new_password_confirm)\
            .send_keys(new_password)

        context.driver.find_element(*self._submit_button).click()
        return ConnectLoginPage()

    def password_not_match(self, context, password_1, password_2):
        context.driver.find_element(*self._new_password)\
            .send_keys(password_1)
        context.driver.find_element(*self._new_password_confirm)\
            .send_keys(password_2)

        context.driver.find_element(*self._submit_button).click()


class ConnectJobsPage():
    CONNECT_JOBS_PAGE = "http://127.0.0.1:4000/#/jobs"

    _search_field_selector = (By.ID, "searchInput")
    _search_button = (By.ID, "searchButton")
    _logout_selector = (By.LINK_TEXT, "logout")
    _submit_candidate_selector = (By.LINK_TEXT, "Submit a candidate")

    def log_out(self, context):
        context.driver.find_element(*self._logout_selector).click()
        return ConnectLoginPage()

    def wait_for_search_field(self, context):
        WebDriverWait(context.driver, 10)\
            .until((EC.visibility_of_element_located
                   (self._search_field_selector)))
        return ConnectJobsPage()

    def search_jobs(self, context, title):
        context.driver.find_element(*self._search_field_selector)\
            .send_keys(title)
        sleep(1)
        context.driver.find_element(*self._search_button).click()

    def select_job(self, context, job_title):
        _job_results_selector = (By.PARTIAL_LINK_TEXT, job_title)

        search_results = context.\
            driver.find_elements(*_job_results_selector)
        search_results[1].click()

        WebDriverWait(context.driver, 10)\
            .until((EC.visibility_of_element_located
                   (self._submit_candidate_selector)))
        return ConnectJobDetailsPage()


class ConnectSubmitCandidatePage():
    _choose_file_selector = (By.ID, "resumeFileButton")
    _fee_selector = (By.ID, "feeInput")
    _checkbox_selector = (By.ID, "checkedInput")
    _resume_input_selector = (By.ID, "resumeInput")
    _submit_button_selector = (By.ID, "submitButton")
    _first_name_selector = (By.ID, "firstNameInput")
    _last_name_selector = (By.ID, "lastNameInput")
    _email_selector = (By.ID, "emailInput")
    _notes_selector = (By.ID, "notesInput")

    random_values = {_first_name_selector: fake.first_name(),
                     _last_name_selector: fake.last_name(),
                     _email_selector: fake.email(),
                     _notes_selector: fake.bs()}

    _first_name = random_values[_first_name_selector]
    _last_name = random_values[_last_name_selector]

    def fill_in_candidate_info(self, context):
        for key, value in self.random_values.iteritems():
            context.driver.find_element(*key).clear()
            context.driver.find_element(*key).send_keys(value)

    def missing_info(self, context):
        for key in self.random_values.iterkeys():
            context.driver.find_element(*key).clear()
            context.driver.find_element(*key).send_keys(" ")

    def check_error_messages(self, context):
        pass

    def choose_fee(self, context, fee):
        select = Select(context.driver.find_element(*self._fee_selector))
        select.select_by_visible_text(fee)

    def upload_resume(self, context, file_to_upload):
        context.driver.find_element(*self._resume_input_selector).\
            send_keys(file_to_upload)

    def agree_reqs(self, context):
        try:
            context.driver.find_element(*self._checkbox_selector).click()
        except:
            found = False
            while not found:
                context.driver.execute_script("scrollTo(0, 500)")
                context.driver.find_element(*self._checkbox_selector).click()
                found = True

    def click_submit(self, context):
        try:
            context.driver.find_element(*self._submit_button_selector).click()
        except:
            found = False
            while not found:
                context.driver.execute_script("scrollTo(0, 500)")
                context.driver.find_element(*self._submit_button_selector)\
                    .click()
                found = True
        return ConnectJobDetailsPage()


class ConnectJobDetailsPage(ConnectSubmitCandidatePage):
    _submit_candidate_selector = (By.ID, "submitCandidateLink")
    _logout_selector = (By.LINK_TEXT, "logout")

    def submit_a_candidate(self, context):
        try:
            context.driver.find_element(*self._submit_candidate_selector)\
                .click()
        except:
            found = False
            while not found:
                context.driver.execute_script("scrollTo(0, 750)")
                context.driver.find_element(*self._submit_candidate_selector)\
                    .click()
                found = True
        return ConnectSubmitCandidatePage()

    def assert_candidate_submission(self, context):
        _body = (By.CSS_SELECTOR, "body")
        candidate = ConnectJobDetailsPage()
        page_text = context.driver.find_element(*_body).text

        # print page_text
        assert candidate._first_name in page_text
        assert candidate._last_name in page_text
        assert "Pendingaa" in page_text
        assert "Submitted" in page_text


class ConnectFilters():
    _days_posted_asc = (By.ID, "sortdays-posted-asc")
    _days_posted_desc = (By.ID, "sortdays-posted-desc")
    _fee_asc = (By.ID, "sortfee-asc")
    _fee_desc = (By.ID, "sortfee-desc")
    _job_title_asc = (By.ID, "sorttitle-asc")
    _job_title_desc = (By.ID, "sorttitle-desc")
    _company_asc = (By.ID, "sortcompany-asc")
    _company_desc = (By.ID, "sortcompany-desc")

    def select_filter(self, context, filter_id):
        sleep(5)
        filter_selector = (By.ID, filter_id)
        context.driver.find_element(*filter_selector).click()
