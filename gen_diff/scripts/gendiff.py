#!/usr/bin/env python3.10
import os
import sys
import argparse
import json
import yaml
from gen_diff.parser import format_values_dict, compare_dict

# def build_differ(dict1, dict2, key_):
#     result_str = ""
#     if key_ in dict1 and key_ not in dict2:
#         result_str = f"  - {key_}: {dict1[key_]}\n"
#         return result_str
#     if key_ in dict2 and key_ not in dict1:
#         result_str = f"  + {key_}: {dict2[key_]}\n"
#         return result_str
#     if key_ in dict1 and key_ in dict2 and dict1[key_] == dict2[key_]:
#         result_str = f"    {key_}: {dict1[key_]}\n"
#         return result_str
#     result_str = f"  - {key_}: {dict1[key_]}\n  + {key_}: {dict2[key_]}\n"
#     return result_str


# def compare_dict(dict1, dict2):
#     keys_union = sorted(set(dict1.keys()) | set(dict2.keys()))
#     res = "{\n"
#     for i in keys_union:
#         res += build_differ(dict1, dict2, i)
#     res += "}"
#     print(res)
#     return res


# def format_values_dict(file_txt):
#     new_file_txt = dict()
#     for key_, value_ in file_txt.items():
#         new_value_ = value_
#         if isinstance(value_, bool):
#             new_value_ = str(value_).lower()
#         new_file_txt[key_] = new_value_
#     return new_file_txt


def generate_diff(file1, file2):
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
    format_file1_txt = format_values_dict(file1_txt)
    format_file2_txt = format_values_dict(file2_txt)
    dict_diff = compare_dict(format_file1_txt, format_file2_txt)
    return dict_diff


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format',
                        help='set format of output')
    parser.parse_args()

    file_args = sys.argv
    # full_path = os.path.dirname(file_args[0])
    # print(full_path)
    file1 = file_args[1]
    # file1 = f"{full_path}/{file_args[1]}"
    # print(file1)
    file2 = file_args[2]
    # file2 = f"{full_path}/{file_args[2]}"
    # print(file2)
    generate_diff(file1, file2)


if __name__ == '__main__':
    main()
