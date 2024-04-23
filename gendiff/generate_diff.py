import os
from gendiff.parser import parse
from gendiff.builder import get_diff
from gendiff.loader import receiving_data
from gendiff.formats.stylish import formatting_stylish
from gendiff.formats.plain import formatting_plain
from gendiff.formats.json_ import formatting_json

STYLISH = 'stylish'
F_PLAIN = 'plain'
F_JSON = 'json'


def generate_diff(data1, data2, formatter='stylish'):

    data1_txt = receiving_data(data1)
    data2_txt = receiving_data(data2)
    _, extension_with_dot = os.path.splitext(data1)
    extension = extension_with_dot[1:]
    parsed_data1 = parse(data1_txt, extension)
    parsed_data2 = parse(data2_txt, extension)
    dict_diff = get_diff(parsed_data1, parsed_data2)
    if formatter == STYLISH:
        result = formatting_stylish(dict_diff)
    elif formatter == F_PLAIN:
        result = formatting_plain(dict_diff)
    elif formatter == F_JSON:
        result = formatting_json(dict_diff)
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
