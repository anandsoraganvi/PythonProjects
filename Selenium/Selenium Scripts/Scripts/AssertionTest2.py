import unittest
from selenium import webdriver
import time
import openpyxl

A="ASDD"
B="sads"

assertEquals(A,B)


class Test(unittest.TestCase):
    def testname(self):
        driver=webdriver.Chrome("C:/Users/anaso/PycharmProjects/Selenium/Selenium Scripts/Drivers/chromedriver.exe")
        driver.maximize_window()
        driver.get("http://google.com")
        time.sleep(2)
        Title=driver.title

        #writing page source to text file
        t=driver.page_source
        f = open("C:/Users/anaso/PycharmProjects/Selenium/guru99.txt", "w+")
        f.write(t)




        # assertEqual
        #self.assertEqual("Google", Title) # simple
        #self.assertEqual("Google", Title, "Webpage title is not same")#logging the error message
        #assertNotEqual
        #self.assertNotEqual("Google123", Title)  # simple
        #self.assertNotEqual("Google", Title,"Webpage title is same",logging.error("Webpage title is same") )  # logging the error message

        #self.assertTrue(Title=="Google1",logging.error("Title is not equal"))
        self.assertFalse(Title == "Google", "Title is not equal")


if __name__=="__main__":
    unittest.main()




