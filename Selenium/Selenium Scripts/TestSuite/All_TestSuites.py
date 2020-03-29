import unittest
from Package1.TC_LoginTest import LoginTest
from Package1.TC_SignupTest import SignupTest

from Package2.TC_PaymentReturnTest import PaymentReturnTest
from Package2.TC_PaymentTest import PaymentTest


#Get all test from LoginTest,SignUpTest,PaymentTest and PaymentReturnTest
tc1=unittest.TestLoader().loadTestsFromTestCase(LoginTest)
tc2=unittest.TestLoader().loadTestsFromTestCase(SignupTest)
tc3=unittest.TestLoader().loadTestsFromTestCase(PaymentTest)
tc4=unittest.TestLoader().loadTestsFromTestCase(PaymentReturnTest)


#Create Test Suites
SanityTestSuite=unittest.TestSuite([tc1,tc2])
MasterTestSuite=unittest.TestSuite([tc1,tc2,tc3,tc4])
FunctionalTestSuite=unittest.TestSuite([tc3,tc4])

#unittest.TextTestRunner().run(SanityTestSuite)
#unittest.TextTestRunner().run(FunctionalTestSuite)
unittest.TextTestRunner(verbosity=10).run(MasterTestSuite)

