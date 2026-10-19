from  selenium import  webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Firefox()
driver.get("https://apps.credence.in/practice")
driver.maximize_window()
driver.implicitly_wait(10)
radio_button=driver.find_elements(By.XPATH,"//input[@class='radioButton']")
print("no of radio buttons:",len(radio_button))
for i in radio_button:
    i.click()
    print(i.get_attribute('value'),"is selected:",i.is_selected())

driver.quit()