# Сначала определите фикстуру в файле, например, в файле conftest.py:
import pytest
from gendiff.generate_diff import generate_diff
from gendiff.loader import convert_json_to_str
# from gendiff.loader import none_constructor, bool_constructor


@pytest.mark.parametrize(
    "file1, file2, file3, file4",
    [
        (
            './tests/fixtures/file1.json',
            './tests/fixtures/file2.json',
            './tests/fixtures/diff_stylish.txt',
            './tests/fixtures/diff_plain.txt',
        ),
        (
            './tests/fixtures/file1.yml',
            './tests/fixtures/file2.yml',
            './tests/fixtures/diff_stylish.txt',
            './tests/fixtures/diff_plain.txt',
        ),
    ]
)
def test_gendiff(file1, file2, file3, file4):
    with (
        open(file3, "r", encoding="utf-8") as f3,
        open(file4, "r", encoding="utf-8") as f4,
    ):
        file3 = f3.read()
        file4 = f4.read()
    # res = generate_diff(file1, file2, "stylish")
    # assert res == file3
    res = generate_diff(file1, file2, "plain")
    assert res == file4


def test_convert_json():
    dct = {
        'key1': None,
        'key2': True
    }
    assert convert_json_to_str(dct) == {'key1': 'null', 'key2': 'true'}


# def test_convert_yaml():
#     node = ScalarNode(tag='tag:yaml.org,2002:bool', value='true')
#     # dct_bool = {'key2': True}
#     assert none_constructor('tag:yaml.org,2002:null', None) == 'null'
#     assert bool_constructor('tag:yaml.org,2002:bool', True) == 'true'
#     # assert none_constructor('tag:yaml.org,2002:null',
#     #                         dct_none) == {'key1': 'null'}
#     # assert bool_constructor('tag:yaml.org,2002:bool',
#     #                         dct_bool) == {'key2': 'true'}
