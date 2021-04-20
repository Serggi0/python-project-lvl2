import argparse


def create_parser_arg():
    parser_arg = argparse.ArgumentParser(description='Generate diff')
    parser_arg.add_argument('first_file')
    parser_arg.add_argument('second_file')
    parser_arg.add_argument('-f', '--format',
                            help='set format of output',
                            choices=['plain', 'stylish', 'json'],
                            default='stylish'
                            )
    return parser_arg
