import time

from  selenium import webdriver
from  selenium.webdriver.common.by import By
driver=webdriver.Firefox()
driver.get("https://apps.credence.in/practice")
driver.maximize_window()
multiselect_checkbox=driver.find_elements(By.XPATH,"//option[contains(@value,'item')]")
print(len(multiselect_checkbox))
#approach 1
#select all checkboxes
#for i in range(len(multiselect_checkbox)):
    #multiselect_checkbox[i].click()
#=========================================
#approach 2
#for checkbox in multiselect_checkbox:
 #   checkbox.click()
#=========================================
#select first 3 checkboxes
'''
for checkbox in range(len(multiselect_checkbox)):
    if checkbox<3:
        multiselect_checkbox[checkbox].click()
'''
#select last 3 checkboxes
#for i in range(len(multiselect_checkbox)-3,len(multiselect_checkbox)):
 #   multiselect_checkbox[i].click()
#=====================================
#if it checkbox is already selected then first unselect it
#for checkbox in multiselect_checkbox:
  #  checkbox.click()
  #  if checkbox.is_selected():
   #     checkbox.click()

for i in range(len(multiselect_checkbox)):
    if i<3:
        multiselect_checkbox[i].click()
        if multiselect_checkbox[i].text == "Item 2" or multiselect_checkbox[i].text == "Item 3":
            print(f"{multiselect_checkbox[i].text} is selected")
time.sleep(3)
driver.quit()