#!/usr/bin/env python3.10
from gendiff.cli import get_arguments_parsed
from gendiff.generate_diff import generate_diff


def main():

    args_ = get_arguments_parsed()
    print(
        generate_diff(
            args_.first_file,
            args_.second_file,
            formatter=args_.format
        )
    )


if __name__ == '__main__':
    main()
