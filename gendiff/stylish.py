import itertools
import json

ADDED = "added"
REMOVED = "removed"
CHANGED = "changed"
UNCHANGED = "unchanged"
MINUS = "  - "
PLUS = "  + "
SPACE = "    "


def getting_padding(val):
    if val[0] == ADDED:
        indent_ = PLUS
    elif val[0] == REMOVED:
        indent_ = MINUS
    else:
        indent_ = SPACE
    return indent_


def looking_conditions(iter_, *args):
    lines, key, val, deep_size, curr_indent = args[0]
    if not isinstance(val, tuple):
        if isinstance(val, dict):
            val = (UNCHANGED, val)
        else:
            deep_indent = curr_indent + SPACE
            lines.append(f'{deep_indent}{key}: {val}')
            return True
    if val[0] == CHANGED:
        deep_indent = curr_indent + MINUS
        lines.append(
            f'{deep_indent}{key}: {iter_(val[1], deep_size)}')
        deep_indent = curr_indent + PLUS
        lines.append(
            f'{deep_indent}{key}: {iter_(val[2], deep_size)}')
    else:
        deep_indent = curr_indent + getting_padding(val)
        lines.append(
            f'{deep_indent}{key}: {iter_(val[1], deep_size)}')
    return False


def stringify_stylish(dict_diff, replacer=SPACE, spaces_count=1):

    def iter_(current_value, depth):
        if not isinstance(current_value, dict):
            if isinstance(current_value, bool) or current_value is None:
                processed_value = json.dumps(current_value)
            else:
                processed_value = current_value
            return processed_value
            # return str(current_value)
        deep_size = depth + spaces_count
        curr_indent = replacer * depth
        lines = []
        for key, val in current_value.items():
            data_array = (lines, key, val, deep_size, curr_indent)
            looking_conditions(iter_, data_array)
        result = itertools.chain("{", lines, [curr_indent + "}"])
        return '\n'.join(result)

    return iter_(dict_diff, 0)
