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
radio_button3=driver.find_element(By.XPATH,"//input[@value='radio3']")
radio_button3.click()
assert radio_button3.is_selected(),"radio button 3 is not selected"
driver.quit()