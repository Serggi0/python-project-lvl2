import os.path
from gendiff.parser import parse
from gendiff.format.stylish import make_stylish_line
from gendiff.format.plain import make_plain
from gendiff.format.json import make_json_line
from gendiff.constants import (ADDED, CHANGED_FROM, CHANGED_TO,
                               DELETED, SIMILAR, SUBDICTS, ROOT)


def formatter(diff, format_name='stylish'):
    if format_name == 'stylish':
        return make_stylish_line(diff)
    elif format_name == 'plain':
        return make_plain(diff)
    elif format_name == 'json':
        return make_json_line(diff)


def read_file(path):
    path = os.path.abspath(path)
    data = open(path)
    return data


def get_format(path):
    part, ext = os.path.splitext(path)
    if ext == '.json':
        format = 'json'
    elif ext == '.yaml' or '.yml':
        format = 'yaml'
    else:
        print('This file extension is not parsed')
    return format


def generate_diff(file_path1, file_path2, format_name='stylish'):
    parsed_file1 = parse(read_file(file_path1), get_format(file_path1))
    parsed_file2 = parse(read_file(file_path2), get_format(file_path2))
    diff = make_diff_tree(parsed_file1, parsed_file2)
    return formatter(diff, format_name)


def make_diff_tree(file1, file2):
    return {
        'type': ROOT,
        'children': get_sorted_children(file1, file2)
    }


def get_keys(dictionary):
    return dictionary.keys()


def get_common_keys(file1, file2):
    return get_keys(file1) | get_keys(file2)


def get_sorted_children(file1: dict, file2: dict):
    children = []
    for elem in get_common_keys(file1, file2):
        if elem not in file1:
            children.append({
                'key': elem,
                'type': ADDED,
                'value': file2[elem]
            })
        elif elem not in file2:
            children.append({
                'key': elem,
                'type': DELETED,
                'value': file1[elem]
            })
        elif file1[elem] == file2[elem]:
            children.append({
                'key': elem,
                'type': SIMILAR,
                'value': file2[elem]
            })
        elif isinstance(file1[elem], dict) and isinstance(file2[elem], dict):
            children.append({
                'key': elem,
                'type': SUBDICTS,
                'children': get_sorted_children(file1[elem], file2[elem])
            })
        else:
            children.append({
                'key': elem,
                'type': CHANGED_FROM,
                'value': file1[elem]
            })
            children.append({
                'key': elem,
                'type': CHANGED_TO,
                'value': file2[elem]
            })
    return sorted(children, key=lambda x: x['key'])
