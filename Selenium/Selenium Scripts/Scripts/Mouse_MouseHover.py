
from selenium import  webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains

driver = webdriver.Chrome("C:/Users/anaso/PycharmProjects/Selenium/Selenium Scripts/Drivers/chromedriver.exe")
driver.maximize_window()

driver.get("https://opensource-demo.orangehrmlive.com")
driver.set_page_load_timeout(4)

driver.find_element_by_id("txtUsername").send_keys("admin")
driver.find_element_by_id("txtPassword").send_keys("admin123")
driver.find_element_by_id("btnLogin").click()

admin=driver.find_element_by_xpath("//*[@id='menu_admin_viewAdminModule']")
usermang=driver.find_element_by_xpath("//*[@id='menu_admin_UserManagement']")
users=driver.find_element_by_xpath("//*[@id='menu_admin_viewSystemUsers']")
time.sleep(2)
actions=ActionChains(driver)
actions.move_to_element(admin).move_to_element(usermang).move_to_element(users).click().perform()




