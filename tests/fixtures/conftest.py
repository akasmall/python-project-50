import pytest


@pytest.fixture
def my_fixture():
    data = "Some data"
    return data
