import itertools

MINUS = "  - "
PLUS = "  + "
SPACE = "    "


def getting_padding(val):
    # if val[0] == "nested" or val[0] == "unchanged":
    if val[0] == "added":
        indent_ = PLUS
    elif val[0] == "removed":
        indent_ = MINUS
    else:
        indent_ = SPACE
    return indent_


def is_tuple(val):
    if not isinstance(val, tuple):
        if isinstance(val, dict):
            return True
        else:
            return False


def looking_conditions(iter_, *args):
    lines, key, val, deep_size, curr_indent = args[0]
    if not isinstance(val, tuple):
        if isinstance(val, dict):
            val = ("unchanged", val)
        else:
            deep_indent = curr_indent + SPACE
            lines.append(f'{deep_indent}{key}: {val}')
            return True
    if val[0] == "changed":
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


# if val[0] == "changed":
#     # deep_indent = curr_indent + MINUS
#     # lines.append(f'{deep_indent}{key}: {iter_(val[1], deep_size)}')
#     # deep_indent = curr_indent + PLUS
#     # lines.append(f'{deep_indent}{key}: {iter_(val[2], deep_size)}')
#     return [key, curr_indent + MINUS, curr_indent + PLUS]
# else:
#     return [key, curr_indent + getting_padding(val)]
#     # deep_indent = curr_indent + getting_padding(val)
#     # lines.append(f'{deep_indent}{key}: {iter_(val[1], deep_size)}')


def stringify(value, replacer=SPACE, spaces_count=1):

    def iter_(current_value, depth):
        if not isinstance(current_value, dict):
            return str(current_value)
        deep_size = depth + spaces_count
        curr_indent = replacer * depth
        lines = []
        for key, val in current_value.items():
            data_array = (lines, key, val, deep_size, curr_indent)
            looking_conditions(iter_, data_array)
        result = itertools.chain("{", lines, [curr_indent + "}"])
        return '\n'.join(result)
        # return lines

    return iter_(value, 0)


def build_str_diff(dict_diff):
    result_str = stringify(dict_diff)
    print(result_str)
    return result_str


# def stringify(value, replacer=SPACE, spaces_count=1):

#     def iter_(current_value, depth):
#         if not isinstance(current_value, dict):
#             return str(current_value)
#         deep_size = depth + spaces_count
#         curr_indent = replacer * depth
#         lines = []
#         for key, val in current_value.items():
#             if not isinstance(val, tuple):
#                 if isinstance(val, dict):
#                     val = ("unchanged", val)
#                 else:
#                     deep_indent = curr_indent + SPACE
#                     lines.append(f'{deep_indent}{key}: {val}')
#                     continue
#             if val[0] == "changed":
#                 deep_indent = curr_indent + MINUS
#                 lines.append(
#                     f'{deep_indent}{key}: {iter_(val[1], deep_size)}')
#                 deep_indent = curr_indent + PLUS
#                 lines.append(
#                     f'{deep_indent}{key}: {iter_(val[2], deep_size)}')
#             else:
#                 deep_indent = curr_indent + getting_padding(val)
#                 lines.append(
#                     f'{deep_indent}{key}: {iter_(val[1], deep_size)}')
#         result = itertools.chain("{", lines, [curr_indent + "}"])
#         return '\n'.join(result)
#         # return lines

#     return iter_(value, 0)
