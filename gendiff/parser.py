import os.path
import json
import yaml


def get_path_file(file):
    return os.path.abspath(file)


def parse(file):
    path = get_path_file(file)
    part, ext = os.path.splitext(file)
    if ext == '.json':
        return json.load(open(path))
    elif ext == '.yaml' or '.yml':
        return yaml.safe_load(open(path))
    else:
        return None
