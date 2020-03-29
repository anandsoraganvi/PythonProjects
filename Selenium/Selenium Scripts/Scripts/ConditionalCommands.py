from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome("C:/Users/anaso/PycharmProjects/Selenium/Selenium Scripts/Drivers/chromedriver.exe")
driver.get("https://www.computerhope.com/jargon/r/radiobut.htm")
#isselected()

driver.find_element_by_id('example').location_once_scrolled_into_view

time.sleep(1)

assert ("What is a Radio Button?" == driver.title) #or assert "str" in driver.title
print(driver.find_element_by_xpath("//*[@id='main-content']/article/form/p[1]/input[1]").is_selected())
time.sleep(1)
if(not(driver.find_element_by_xpath("//input[@type='radio' and @value='V2']").is_selected())):
    driver.find_element_by_xpath("//input[@type='radio' and @value='V2']").click()
time.sleep(1)
 # or xpath=//*[@id="main-content"]/article/form/p[1]/input[2]
time.sleep(1)
driver.find_element_by_xpath("//input[@type='radio' and @value='V3']").click()
time.sleep(1)
driver.find_element_by_xpath("//input[@type='radio' and @value='V3']").location_once_scrolled_into_view
time.sleep(1)
driver.find_element_by_xpath("//input[@type='radio' and @value='V4']").click()



