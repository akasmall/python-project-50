from gendiff.parser import parser_data
from gendiff.loader import download_file
from gendiff.stylish import stringify_stylish
from gendiff.plain import stringify_plain
from gendiff.json import stringify_json


def generate_diff(file1, file2, formatter='stylish'):
    file1_txt = download_file(file1)
    file2_txt = download_file(file2)
    dict_diff = parser_data(file1_txt, file2_txt)
    if formatter == 'stylish':
        result = stringify_stylish(dict_diff)
    elif formatter == 'plain':
        result = stringify_plain(dict_diff)
    elif formatter == 'json':
        result = stringify_json(dict_diff)
    # else:
    #     return 'Неизвестный форматтер!!!'
        # raise ValueError('Неизвестный форматтер!!!')
    return result


# # временно для теста
# # для теста ++++
# FORMATTER_ = 'stylish'
# # FORMATTER_ = 'plain'
# # FORMATTER_ = 'json'
# FILE_1 = './tests/fixtures/file1.json'
# FILE_2 = './tests/fixtures/file2.json'
# # file1 = './tests/fixtures/file1.yml'
# # file2 = './tests/fixtures/file2.yml'
# # для теста ----
# generate_diff(FILE_1, FILE_2, FORMATTER_)
