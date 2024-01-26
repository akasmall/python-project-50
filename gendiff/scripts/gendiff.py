#!/usr/bin/env python3.10
import sys
import argparse
from gendiff.generate_diff import generate_diff
# from gendiff.generate_diff import get_diff


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format',
                        help='set format of output')
    parser.parse_args()

    # get_diff(sys.argv[1], sys.argv[2])
    generate_diff(sys.argv[1], sys.argv[2])


if __name__ == '__main__':
    main()
