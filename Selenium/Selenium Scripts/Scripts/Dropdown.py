from selenium import  webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import  Select

driver = webdriver.Chrome("C:/Users/anaso/PycharmProjects/Selenium/Selenium Scripts/Drivers/chromedriver.exe")
driver.implicitly_wait(5)
#driver.maximize_window()

driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
driver.set_page_load_timeout(10)



driver.find_element(By.ID, "RESULT_RadioButton-9").location_once_scrolled_into_view

#dropdowns selection different ways

#Method 1 : using direct xpath to that option
#dropdown = driver.find_element(By.XPATH, "//*[@id='RESULT_RadioButton-9']/option[4]").click()

#Method 2 : using select class

dropdown=Select(driver.find_element_by_id("RESULT_RadioButton-9"))
#By visible text
dropdown.select_by_visible_text("Evening")
time.sleep(2)
#By value
dropdown.select_by_value("Radio-1")
time.sleep(2)
#By index
dropdown.select_by_index(3)#evening

#Count number of options
print(len(dropdown.options))
#Capture all options and print them
all_options=dropdown.options
for i in all_options:
    print(i.text)

#driver.find_element_by_id("RESULT_FileUpload-11'").click()

#Drop down 2
driver.get("http://testautomationpractice.blogspot.com/")
driver.set_page_load_timeout(4)

#dropdowns
driver.find_element_by_xpath("//*[@id='HTML6']/div[1]/form/fieldset[1]/label").location_once_scrolled_into_view

dropdown=driver.find_elements(By.ID, "speed")
for i in dropdown:
    print(i.text)
WE=Select(driver.find_element(By.ID, "speed"))
print(len(WE.options))
for i in WE.options:
    print(i.text)
WE.select_by_index(3)




