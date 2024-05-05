import json


ADDED = "added"
REMOVED = "removed"
CHANGED = "changed"
UNCHANGED = "unchanged"
NESTED = "nested"
MINUS = "  - "
PLUS = "  + "
SPACE = "    "


def flatten(tree):
    res_fl = []

    def walk(subtree):
        for item in subtree:
            if isinstance(item, list):
                walk(item)
            else:
                res_fl.append(item)
    walk(tree)
    return res_fl


def converting_values(val_, depth):
    result_val = ''
    if isinstance(val_, dict):
        lines_dict = []
        for key, val in val_.items():
            result_val = converting_values(val, depth + 1)
            lines_dict.append(f'{SPACE * depth}{key}: {result_val}' + '\n')
        return '{\n' + ("").join(lines_dict) + (SPACE * (depth - 1)) + '}'
    if isinstance(val_, bool) or val_ is None:
        return json.dumps(val_)
    return val_


def converting_vertice(key_, val_, depth):
    depth_values = depth + 1
    if val_[0] is ADDED:
        result_ver = converting_values(val_[1], depth_values + 1)
        return f'{SPACE * depth}{PLUS}{key_}: {result_ver}'
    if val_[0] is REMOVED:
        result_ver = converting_values(val_[1], depth_values + 1)
        return f'{SPACE * depth}{MINUS}{key_}: {result_ver}'
    if val_[0] is UNCHANGED:
        result_ver = converting_values(val_[1], depth_values + 1)
        return f'{SPACE * depth}{SPACE}{key_}: {result_ver}'
    if val_[0] is CHANGED:
        result_1 = converting_values(val_[1], depth_values + 1)
        result_2 = converting_values(val_[2], depth_values + 1)
        return f'{SPACE * depth}{MINUS}{key_}: {result_1}\n'\
            f'{SPACE * depth}{PLUS}{key_}: {result_2}'
    return f'{SPACE * depth}{result_ver}'


def formatting_stylish(dict_diff, depth=0):
    lines = []
    for key, val in dict_diff.items():
        result = ""
        if val[0] is NESTED:
            result = formatting_stylish(val[1], depth + 1)
            result.insert(0, SPACE + SPACE * depth + key + ': {')
            result.append(SPACE + SPACE * depth + '}')
        else:
            result = converting_vertice(key, val, depth)
        lines.append(result)
        lines = flatten(lines)
    if depth == 0:
        lines = "{\n" + ("\n").join(lines) + "\n}"
    return lines
