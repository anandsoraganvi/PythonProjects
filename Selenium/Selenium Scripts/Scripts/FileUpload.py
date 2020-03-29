from selenium import  webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome("C:/Users/anaso/PycharmProjects/Selenium/Selenium Scripts/Drivers/chromedriver.exe")
driver.maximize_window()

#Site 1
driver.get("http://testautomationpractice.blogspot.com/")
driver.set_page_load_timeout(4)
driver.switch_to_frame(0)
driver.find_element_by_id("RESULT_FileUpload-11").send_keys("C://D/Sem 3/CV/graduation-april2019/QA/Anand_Soraganvi_QA_RD.pdf")


