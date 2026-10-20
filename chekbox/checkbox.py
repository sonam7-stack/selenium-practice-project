import time

from  selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Dropdown.dropdown import dd_select

driver=webdriver.Firefox()
driver.implicitly_wait(10)
driver.get("https://apps.credence.in/practice")
driver.maximize_window()
checkbox1=driver.find_element(By.ID,'checkBoxOption1')
checkbox1.click()
checkbox2=driver.find_element(By.ID,'checkBoxOption2')
checkbox2.click()
checkbox3=driver.find_element(By.ID,'checkBoxOption3')
checkbox3.click()
time.sleep(5)
assert  checkbox2.is_selected(),"checkbox2 is not selected"

driver.quit()