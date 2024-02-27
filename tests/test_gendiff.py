# Сначала определите фикстуру в файле, например, в файле conftest.py:
import pytest
from gendiff.generate_diff import generate_diff
from gendiff.loader import convert_json_to_str


@pytest.mark.parametrize(
    "file1, file2, file3",
    [
        (
            './tests/fixtures/file1.json',
            './tests/fixtures/file2.json',
            './tests/fixtures/diff_f1_f2.txt',
        ),
        (
            './tests/fixtures/file1.yml',
            './tests/fixtures/file2.yml',
            './tests/fixtures/diff_f1_f2.txt',
        ),
    ]
)
def test_gendiff(file1, file2, file3):
    with (
        open(file3, "r", encoding="utf-8") as f3,
    ):
        file3 = f3.read()
    res = generate_diff(file1, file2)
    assert res == file3


def test_convert_json():
    dct = {
        'key1': None,
        'key2': True
    }
    assert convert_json_to_str(dct) == {'key1': 'null', 'key2': 'true'}
