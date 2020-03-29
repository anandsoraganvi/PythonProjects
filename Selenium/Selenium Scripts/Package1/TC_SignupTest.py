import unittest

class SignupTest(unittest.TestCase):
    def test_signupbyEmail(self):
        print("This is signup by Email test")
        self.assertTrue(True)#To pass this test intentionally

    def test_signupbyFacebook(self):
        print("This is signup by Facebook test")
        self.assertTrue(True)#To pass this test intentionally

    def test_signupbyTwitter(self):
        print("This is signup by Twitter test")
        self.assertTrue(True)#To pass this test intentionally


if __name__=="main":
    unittest.main()

