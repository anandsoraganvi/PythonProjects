from selenium import  webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome("C:/Users/anaso/PycharmProjects/Selenium/Selenium Scripts/Drivers/chromedriver.exe")
driver.maximize_window()

driver.get("http://testautomationpractice.blogspot.com/")
driver.set_page_load_timeout(4)

driver.find_element_by_xpath("//*[@id='HTML1']/h2").location_once_scrolled_into_view
#table=driver.find_element_by_name("BookTable").text
#print(table)


nrows=len(driver.find_elements(By.XPATH,"//*[@id='HTML1']/div[1]/table/tbody/tr"))
ncolumns=len(driver.find_elements(By.XPATH,"//*[@id='HTML1']/div[1]/table/tbody/tr[1]/th"))

print(nrows,ncolumns)
a=[]
#Header
for j in range(1,ncolumns+1):
    value=driver.find_element_by_xpath(f"//*[@id='HTML1']/div[1]/table/tbody/tr[1]/th["+str(j)+"]").text
    a.append(value)
    print("{:20}".format(value),end="\t")
print("\n")

#elements
for i in range(2,nrows+1):
    for j in range(1,ncolumns+1):
        value=driver.find_element_by_xpath(f"//*[@id='HTML1']/div[1]/table/tbody/tr["+str(i)+"]/td["+str(j)+"]").text
        a.append(value)
        print("{:20}".format(value),end="\t")
    print("\n")




