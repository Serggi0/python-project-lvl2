import json
import yaml


def parse(data, format):
    if format == 'json':
        return json.load(data)
    elif format == 'yaml':
        return yaml.safe_load(data)
