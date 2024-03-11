from gendiff.parser import parser_data
from gendiff.loader import download_file
from gendiff.stylish import stringify_stylish
from gendiff.plain import stringify_plain


def generate_diff(file1, file2, formatter='stylish'):
    # для теста ++++
    # formatter = 'plain'
    # file1 = './tests/fixtures/file1.json'
    # file2 = './tests/fixtures/file2.json'
    # file1 = './tests/fixtures/file1.yml'
    # file2 = './tests/fixtures/file2.yml'
    # для теста ----

    file1_txt, file2_txt = download_file(file1, file2)
    dict_diff = parser_data(file1_txt, file2_txt)
    # print(dict_diff)
    if formatter == 'stylish':
        result = stringify_stylish(dict_diff)
        print(result)
    elif formatter == 'plain':
        result = stringify_plain(dict_diff)
        print(result)
    else:
        print("Неизвестный форматтер!!!")
        return False
    return result


# временно для теста
# generate_diff("file1", "file2")
