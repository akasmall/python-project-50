# Сначала определите фикстуру в файле, например, в файле conftest.py:
import os
import pytest
# import yaml
from gendiff.scripts.gendiff import generate_diff


# def get

@pytest.mark.parametrize(
    "file1, file2, file3",
    [
        (
            f"{os.getcwd()}/tests/fixtures/file1.json",
            f"{os.getcwd()}/tests/fixtures/file2.json",
            f"{os.getcwd()}/tests/fixtures/diff_f1_f2.txt",
        ),
        (
            f"{os.getcwd()}/tests/fixtures/file1.yml",
            f"{os.getcwd()}/tests/fixtures/file2.yml",
            f"{os.getcwd()}/tests/fixtures/diff_f1_f2.txt",
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
