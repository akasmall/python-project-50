import os
import json
import yaml
from gendiff.parser import parser_data


# def get_diff(file1, file2):
def generate_diff(file1, file2):
    # для теста ++++
    file1 = './tests/fixtures/file1.json'
    file2 = './tests/fixtures/file2.json'
    # для теста ----
    with (
        open(file1, "r", encoding="utf-8") as f1,
        open(file2, "r", encoding="utf-8") as f2,
    ):
        type_file1 = os.path.splitext(file1)[1]
        type_file2 = os.path.splitext(file2)[1]
        if type_file1 == ".json" and type_file2 == ".json":
            file1_txt = json.load(f1)
            file2_txt = json.load(f2)
            # file2_txt = json.dumps(json.load(f2), indent=2)
        elif (type_file1 == ".yml" and type_file2 == ".yml") or \
                (type_file1 == ".yaml" and type_file2 == ".yaml"):
            file1_txt = yaml.safe_load(f1)
            file2_txt = yaml.safe_load(f2)
        else:
            return False
    return parser_data(file1_txt, file2_txt)


# временно для теста
generate_diff("file1", "file2")
# get_diff("file1", "file2")
