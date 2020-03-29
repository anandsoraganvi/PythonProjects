from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome("C:/Users/anaso/PycharmProjects/Selenium/Selenium Scripts/Drivers/chromedriver.exe")
driver.get("http://demo.automationtesting.in/Windows.html")
print(driver.current_url)
print(driver.title)
driver.find_element_by_xpath("//div[@id='Tabbed']//button[@class='btn btn-info'][contains(text(),'click')]").click()

print("Browser page one is closed")
print(driver.title)
time.sleep(5)
print("Browser page two is now closed")
driver.quit()