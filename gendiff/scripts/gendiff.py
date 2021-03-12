#!/usr/bin/env python
from gendiff.engine import generate_diff
from gendiff.engine import create_parser_arg


def main():
    parser_arg = create_parser_arg()
    args = parser_arg.parse_args()
    generate_diff(args.first_file, args.second_file)


if __name__ == '__main__':
    main()
