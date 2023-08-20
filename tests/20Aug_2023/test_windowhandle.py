import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.mouse_button import MouseButton
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin

def test_04():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/windows")
    driver.maximize_window()
    main_window = driver.current_window_handle
    print(main_window)
    link = driver.find_element(By.LINK_TEXT, "Click Here")
    link.click()
    window_handle = driver.window_handles
    print(window_handle)
    for handle in window_handle:
        driver.switch_to.window(handle)
        if "New Window" in driver.page_source:
             print("Found the text")
             break