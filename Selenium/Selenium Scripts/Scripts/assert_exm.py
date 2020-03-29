
try:
    1/0
except:
    ZeroDivisionError
    print("Devide by zero")

try:
    assert(1<0)
except:
    print("AssertionError")


import unittest


class Test(unittest.TestCase):
    def testu(self):
        self.assertEqual("A","A","Exceprt")
        a="D"

        self.assertTrue(a=="E","Error")


if __name__ == '__main__':
    unittest.main()


