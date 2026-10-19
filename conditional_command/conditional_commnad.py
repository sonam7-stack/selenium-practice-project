#conditional command are:
#is_displayed
#is_enabled
#is_selected
import time
from re import search

from selenium import webdriver
from  selenium.webdriver.common.by import By
driver=webdriver.Firefox()
driver.get("https://apps.credence.in/practice")
driver.maximize_window()
radio_button=driver.find_element(By.XPATH,"//input[@value='radio1']")
time.sleep(2)
print(radio_button.is_displayed())
print('is enabled:',radio_button.is_enabled())
driver.quit()