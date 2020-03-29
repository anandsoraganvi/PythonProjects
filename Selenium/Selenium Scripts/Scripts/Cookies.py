from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options

driver = webdriver.Chrome(executable_path="C:/Users/anaso/PycharmProjects/Selenium/Selenium Scripts/Drivers/chromedriver.exe")
driver.maximize_window()

# Site 1
driver.get("http://amazon.ca")
driver.set_page_load_timeout(4)

cookies=driver.get_cookies()
print(len(cookies))
print(cookies)

cookie={'name':'Mycookie','value':'123456'}
driver.add_cookie(cookie)
cookies=driver.get_cookies()
print(len(cookies))
print(cookies)


driver.delete_cookie('Mycookie')
cookies=driver.get_cookies()
print(len(cookies))
print(cookies)

driver.delete_all_cookies()
cookies=driver.get_cookies()
print(len(cookies))
print(cookies)
