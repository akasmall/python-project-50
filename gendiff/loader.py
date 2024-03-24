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


def download_file(file):
    yaml.SafeLoader.add_constructor('tag:yaml.org,2002:null', none_constructor)
    yaml.SafeLoader.add_constructor('tag:yaml.org,2002:bool', bool_constructor)

    try:
        with (
            open(file, "r", encoding="utf-8") as f,
        ):
            _, file_ext = os.path.splitext(file)
            if file_ext == ".json":
                file_txt = json.load(f, object_hook=convert_json_to_str)
            elif (file_ext == ".yml") or (file_ext == ".yaml"):
                file_txt = yaml.safe_load(f)
            else:
                raise Exception('Неподдерживаемый формат файла')
        return file_txt
    except IOError as e:
        print('Не удалось открыть файл', e)
