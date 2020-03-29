from selenium import  webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome("C:/Users/anaso/PycharmProjects/Selenium/Selenium Scripts/Drivers/chromedriver.exe")
driver.maximize_window()
driver.get("https://seleniumhq.github.io/selenium/docs/api/java/index.html")

driver.switch_to_frame("packageListFrame")
driver.find_element_by_link_text("org.openqa.selenium").click()
time.sleep(2)

driver.switch_to_default_content()
driver.switch_to_frame("packageFrame")
driver.find_element_by_link_text("Rotatable").click()
time.sleep(2)

driver.switch_to_default_content()
driver.switch_to_frame("classFrame")
driver.find_element_by_link_text("ScreenOrientation").click()


