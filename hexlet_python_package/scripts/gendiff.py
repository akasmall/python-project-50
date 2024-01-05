#!/usr/bin/env python3.10
import argparse
import json
import os
import sys


def compare_dict(dict1, dict2):
    dict_diff = {
        key_: (dict1[key_], "", "-") for key_ in dict1 if key_ not in dict2
    }
    dict_diff.update({
        key_: (dict2[key_], "", "+") for key_ in dict2 if key_ not in dict1
    })
    for key_ in dict1:
        if key_ in dict2 and dict1[key_] == dict2[key_]:
            dict_diff.update({key_: (dict1[key_], "", None)})
            continue
        elif key_ not in dict2:
            continue
        else:
            dict_diff.update({key_: (dict1[key_], dict2[key_], "$")})
    return dict(sorted(dict_diff.items()))


def print_dict(dict_diff_):
    print("{")
    for key_, value_ in dict_diff_.items():

        if value_[2] == "-":
            print(f"  - {key_}: {value_[0]}")
        elif value_[2] == "+":
            print(f"  + {key_}: {value_[0]}")
        elif value_[2] == "$":
            print(f"  - {key_}: {value_[0]}")
            print(f"  + {key_}: {value_[1]}")
        else:
            print(f"    {key_}: {value_[0]}")
    print("}")


def generate_diff(file1, file2):
    with (
        open(file1, "r", encoding="utf-8") as f1,
        open(file2, "r", encoding="utf-8") as f2,
    ):
        file1 = json.load(f1)
        file2 = json.load(f2)
    dict_diff = compare_dict(file1, file2)
    print_dict(dict_diff)


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format',
                        help='set format of output')
    parser.parse_args()

    file_args = sys.argv
    full_path = os.getcwd()
    file1 = f"{full_path}/{file_args[1]}"
    file2 = f"{full_path}/{file_args[2]}"
    generate_diff(file1, file2)


if __name__ == '__main__':
    main()
