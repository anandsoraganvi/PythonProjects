import pytest

@pytest.yield_fixture()
def setup():
    print("\nThis is setup method executes before every method")
    yield
    print("\nThis is setup method executes after every method")


def testMethod1(setup):
    print("This is test method1")

def testMethod2(setup):
    print("This is test method2")

