#!/usr/bin/env python3.10
import argparse
from gendiff.generate_diff import generate_diff


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format',
                        help='set format of output')
    args_ = parser.parse_args()

    first_file = args_.first_file
    second_file = args_.second_file

    if args_.format:
        generate_diff(first_file, second_file, args_.format)
    else:
        generate_diff(first_file, second_file)


if __name__ == '__main__':
    main()
