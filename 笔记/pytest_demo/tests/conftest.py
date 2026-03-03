import pytest

from src.calculator import Calculator


@pytest.fixture
def calc():
    print("Setting up Calculator instance")
    return Calculator()

@pytest.fixture(scope="session",autouse=True)
def setup_and_teardown():
    print("Setting up session")
    yield
    print("Tearing down session")