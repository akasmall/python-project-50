# Сначала определите фикстуру в файле, например, в файле conftest.py:
# from tests.fixtures import file1_fixture as file1
from tests.fixtures import file1_fixture
# import file1_fixture


# Затем можно использовать эту фикстуру в своих тестах:


def test_using_fixture(file1):
    # new_ = file1_fixture
    assert file1 == "Some data"
