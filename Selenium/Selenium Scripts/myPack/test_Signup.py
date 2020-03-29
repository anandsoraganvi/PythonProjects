import pytest

@pytest.yield_fixture()
def setup():
    print("\nOpening URL to Signup")
    yield
    print("\nClosing browser after Signup")


def test_signupbyEmail(setup):
    print("This is signup by Email test")


def test_signupbyFacebook(setup):
    print("This is signup by Facebook test")
