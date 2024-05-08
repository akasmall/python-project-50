import json

ADDED = "added"
REMOVED = "removed"
CHANGED = "changed"
NESTED = "nested"
UNCHANGED = "unchanged"
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


def collect_lines(lines_list):
    new_list = [f"Property '{lines_list[i]}'" + lines_list[i + 1]
                for i in range(0, len(lines_list) - 1, 2)]
    return new_list


def add_parent(lines_list, parent_key):
    new_list = []
    for i in range(0, len(lines_list) - 1, 2):
        if parent_key != '':
            new_list.append(f"{parent_key}.{lines_list[i]}")
            new_list.append(lines_list[i + 1])
    return new_list


def convert_values(val_):
    if isinstance(val_, dict):
        return "[complex value]"
    if isinstance(val_, str):
        return f"'{val_}'"
    if isinstance(val_, bool) or val_ is None:
        return json.dumps(val_)
    return val_


def convert_vertice(val_):
    if val_[0] is ADDED:
        result_ver = convert_values(val_[1])
        return f" was added with value: {result_ver}"
    if val_[0] is REMOVED:
        result_ver = convert_values(val_[1])
        return " was removed"
    if val_[0] is UNCHANGED:
        result_ver = convert_values(val_[1])
        return None
    if val_[0] is CHANGED:
        result_val1 = convert_values(val_[1])
        result_val2 = convert_values(val_[2])
        return f" was updated. From {result_val1} to {result_val2}"
    return f'{result_ver}'


def format_plain(dict_diff, key_parent='', depth=0):  # noqa C901
    lines = []
    for key, val in dict_diff.items():
        result = ""
        if val[0] is NESTED:
            result = format_plain(val[1], key, depth + 1)
            if key_parent != '':
                lines += add_parent(result, key_parent)
            else:
                lines.append(result)
        else:
            result = convert_vertice(val)
            if result is None:
                continue
            if key_parent == '':
                lines.append([key, result])
            else:
                lines.append([f"{key_parent}.{key}", result])
        lines = flatten(lines)
    if depth == 0:
        lines = collect_lines(lines)
        lines = ("\n").join(lines)
    return lines
