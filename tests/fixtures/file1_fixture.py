import pytest


@pytest.fixture
def my_fixture():
    # Здесь может быть любой код инициализации фикстуры
    data = "Some data"
    return data
