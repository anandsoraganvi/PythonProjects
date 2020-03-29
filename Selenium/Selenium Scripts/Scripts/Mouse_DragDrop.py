
from selenium import  webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains

driver = webdriver.Chrome("C:/Users/anaso/PycharmProjects/Selenium/Selenium Scripts/Drivers/chromedriver.exe")
driver.maximize_window()

driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
driver.set_page_load_timeout(4)
n=len(driver.find_elements(By.CLASS_NAME,"dragableBox"))//2
print(n)
time.sleep(2)
#driver.find_element_by_id("box1").click()
for i in range(1,n+1):
    box=driver.find_element(By.ID,"box"+str(i)+"")
    target=driver.find_element(By.ID,"box10"+str(i)+"")
    action=ActionChains(driver)
    action.drag_and_drop(box,target).perform()
    time.sleep(1)