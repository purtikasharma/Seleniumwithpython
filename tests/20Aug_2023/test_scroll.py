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
    driver.get("https://awesomeqa.com/selenium/frame_with_nested_scrolling_frame_out_of_view.html")
    iframe = driver.find_element(By.TAG_NAME, "iframe")
    action = ActionChains(driver)
    scroll_orgin = ScrollOrigin.from_element(iframe)
    action.scroll_from_origin(scroll_orgin,0,200).perform()


   # action.scroll_to_element(iframe).perform()
    time.sleep(20)
    # Scroll from element with offset 0,-50
