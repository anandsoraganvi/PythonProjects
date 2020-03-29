import unittest
from selenium import  webdriver


def setUpModule():
    print("This is setUp module")

def tearDownModule():
    print("This is tearDown module")

class AppTesting(unittest.TestCase):
    @classmethod
    def setUp(self):
        print("This is Login test")

    @classmethod
    def tearDown(self):
        print("This is logout")


    @classmethod
    def setUpClass(cls):
        print("Open application\n")

    @classmethod
    def tearDownClass(cls):
        print("Close application")


    def test_search(self):
        print("This is search test")

    def test_advsearch(self):
        print("This is advanced search")

    def test_prepaidrecharge(self):
        print("This is prepaid recharge test")

    def test_postpaidrecharge(self):
        print("This is postpaid recharge test")


if __name__=="__main__":
    unittest.main()



