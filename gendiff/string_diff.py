import itertools

MINUS = "  - "
PLUS = "  + "
SPACE = "    "
# INDENT = "  "


# def stringify(value, replacer=' ', spaces_count=1):

#     def iter_(current_value, depth):
#         if not isinstance(current_value, dict):
#             return str(current_value)

#         deep_indent_size = depth + spaces_count
#         deep_indent = replacer * deep_indent_size
#         current_indent = replacer * depth
#         lines = []
#         for key, val in current_value.items():
#            lines.append(f'{deep_indent}{key}: {iter_(val, deep_indent_size)}')
#         result = itertools.chain("{", lines, [current_indent + "}"])
#         return '\n'.join(result)

#     return iter_(value, 0)

def getting_padding(val):
    # if val[0] == "nested" or val[0] == "unchanged":
    if val[0] == "added":
        indent_ = PLUS
    elif val[0] == "removed":
        indent_ = MINUS
    else:
        indent_ = SPACE
    return indent_


def stringify(value, replacer=SPACE, spaces_count=1):

    def iter_(current_value, depth):
        if not isinstance(current_value, dict):
            return str(current_value)
        deep_indent_size = depth + spaces_count
        current_indent = replacer * depth
        lines = []
        for key, val in current_value.items():
            if not isinstance(val, tuple):
                deep_indent = current_indent + SPACE
                lines.append(f'{deep_indent}{key}: {val}')
                continue
            if val[0] == "changed":
                deep_indent = current_indent + MINUS
                lines.append(
                    f'{deep_indent}{key}: {iter_(val[1], deep_indent_size)}')
                deep_indent = current_indent + PLUS
                lines.append(
                    f'{deep_indent}{key}: {iter_(val[2], deep_indent_size)}')
            else:
                deep_indent = current_indent + getting_padding(val)
                lines.append(
                    f'{deep_indent}{key}: {iter_(val[1], deep_indent_size)}')
        result = itertools.chain("{", lines, [current_indent + "}"])
        return '\n'.join(result)
        # return lines

    return iter_(value, 0)


# def collecting_str(text):
#     txt_str = ""
#     return txt_str


def build_str_diff(dict_diff):
    # result_str = "{\n" + SPACE
    # for i in dict_diff:
    #     result_str = stringify(dict_diff[i]) + "\n"
    # return result_str + "}"
    result_str = stringify(dict_diff)
    print(result_str)
    return result_str


# def build_str_diff(dict_diff):
#     str_diff = "{\n"
#     for key_ in dict_diff:
#         if dict_diff[key_][0] == 'removed':
#             str_diff += f"  - {key_}: {dict_diff[key_][1]}\n"
#         elif dict_diff[key_][0] == 'unchanged':
#             str_diff += f"    {key_}: {dict_diff[key_][1]}\n"
#         elif dict_diff[key_][0] == 'added':
#             str_diff += f"  + {key_}: {dict_diff[key_][1]}\n"
#         elif dict_diff[key_][0] == 'changed':
#             str_diff += f"  - {key_}: {dict_diff[key_][1]}\n"
#             str_diff += f"  + {key_}: {dict_diff[key_][2]}\n"
#     str_diff += "}"
#     print(str_diff)
#     return str_diff
