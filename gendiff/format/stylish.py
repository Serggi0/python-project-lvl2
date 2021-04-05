from gendiff.prefix import ADDED, CHANGED_FROM, CHANGED_TO, DELETED, SIMILAR, SUBDICTS

PREFIX = {
    ADDED: '+',
    CHANGED_FROM: '-',
    CHANGED_TO: '+',
    DELETED: '-',
    SIMILAR: ' ',
    # пробел при обинаковых ключах
    SUBDICTS: ' '
    # пробел перед whith subdicts, исключения: setting5, nest, group2, group3
    }


def make_stylish_line(diff):
    views = '\n'.join(form_views(diff)) #новая строка после обработки каждой строки, кроме упаковки блоков: setting5, nest, group2, group3
    return views.join(['{\n', '\n}'])


def form_views(tree, shift=2): # начальные 2 пробела
    lines = []
    calc_spaces = ' ' * shift


    for node in tree['children']:
        prefix = PREFIX[node['type']]
        # 2 начальных пробела + знак префикса + пробел между знаком префикса и ключом = 4 или (2 + знак префикса + пробел) -> для 1-го уровня
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
            # к каждой строке внутри подсловаря добавляются 2+2 начальных пробела +4 пробела на каждом круге
            lines.append(f'{calc_spaces}  }}') # 2 пробела перед закрывающейся скобкой +пробелы в зависимости от уровня вложенности
    return lines


def prepare_value(value, shift):
    if isinstance(value, dict):
        calc_spaces = ' ' * shift
        line = '\n'.join(prepare_rows(value, shift)) #новая строка после обработки каждой строки
        return f'{{\n{line}\n{calc_spaces}  }}' # + 2 пробела перед закрывающейся скобкой
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
        if isinstance(v, dict): # упаковка блоков
            lines.append(f'{calc_spaces}{k}: {{')
            lines.extend(prepare_rows(v, shift + 4))
            lines.append(f'{calc_spaces}}}')
        else:
            lines.append(f'{calc_spaces}{k}: {v}')
    return lines
