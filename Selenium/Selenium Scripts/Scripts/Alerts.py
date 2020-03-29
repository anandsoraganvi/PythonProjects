from selenium import  webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome("C:/Users/anaso/PycharmProjects/Selenium/Selenium Scripts/Drivers/chromedriver.exe")
driver.maximize_window()

driver.get("http://testautomationpractice.blogspot.com/")
driver.set_page_load_timeout(4)

driver.find_element_by_xpath("//*[@id='HTML9']/div[1]/button").click()
time.sleep(2)
#Press ok alert
#driver.switch_to_alert().accept()
#print(driver.find_element_by_id("demo").text)

#Press cancel alert
driver.switch_to_alert().dismiss()
print(driver.find_element_by_id("demo").text)
