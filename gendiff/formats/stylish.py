# import itertools
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
            lines_dict.append(f'{SPACE*depth}{key}: {result_val}' + '\n')
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
            # result.insert(0, SPACE + SPACE * depth + key + ': {\n')
            result.insert(0, SPACE + SPACE * depth + key + ': {')
            # result.append(SPACE + SPACE * depth + '}')
            # result.append('\n' + SPACE + SPACE * depth + '}')
            result.append(SPACE + SPACE * depth + '}')
            # plug = 1
        else:
            result = converting_vertice(key, val, depth)
        lines.append(result)
        lines = flatten(lines)
    if depth == 0:
        lines = "{\n" + ("\n").join(lines) + "\n}"
    return lines


def looking_conditions():
    pass


# DATA_DIFF = {
#     'group1': ('nested', {
#         'baz': ('changed', 'bas', 'bars'),
#         'foo': ('unchanged', 'bar'),
#         'nest': ('changed', {'key': 'value'}, 'str')
#     }),
#     'follow': ('removed', False),
#     'nest': ('changed', {'key1': 'value1', 'key2': 'value2'}, 'str'),
#     'host': ('unchanged', 'hexlet.io'),
#     'proxy': ('removed', '123.234.53.22'),
#     'timeout': ('changed', 50, 20),
#     'verbose': ('added', True)
# }

# DATA_DIFF = {
#     'common': ('nested', {
#         'follow': ('added', False),
#         'setting1': ('unchanged', 'Value 1'),
#         'setting2': ('removed', 200),
#         'setting3': ('changed', True, None),
#         'setting4': ('added', 'blah blah'),
#         'setting5': ('added', {
#             'key5': 'value5'
#         }),
#         'setting6': ('nested', {
#             'doge': ('nested', {
#                 'wow': ('changed', '', 'so much')
#             }),
#             'key': ('unchanged', 'value'),
#             'ops': ('added', 'vops')
#         })
#     }),
#     'group1': ('nested', {
#         'baz': ('changed', 'bas', 'bars'),
#         'foo': ('unchanged', 'bar'),
#         'nest': ('changed', {'key': 'value'}, 'str')
#     }),
#     'group2': ('removed', {
#         'abc': 12345,
#         'deep': {
#             'id': 45
#         }
#     }),
#     'group3': ('added', {
#         'deep': {'id': {
#             'number': 45}
#         },
#         'fee': 100500
#     })
# }

# res = formatting_stylish(DATA_DIFF)
# # noqaC901
# print(res)

# ADDED = "added"
# REMOVED = "removed"
# CHANGED = "changed"
# UNCHANGED = "unchanged"
# MINUS = "  - "
# PLUS = "  + "
# SPACE = "    "


# def getting_padding(val):
#     if val[0] == ADDED:
#         indent_ = PLUS
#     elif val[0] == REMOVED:
#         indent_ = MINUS
#     else:
#         indent_ = SPACE
#     return indent_


# def looking_conditions(iter_, *args):
#     lines, key, val, deep_size, curr_indent = args[0]
#     if not isinstance(val, tuple):
#         if isinstance(val, dict):
#             val = (UNCHANGED, val)
#         else:
#             deep_indent = curr_indent + SPACE
#             lines.append(f'{deep_indent}{key}: {val}')
#             return True
#     if val[0] == CHANGED:
#         deep_indent = curr_indent + MINUS
#         lines.append(
#             f'{deep_indent}{key}: {iter_(val[1], deep_size)}')
#         deep_indent = curr_indent + PLUS
#         lines.append(
#             f'{deep_indent}{key}: {iter_(val[2], deep_size)}')
#     else:
#         deep_indent = curr_indent + getting_padding(val)
#         lines.append(
#             f'{deep_indent}{key}: {iter_(val[1], deep_size)}')
#     return False


# def formatting_stylish(dict_diff, replacer=SPACE, spaces_count=1):

#     def iter_(val_, depth):
#         if not isinstance(val_, dict):
#             if isinstance(val_, bool) or val_ is None:
#                 processed_value = json.dumps(val_)
#             else:
#                 processed_value = val_
#             return processed_value
#             # return str(val_)
#         deep_size = depth + spaces_count
#         curr_indent = replacer * depth
#         lines = []
#         for key, val in val_.items():
#             data_array = (lines, key, val, deep_size, curr_indent)
#             looking_conditions(iter_, data_array)
#         result = itertools.chain("{", lines, [curr_indent + "}"])
#         return '\n'.join(result)

#     return iter_(dict_diff, 0)
