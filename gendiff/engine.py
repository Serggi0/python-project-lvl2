import argparse
from gendiff.parser import parse


SAVED = ' '
DELETED = '-'
ADDED = '+'


def change_value(file_dict):
    for k in file_dict:
        if file_dict[k] is True:
            file_dict[k] = 'true'
        if file_dict[k] is False:
            file_dict[k] = 'false'
        if file_dict[k] is None:
            file_dict[k] = 'null'
    return file_dict


def compare_files(file1, file2):
    file1 = change_value(file1)
    file2 = change_value(file2)
    keys_file1 = set(file1.keys())
    keys_file2 = set(file2.keys())
    result = []

    for elem in (keys_file1 & keys_file2):
        result.extend(compare_value(elem, file1[elem], file2[elem]))
    for elem in (keys_file1 - keys_file2):
        result.append((DELETED, elem, file1[elem]))
    for elem in (keys_file2 - keys_file1):
        result.append((ADDED, elem, file2[elem]))
    return result


def compare_value(key, value1, value2):
    result = ()
    if value1 == value2:
        result = ((SAVED, key, value2),)
    else:
        result = (DELETED, key, value1), (ADDED, key, value2)
    return result


# def sort_diff(data):
#     return sorted(data, key=lambda x: x[1])


def generate_diff(file1, file2):
    parsed_file1 = parse(file1)
    parsed_file2 = parse(file2)
    diff = compare_files(parsed_file1, parsed_file2)
    print(display_diff(diff))
    return display_diff(diff)


def display_diff(data):
    diff = sorted(data, key=lambda x: x[1])
    str_diff = '{'

    for elem in diff:
        str_diff += '\n{} {}: {}'.format(elem[0], elem[1], elem[2])
    str_diff += "\n}"
    return str_diff


def create_parser_arg():
    parser_arg = argparse.ArgumentParser(description='Generate diff')
    parser_arg.add_argument('first_file')
    parser_arg.add_argument('second_file')
    parser_arg.add_argument('-f', '--format', help='set format of output')
    return parser_arg
