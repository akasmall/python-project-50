from gendiff.parser import parser_data
from gendiff.loader import download_file
from gendiff.stylish import stringify_stylish
from gendiff.plain import stringify_plain
from gendiff.json import stringify_json


def generate_diff(data1, data2, formatter='stylish'):
    data1_txt = download_file(data1)
    data2_txt = download_file(data2)
    dict_diff = parser_data(data1_txt, data2_txt)
    if formatter == 'stylish':
        result = stringify_stylish(dict_diff)
    elif formatter == 'plain':
        result = stringify_plain(dict_diff)
    elif formatter == 'json':
        result = stringify_json(dict_diff)
    # else:
    #     # return 'Неизвестный формат!!!'
    #     raise ValueError(f"{formatter} - неизвестный формат!")
    return result


# # временно для теста
# # для теста ++++
# FORMATTER_ = 'stylish'
# # FORMATTER_ = 'plain'
# # FORMATTER_ = 'json'
# data_1 = './tests/fixtures/data1.json'
# data_2 = './tests/fixtures/data2.json'
# # data1 = './tests/fixtures/data1.yml'
# # data2 = './tests/fixtures/data2.yml'
# # для теста ----
# generate_diff(data_1, data_2, FORMATTER_)
