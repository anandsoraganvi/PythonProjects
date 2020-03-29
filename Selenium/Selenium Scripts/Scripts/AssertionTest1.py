import unittest
from selenium import webdriver
import time
import logging


class Test(unittest.TestCase):
    def testname(self):
        driver=webdriver.Chrome("C:/Users/anaso/PycharmProjects/Selenium/Selenium Scripts/Drivers/chromedriver.exe")
        driver.maximize_window()
        driver.get("http://google.com")
        time.sleep(2)
        Title=driver.title


        # assertEqual
        #self.assertEqual("Google", Title) # simple
        #self.assertEqual("Google", Title, "Webpage title is not same")#logging the error message
        #self.assertNotEqual("Google123", Title)  # simple
        self.assertNotEqual("Google", Title,"Webpage title is same")  # logging the error message


if __name__=="__main__":
    unittest.main()




