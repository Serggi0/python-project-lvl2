#!/usr/bin/env python
from gendiff.differ import generate_diff
from gendiff.cli import create_parser_arg


def main():
    my_parser = create_parser_arg()
    args = my_parser.parse_args()
    print(generate_diff(args.first_file, args.second_file, args.format))


if __name__ == '__main__':
    main()
