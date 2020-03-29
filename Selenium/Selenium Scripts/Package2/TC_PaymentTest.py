import unittest

class PaymentTest(unittest.TestCase):

    def test_paymentInDollar(self):
        print("This is payment in dollar test")
        self.assertTrue(True)

    def test_paymentInRuppe(self):
        print("This is payment in Rupee test")
        self.assertTrue(True)


if __name__=="__main__":
    unittest.main()
