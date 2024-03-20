import os
import json
import yaml


def none_constructor(loader, node):
    return loader.construct_scalar(node)


def bool_constructor(loader, node):
    return loader.construct_scalar(node)


def convert_json_to_str(dct):
    for key, value in dct.items():
        if value is None or isinstance(value, bool):
            dct[key] = json.dumps(value)
    return dct


def download_file(file1, file2):
    yaml.SafeLoader.add_constructor('tag:yaml.org,2002:null', none_constructor)
    yaml.SafeLoader.add_constructor('tag:yaml.org,2002:bool', bool_constructor)

    try:
        with (
            open(file1, "r", encoding="utf-8") as f1,
            open(file2, "r", encoding="utf-8") as f2,
        ):
            _, file_ext_1 = os.path.splitext(file1)
            _, file_ext_2 = os.path.splitext(file2)
            if file_ext_1 == ".json" and file_ext_2 == ".json":
                file1_txt = json.load(f1, object_hook=convert_json_to_str)
                file2_txt = json.load(f2, object_hook=convert_json_to_str)
            elif (file_ext_1 == ".yml" and file_ext_2 == ".yml") or \
                    (file_ext_1 == ".yaml" and file_ext_2 == ".yaml"):
                # file1_txt = yaml.safe_load(f1)
                file1_txt = yaml.safe_load(f1)
                file2_txt = yaml.safe_load(f2)
            else:
                raise Exception('Неподдерживаемый формат файла')
        return (file1_txt, file2_txt)
    except IOError as e:
        print('Не удалось открыть файл', e)


# def convert_json_to_str(dct):
#     for key, value in dct.items():
#         if value is None:
#             dct[key] = "null"
#         elif isinstance(value, bool):
#             dct[key] = str(value).lower()
#     return dct
