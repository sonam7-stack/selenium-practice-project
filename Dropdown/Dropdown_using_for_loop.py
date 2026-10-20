from  selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Dropdown.dropdown import dd_select

driver=webdriver.Firefox()
driver.implicitly_wait(10)
driver.get("https://apps.credence.in/practice")
driver.maximize_window()

try:

    dropdown_element=driver.find_element(By.XPATH,"//select[@id='dropdown-class-example']")
    dropdown_select=Select(dropdown_element)
    dd_options=dropdown_select.options
    print("no of options in drop down:",len(dd_options))
    for index in range(1,len(dd_options)):
        dropdown_select.select_by_index(index)
        if dropdown_select.first_selected_option.text=="Option2":
            break
        print("selected option:",dropdown_select.first_selected_option.text)
        assert dd_select.first_selected_option.text=="Option2","Option2 is not selected"
finally:
    driver.quit()