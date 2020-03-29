import pytest

@pytest.fixture()
def setup():
    print("This is setup method executes before every method")


def testMethod1(setup):
    print("This is test method1")

def testMethod2(setup):
    print("This is test method2")

