import pytest
from gendiff.generate_diff import generate_diff
# from gendiff.loader import convert_json_to_str


@pytest.mark.parametrize(
    "file1, file2, formatter, file_sample",
    [
        (
            './tests/fixtures/file1.json',
            './tests/fixtures/file2.json',
            'stylish',
            './tests/fixtures/diff_stylish.txt',
        ),
        (
            './tests/fixtures/file1.json',
            './tests/fixtures/file2.json',
            'plain',
            './tests/fixtures/diff_plain.txt',
        ),
        (
            './tests/fixtures/file1.json',
            './tests/fixtures/file2.json',
            'json',
            './tests/fixtures/diff_json.txt',
        ),
        (
            './tests/fixtures/file1.yml',
            './tests/fixtures/file2.yml',
            'stylish',
            './tests/fixtures/diff_stylish.txt',
        ),
        (
            './tests/fixtures/file1.yml',
            './tests/fixtures/file2.yml',
            'plain',
            './tests/fixtures/diff_plain.txt',
        ),
        (
            './tests/fixtures/file1.yml',
            './tests/fixtures/file2.yml',
            'json',
            './tests/fixtures/diff_json.txt',
        ),
    ]
)
def test_gendiff(file1, file2, formatter, file_sample):
    with (
        open(file_sample, "r", encoding="utf-8") as f_f
    ):
        data_sample = f_f.read()
    res = generate_diff(file1, file2, formatter)
    assert res == data_sample


# def test_convert_json():
#     dct = {
#         'key1': None,
#         'key2': True
#     }
#     assert convert_json_to_str(dct) == {'key1': 'null', 'key2': 'true'}
