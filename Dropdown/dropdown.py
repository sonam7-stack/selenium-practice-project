from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver=webdriver.Firefox()
driver.get("https://apps.credence.in/practice")
driver.maximize_window()
driver.implicitly_wait(10)
dropdown=driver.find_element(By.ID,"dropdown-class-example")
dropdown.click()
dd_select=Select(dropdown)
dd_select.select_by_index(1)
dd_select.select_by_visible_text("Option2")
assert dd_select.first_selected_option.text=="Option2","Option2 is not selected"

driver.quit()