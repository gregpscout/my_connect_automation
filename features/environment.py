from behave import *
import logging
from selenium import webdriver
from behave.log_capture import capture


@capture
def before_scenario(context, scenario):
    selenium_logger = logging.getLogger(
        'selenium.webdriver.remote.remote_connection')
    selenium_logger.setLevel(logging.WARN)

    # context.driver = webdriver.Firefox()
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.implicitly_wait(5)


@capture
def after_scenario(context, scenario):
    context.driver.quit()
