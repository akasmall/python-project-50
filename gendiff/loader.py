import os
import json
import yaml


def download_file(file1, file2):
    try:
        with (
            open(file1, "r", encoding="utf-8") as f1,
            open(file2, "r", encoding="utf-8") as f2,
        ):
            # type_file1 = os.path.splitext(file1)[1]
            # type_file2 = os.path.splitext(file2)[1]
            _, file_ext_1 = os.path.splitext(file1)
            _, file_ext_2 = os.path.splitext(file2)
            if file_ext_1 == ".json" and file_ext_2 == ".json":
                file1_txt = json.load(f1)
                file2_txt = json.load(f2)
            elif (file_ext_1 == ".yml" and file_ext_2 == ".yml") or \
                    (file_ext_1 == ".yaml" and file_ext_2 == ".yaml"):
                file1_txt = yaml.safe_load(f1)
                file2_txt = yaml.safe_load(f2)
            else:
                raise Exception('Неподдерживаемый формат файла')
        return (file1_txt, file2_txt)
    except IOError as e:
        print('Не удалось открыть файл', e)
