from  selenium import  webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get("https://apps.credence.in/practice")
driver.maximize_window()
driver.implicitly_wait(10)
radio_button1=driver.find_element(By.XPATH,"//input[@value='radio1']")
radio_button1.click()
radio_button2=driver.find_element(By.XPATH,"//input[@value='radio2']")
radio_button2.click()

assert radio_button2.is_selected(),"radio button 3 is not selected"
driver.quit()