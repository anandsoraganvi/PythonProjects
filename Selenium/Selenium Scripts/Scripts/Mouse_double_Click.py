
from selenium import  webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains

driver = webdriver.Chrome("C:/Users/anaso/PycharmProjects/Selenium/Selenium Scripts/Drivers/chromedriver.exe")
driver.maximize_window()

driver.get("http://testautomationpractice.blogspot.com/")
driver.set_page_load_timeout(4)

element=driver.find_element_by_xpath("//*[@id='HTML10']/div[1]/button")
actions=ActionChains(driver)
actions.double_click(element).perform()
time.sleep(2)
print(driver.find_element_by_xpath("//*[@id='field2']").text)

