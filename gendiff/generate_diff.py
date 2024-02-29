from gendiff.parser import parser_data
from gendiff.loader import download_file
from gendiff.stylish import stringify


def generate_diff(file1, file2, formatter='stylish'):
    # для теста ++++
    # file1 = './tests/fixtures/file1.json'
    # file2 = './tests/fixtures/file2.json'
    # file1 = './tests/fixtures/file1.yml'
    # file2 = './tests/fixtures/file2.yml'
    # для теста ----

    file1_txt, file2_txt = download_file(file1, file2)
    dict_diff = parser_data(file1_txt, file2_txt)
    if formatter != 'stylish':
        print("Неизвестный форматтер!!!")
        return False
    else:
        result = stringify(dict_diff)
        print(result)
        return result


# временно для теста
# generate_diff("file1", "file2")
