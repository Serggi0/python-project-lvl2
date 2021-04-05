from gendiff.prefix import (ADDED, CHANGED_FROM, CHANGED_TO,
                            DELETED, SIMILAR, SUBDICTS)

PREFIX = {
    ADDED: '+',
    CHANGED_FROM: '-',
    CHANGED_TO: '+',
    DELETED: '-',
    SIMILAR: ' ',
    SUBDICTS: ' '
}


def make_stylish_line(diff):
    views = '\n'.join(form_views(diff))
    return views.join(['{\n', '\n}'])


def form_views(tree, shift=2):  # noqa: C901
    lines = []
    calc_spaces = ' ' * shift

    for node in tree['children']:
        prefix = PREFIX[node['type']]
        if node['type'] == ADDED:
            lines.append(f'{calc_spaces}{prefix} {node["key"]}: '
                         f'{prepare_value(node["value"], shift)}')
        elif node['type'] == DELETED:
            lines.append(f'{calc_spaces}{prefix} {node["key"]}: '
                         f'{prepare_value(node["value"], shift)}')
        elif node['type'] == CHANGED_FROM:
            lines.append(f'{calc_spaces}{prefix} {node["key"]}: '
                         f'{prepare_value(node["value"], shift)}')
        elif node['type'] == CHANGED_TO:
            lines.append(f'{calc_spaces}{prefix} {node["key"]}: '
                         f'{prepare_value(node["value"], shift)}')
        elif node['type'] == SIMILAR:
            lines.append(f'{calc_spaces}{prefix} {node["key"]}: '
                         f'{prepare_value(node["value"], shift)}')
        elif node['type'] == SUBDICTS:
            lines.append(f'{calc_spaces}{prefix} {node["key"]}: {{')
            lines.extend(form_views(node, shift=shift + 4))
            lines.append(f'{calc_spaces}  }}')
    return lines


def prepare_value(value, shift):
    if isinstance(value, dict):
        calc_spaces = ' ' * shift
        line = '\n'.join(prepare_rows(value, shift))
        return f'{{\n{line}\n{calc_spaces}  }}'
    else:
        return change_value(value)


def change_value(value):
    if value is True:
        value = 'true'
    elif value is False:
        value = 'false'
    elif value is None:
        value = 'null'
    return f'{value}'


def prepare_rows(value, shift):
    calc_spaces = ' ' * (shift + 6)
    lines = []
    for k, v in value.items():
        if isinstance(v, dict):
            lines.append(f'{calc_spaces}{k}: {{')
            lines.extend(prepare_rows(v, shift + 4))
            lines.append(f'{calc_spaces}}}')
        else:
            lines.append(f'{calc_spaces}{k}: {v}')
    return lines
