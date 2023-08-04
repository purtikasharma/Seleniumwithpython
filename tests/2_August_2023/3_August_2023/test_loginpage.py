import logging
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

def test_login():
    LOGGER = logging.getLogger(__name__)
    driver =webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://app.vwo.com")
    emailaddress_element = driver.find_element(By.ID, "login-username")
    password_field = driver.find_element(By.ID,"login-password")
    emailaddress_element.send_keys("purtikasharma4444@gmail.com")
    password_field.send_keys("Purtika@241996")

    signin = driver.find_element(By.ID,"js-login-btn")
    signin.click()
    time.sleep(5)

    LOGGER.info('title is ->  ' + driver.title)
    assert "Dashboard" in driver.title