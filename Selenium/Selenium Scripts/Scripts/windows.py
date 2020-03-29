from selenium import  webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome("C:/Users/anaso/PycharmProjects/Selenium/Selenium Scripts/Drivers/chromedriver.exe")
driver.maximize_window()
driver.get("http://demo.automationtesting.in/Windows.html")
time.sleep(2)
driver.find_element_by_xpath("//*[@id='Tabbed']/a/button").click()
print(driver.current_window_handle) #CDwindow-B34BC9CDC075DC3972E670978DB20B21 #parent handle

handles=driver.window_handles
for i in handles:
    driver.switch_to_window(i)
    print(driver.title)
    if(driver.title=="Frames & windows"):
        driver.close()