import pytest

@pytest.yield_fixture()
def setup():
    print("\nOpening URL to Login")
    yield
    print("\nClosing browser after login")


def test_loginbyEmail(setup):
    print("This is login by Email test")


def test_loginbyFacebook(setup):
    print("This is login by Facebook test")
