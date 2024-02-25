from gendiff.parser import parser_data
from gendiff.loader import download_file


def generate_diff(file1, file2):
    # для теста ++++
    # file1 = './tests/fixtures/file1.json'
    # file2 = './tests/fixtures/file2.json'
    # file1 = './tests/fixtures/file1.yml'
    # file2 = './tests/fixtures/file2.yml'
    # для теста ----

    file1_txt, file2_txt = download_file(file1, file2)
    result = parser_data(file1_txt, file2_txt)
    return result


# временно для теста
# generate_diff("file1", "file2")
