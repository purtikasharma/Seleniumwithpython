import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.mouse_button import MouseButton
def test_mouseaction():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")
    #clickable = driver.find_element(By.ID,"clickable")
    click = driver.find_element(By.ID,"click")
    click.click()
    #actions =ActionChains(driver)
    #click normal click
    #click and hold - click and will not release it
    #actions.click_and_hold(clickable).\
     #   key_down(Keys.SHIFT).send_keys("Purtika")\
      #  .key_up(Keys.SHIFT).perform()
    time.sleep(10)
   # actions.click(click).perform()
    #assert "resultPage.html" in driver.current_url
    #-------------
    #Action Builder --- is for mouse
    actions_buider = ActionBuilder(driver)
    actions_buider.pointer_action.pointer_down(MouseButton.BACK)
    time.sleep(5)
    actions_buider.pointer_action.pointer_down(MouseButton.BACK)
    actions_buider.perform()
