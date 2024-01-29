from gendiff.parser import parser_data
from gendiff.loader import download_file


def generate_diff(file1, file2):
    # для теста ++++
    file1 = './tests/fixtures/file1.json'
    file2 = './tests/fixtures/file2.json'
    # для теста ----

    file1_txt, file2_txt = download_file(file1, file2)
    return parser_data(file1_txt, file2_txt)


# временно для теста
generate_diff("file1", "file2")
