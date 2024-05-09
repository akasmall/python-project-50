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
    new_list = []
    for line_ in lines_list:
        new_list.append(f"Property '{line_[0]}'{line_[1]}")
    return new_list


def add_parent(lines_list, parent_key):
    new_list = []
    for line_ in lines_list:
        new_list.append((f"{parent_key}.{line_[0]}", line_[1]))
    return new_list


def convert_values(val_):
    if isinstance(val_, dict):
        return "[complex value]"
    if isinstance(val_, str):
        return f"'{val_}'"
    if isinstance(val_, bool) or val_ is None:
        return json.dumps(val_)
    return val_


def convert_vertice(val_, depth_):
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
    if val_[0] is NESTED:
        res_ = format_plain(val_[1], depth_ + 1)
        return res_
    return f'{result_ver}'


def format_plain(dict_diff, depth=0):
    lines = []
    for key, val in dict_diff.items():
        result = convert_vertice(val, depth)
        if result is None:
            continue
        if isinstance(result, list):
            result = add_parent(result, key)
            lines.append(result)
            lines = flatten(lines)
        else:
            lines.append((key, result))
    if depth == 0:
        lines = collect_lines(lines)
        lines = ("\n").join(lines)
    return lines
