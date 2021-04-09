import json


def make_json_line(diff):
    return json.dumps(diff, indent=4)
