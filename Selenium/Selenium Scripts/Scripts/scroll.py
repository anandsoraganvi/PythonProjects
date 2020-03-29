from selenium import  webdriver
from selenium.webdriver.common.by import By
import time
import unittest

driver = webdriver.Chrome("C:/Users/anaso/PycharmProjects/Selenium/Selenium Scripts/Drivers/chromedriver.exe")
driver.maximize_window()

driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
driver.set_page_load_timeout(4)
driver.maximize_window()
a=0
#Scroll down by pixel

#driver.execute_script("window.scrollBy(0,1000)","")
#for i in range(3):

    #b=1000*i
    #driver.execute_script("window.scrollBy("+str(a)+","+str(b)+")","")
    #time.sleep(2)
    #a=b

#Method 2: Scroll down till specific element visible
flag=driver.find_element_by_xpath("//*[@id='content']/div[2]/div[2]/table[1]/tbody/tr[86]/td[2]")
driver.execute_script("arguments[0].scrollIntoView();",flag)

#Method 3 : Scroll till end of the page

driver.execute_script("window.scrollBy(0,document.body.scrollHeight)","")

#Method 4
driver.find_element_by_xpath("//*[@id='content']/div[2]/div[2]/table[2]/tbody/tr[56]/td[1]/img").location_once_scrolled_into_view
