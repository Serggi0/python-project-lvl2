import argparse
from gendiff.format.stylish import make_stylish_line
from gendiff.format.plain import make_plain


def create_parser_arg():
    parser_arg = argparse.ArgumentParser(description='Generate diff')
    parser_arg.add_argument('first_file')
    parser_arg.add_argument('second_file')
    parser_arg.add_argument('-f', '--format',
                            help='set format of output',
                            choices=['plain', 'stylish'],
                            default='stylish'
                            )
    return parser_arg


def formatter(diff, format_name='stylish'):
    if format_name == 'stylish':
        return make_stylish_line(diff)
    if format_name == 'plain':
        return make_plain(diff)