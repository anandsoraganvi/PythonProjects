
from selenium import  webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains

driver = webdriver.Chrome("C:/Users/anaso/PycharmProjects/Selenium/Selenium Scripts/Drivers/chromedriver.exe")
driver.maximize_window()

driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
driver.set_page_load_timeout(4)

button=driver.find_element_by_css_selector("body > div.wy-grid-for-nav > section > div > div > div > p > span")
actions=ActionChains(driver)
actions.context_click(button).perform()
time.sleep(2)

#Alert management
driver.find_element_by_xpath("/html/body/ul/li[3]/span").click()
print(driver.switch_to_alert().text)
driver.switch_to_alert().accept()
