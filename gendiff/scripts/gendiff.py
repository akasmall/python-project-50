#!/usr/bin/env python3.10
import os
import sys
import argparse
import json
import yaml
from gendiff.parser import format_values_dict, compare_dict


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
    file1 = file_args[1]
    file2 = file_args[2]
    generate_diff(file1, file2)


if __name__ == '__main__':
    main()
