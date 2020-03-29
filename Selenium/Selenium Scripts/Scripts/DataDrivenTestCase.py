import XLUtils
from selenium import  webdriver
import time




path="C://Users/anaso/PycharmProjects/Selenium/Selenium Scripts/Data/Login.xlsx"

rows=XLUtils.getRowcount(path,'Sheet1')
columns=XLUtils.getColumncount(path,'Sheet1')

driver = webdriver.Chrome("C:/Users/anaso/PycharmProjects/Selenium/Selenium Scripts/Drivers/chromedriver.exe")
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com")
driver.set_page_load_timeout(4)



for i in range(2,rows+1):

    UserName=XLUtils.readData(path,'Sheet1',i,1)
    PassWord=XLUtils.readData(path,'Sheet1',i,2)
    time.sleep(1)
    driver.find_element_by_id("txtUsername").send_keys(UserName)
    driver.find_element_by_id("txtPassword").send_keys(PassWord)
    time.sleep(1)
    driver.find_element_by_id("btnLogin").click()
    curl=driver.current_url
    print(curl)
    if(curl=="https://opensource-demo.orangehrmlive.com/index.php/dashboard"):
        XLUtils.writeData(path,'Sheet1',i,3,"Test Passed")
        driver.find_element_by_link_text("Welcome Admin").click()
        time.sleep(2)
        driver.find_element_by_css_selector("#welcome-menu > ul > li:nth-child(2) > a").click()
    else:
        XLUtils.writeData(path, 'Sheet1', i, 3, "Test Failed")



