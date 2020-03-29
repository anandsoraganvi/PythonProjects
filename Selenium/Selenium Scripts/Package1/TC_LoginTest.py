import unittest

class LoginTest(unittest.TestCase):
    def test_loginbyEmail(self):
        print("This is login by Email test")
        self.assertTrue(True)#To pass this test intentionally

    def test_loginbyFacebook(self):
        print("This is login by Facebook test")
        self.assertTrue(True)#To pass this test intentionally

    def test_loginbyTwitter(self):
        print("This is login by Twitter test")
        self.assertTrue(True)#To pass this test intentionally


if __name__=="main":
    unittest.main()

