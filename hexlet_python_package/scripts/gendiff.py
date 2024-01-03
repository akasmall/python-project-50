#!/usr/bin/env python3.10
import argparse


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format',
                        help='set format of output')

    parser.parse_args()
    # args = parser.parse_args()
    # print(args.accumulate(args.integers))


if __name__ == '__main__':
    main()
