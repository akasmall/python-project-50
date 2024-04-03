import os
from gendiff.parser import parse
from gendiff.parser_ import parser_
from gendiff.loader import receiving_data
# from gendiff.loader import download_file
from gendiff.stylish import stringify_stylish
from gendiff.plain import stringify_plain
from gendiff.json import stringify_json

STYLISH = 'stylish'
F_PLAIN = 'plain'
F_JSON = 'json'

# def get_file_type(data_):
#     extension = os.path.splitext(data_)
#     return extension[1:]


def generate_diff(data1, data2, formatter='stylish'):

    data1_txt = receiving_data(data1)
    data2_txt = receiving_data(data2)
    _, extension_with_dot = os.path.splitext(data1)
    extension = extension_with_dot[1:]
    parsed_data1 = parse(data1_txt, extension)
    parsed_data2 = parse(data2_txt, extension)
    dict_diff = parser_(parsed_data1, parsed_data2)
    if formatter == STYLISH:
        result = stringify_stylish(dict_diff)
    elif formatter == F_PLAIN:
        result = stringify_plain(dict_diff)
    elif formatter == F_JSON:
        result = stringify_json(dict_diff)
    return result


# временно для теста
# для теста ++++
# FORMATTER_ = 'stylish'
# FORMATTER_ = 'plain'
# FORMATTER_ = 'json'
# DATA_1 = './tests/fixtures/file1.json'
# DATA_2 = './tests/fixtures/file2.json'
# DATA_1 = './tests/fixtures/file1.yml'
# DATA_2 = './tests/fixtures/file2.yml'
# res = generate_diff(DATA_1, DATA_2, FORMATTER_)
# print(res)
# для теста ----
