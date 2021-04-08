from gendiff.format.stylish import change_value
from gendiff.prefix import (ADDED, CHANGED_FROM, CHANGED_TO,
                            DELETED, SIMILAR, SUBDICTS)

STATUS = {
    ADDED: 'added',
    CHANGED_FROM: 'updated',
    CHANGED_TO: 'to',
    DELETED: 'removed',
    SIMILAR: 'no change',
    SUBDICTS: ' '
}


def make_plain(diff):
    views = form_views(diff)
    return ''.join(views).rstrip()


def form_views(tree, child_name=''):
    lines = []
    for node in tree['children']:
        path = child_name + node['key']
        if node['type'] == SUBDICTS:
            lines.extend(form_views(node, f'{path}.'))
        elif node['type'] == SIMILAR:
            continue
        else:
            lines.append(prepare_node(node, path))
    return lines


def prepare_node(node, path):
    status = STATUS[node['type']]
    line1 = ''
    if node['type'] == DELETED:
        line1 = '\n'
    elif node["type"] == ADDED:
        line1 = f' with value: {prepare_value(node["value"])}\n'
    elif node['type'] == CHANGED_FROM:
        line1 = f'. From {prepare_value(node["value"])} to '
    elif node['type'] == CHANGED_TO:
        string = f'{prepare_value(node["value"])}\n'
        return string
    line2 = f'Property \'{path}\' was {status}{line1}'
    return line2


def prepare_value(value):
    if isinstance(value, dict):
        return '[complex value]'
    elif isinstance(value, str):
        return f'\'{value}\''
    else:
        return change_value(value)
