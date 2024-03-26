#!/usr/bin/env python3.10
# import argparse
from gendiff.cli import get_arguments_parsed
from gendiff.generate_diff import generate_diff


def main():
    # parser = argparse.ArgumentParser(
    #     description='Compares two configuration files
    # and shows a difference.')
    # parser.add_argument('first_file')
    # parser.add_argument('second_file')
    # parser.add_argument('-f', '--format',
    #                     default='stylish',
    #                     choices=['stylish', 'plain', 'json'],
    #                     help='set format of output')
    # args_ = parser.parse_args()

    args_ = get_arguments_parsed()
    print(
        generate_diff(
            args_.first_file,
            args_.second_file,
            formatter=args_.format
        )
    )

    # first_file = args_.first_file
    # second_file = args_.second_file

    # if args_.format:
    #     result = generate_diff(first_file, second_file, args_.format)
    # else:
    #     result = generate_diff(first_file, second_file)
    # if not result:
    #     print("Неизвестный форматтер!!!")
    # else:
    # print(result)


if __name__ == '__main__':
    main()
