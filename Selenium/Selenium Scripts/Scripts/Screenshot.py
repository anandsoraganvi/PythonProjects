from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options

driver = webdriver.Chrome(executable_path="C:/Users/anaso/PycharmProjects/Selenium/Selenium Scripts/Drivers/chromedriver.exe")
driver.maximize_window()

# Site 1
driver.get("http://amazon.ca")
driver.set_page_load_timeout(4)

driver.get_screenshot_as_file("C:/Users/anaso/PycharmProjects/Selenium/Selenium Scripts/Screenshots/Amazon.png")
driver.save_screenshot("C:/Users/anaso/PycharmProjects/Selenium/Selenium Scripts/Screenshots/Amazon_new.png")