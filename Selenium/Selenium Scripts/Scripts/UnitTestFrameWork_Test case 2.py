import unittest
from selenium import  webdriver

class SearchEngineTest(unittest.TestCase):
    def test_chrome(self):
        global driver
        self.driver=webdriver.Chrome("C:/Users/anaso/PycharmProjects/Selenium/Selenium Scripts/Drivers/chromedriver.exe")
        self.driver.get("http://google.com")
        print("Title of this page: "+self.driver.title)
        self.driver.close()

    def test_bing(self):
        self.driver=webdriver.Chrome("C:/Users/anaso/PycharmProjects/Selenium/Selenium Scripts/Drivers/chromedriver.exe")
        self.driver.get("http://bing.com")
        print("Title of this page: "+self.driver.title)
        self.driver.close()



if __name__=="__main__":
    unittest.main()



