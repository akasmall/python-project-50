# Сначала определите фикстуру в файле, например, в файле conftest.py:
# import pytest
from gendiff.scripts.gendiff import compare_dict


def test_gendiff(my_fixture):
    assert my_fixture == "Some data"


def test_compare_dict():
    res = compare_dict({"a": 1, "b": 2}, {"a": 2, "c": 3})
    assert res == {'a': (1, 2, '$'), 'b': (2, '', '-'), 'c': (3, '', '+')}


def test_2():
    assert 2 == 2
