import os
from gendiff.parser import parse
from gendiff.builder import get_diff
from gendiff.loader import receive_data
from gendiff.formats.stylish import format_stylish
from gendiff.formats.plain import format_plain
from gendiff.formats.json_ import format_json

STYLISH = 'stylish'
F_PLAIN = 'plain'
F_JSON = 'json'


def generate_diff(data1, data2, formatter='stylish'):

    data1_txt = receive_data(data1)
    data2_txt = receive_data(data2)
    _, extension_with_dot = os.path.splitext(data1)
    extension = extension_with_dot[1:]
    parsed_data1 = parse(data1_txt, extension)
    parsed_data2 = parse(data2_txt, extension)
    dict_diff = get_diff(parsed_data1, parsed_data2)
    if formatter == STYLISH:
        result = format_stylish(dict_diff)
    elif formatter == F_PLAIN:
        result = format_plain(dict_diff)
    elif formatter == F_JSON:
        result = format_json(dict_diff)
    return result
