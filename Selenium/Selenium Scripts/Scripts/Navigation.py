from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome("C:/Users/anaso/PycharmProjects/Selenium/Selenium Scripts/Drivers/chromedriver.exe")
driver.get("http://newtours.demoaut.com")
print(driver.title)
time.sleep(5)
driver.get("http://facebook.com")
print(driver.title)
time.sleep(5)
driver.back()
print(driver.title)
time.sleep(5)
driver.forward()
print(driver.title)
driver.close()