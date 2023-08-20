import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.mouse_button import MouseButton
def test_03():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")
    clickable = driver.find_element(By.ID, "clickable")
    clickable.click()
    actions = ActionChains(driver)
    actions.double_click(clickable).perform()
    time.sleep(10)
    hover = driver.find_element(By.ID,"hover")
    actions.move_to_element(hover).perform()
    time.sleep(10)
    draggable = driver.find_element(By.ID, "draggable")
    drop = driver.find_element(By.ID,"droppable")
    actions.drag_and_drop(draggable,drop).perform()
    time.sleep(5)

