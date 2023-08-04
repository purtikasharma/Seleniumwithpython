import pytest
from selenium import webdriver
import logging

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    yield driver
def test_open_url_and_verify_title(driver):
    LOGGER = logging.getLogger(__name__)
    LOGGER.debug('This message should go to the log file')
    LOGGER.info('So should this')
    LOGGER.warning('And this, too')
    LOGGER.error('And non-ASCII stuff, too, like Øresund and Malmö')
    driver.get("https://app.vwo.com")
    print(driver.title)
    #actual == expected result
    assert "Login - VWO" == driver.title


