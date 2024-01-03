#!/usr/bin/env python3.10
import argparse


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    # parser.add_argument(prog='gendiff', metavar='first_file', type=str)
    # parser.add_argument(metavar='second_file', type=str)
    # parser.add_argument(dest='accumulate',
    #                     help='show this help message and exit')

    parser.parse_args()
    # args = parser.parse_args()
    # print(args.accumulate(args.integers))


if __name__ == '__main__':
    main()
