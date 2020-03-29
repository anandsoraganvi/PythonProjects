import unittest
from selenium import  webdriver



class App2Testings(unittest.TestCase):
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

    @unittest.skip("I am skipping")  #to skip a test
    def test_search(self):
        print("This is search test")

    @unittest.skip("I am skipping this adv_search test as its not yet ready")  # to skip a test
    def test_advsearch(self):
        print("This is advanced search")
    a=2
    b=4
    @unittest.skipIf(a<b,"Test skipped based on condition")
    def test_prepaidrecharge(self):
        print("This is prepaid recharge test")

    def test_postpaidrecharge(self):
        print("This is postpaid recharge test")


if __name__=="__main__":
    unittest.main()



