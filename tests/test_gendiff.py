import pytest
from gendiff.generate_diff import generate_diff
from gendiff.loader import convert_json_to_str


@pytest.mark.parametrize(
    "file1, file2, file_stylish, file_plain, file_json",
    [
        (
            './tests/fixtures/file1.json',
            './tests/fixtures/file2.json',
            './tests/fixtures/diff_stylish.txt',
            './tests/fixtures/diff_plain.txt',
            './tests/fixtures/diff_json.txt',
        ),
        (
            './tests/fixtures/file1.yml',
            './tests/fixtures/file2.yml',
            './tests/fixtures/diff_stylish.txt',
            './tests/fixtures/diff_plain.txt',
            './tests/fixtures/diff_json.txt',
        ),
    ]
)
def test_gendiff(file1, file2, file_stylish, file_plain, file_json):
    with (
        open(file_stylish, "r", encoding="utf-8") as f_s,
        open(file_plain, "r", encoding="utf-8") as f_p,
        open(file_json, "r", encoding="utf-8") as f_j,
    ):
        file_stylish = f_s.read()
        file_plain = f_p.read()
        file_json = f_j.read()
    assert generate_diff(file1, file2, "stylish") == file_stylish
    assert generate_diff(file1, file2, "plain") == file_plain
    assert generate_diff(file1, file2, "json") == file_json
    # result = generate_diff(file1, file2, "stylish")
    # assert result == file_stylish
    # result = generate_diff(file1, file2, "plain")
    # assert result == file_plain


def test_convert_json():
    dct = {
        'key1': None,
        'key2': True
    }
    assert convert_json_to_str(dct) == {'key1': 'null', 'key2': 'true'}
