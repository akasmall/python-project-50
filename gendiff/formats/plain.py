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


def converting_values(val_):
    if isinstance(val_, dict):
        return "[complex value]"
    if isinstance(val_, str):
        return f"'{val_}'"
    if isinstance(val_, bool) or val_ is None:
        return json.dumps(val_)
    return val_


# def converting_vertice(key_, val_):
def converting_vertice(val_):
    # depth_values = depth + 1
    if val_[0] is ADDED:
        result_ver = converting_values(val_[1])
        return f" was added with value: {result_ver}"
    if val_[0] is REMOVED:
        result_ver = converting_values(val_[1])
        return " was removed"
    if val_[0] is UNCHANGED:
        result_ver = converting_values(val_[1])
        return None
    if val_[0] is CHANGED:
        result_1 = converting_values(val_[1])
        result_2 = converting_values(val_[2])
        return f" was updated. From {result_1} to {result_2}"
    return f'{result_ver}'


def collect_lines(lines_list):
    new_list = [f"Property '{lines_list[i]}'" + lines_list[i + 1]
                for i in range(0, len(lines_list) - 1, 2)]
    return new_list


def add_parent(lines_list, parent):
    new_list = []
    for i in range(0, len(lines_list) - 1, 2):
        if parent != '':
            new_list.append(f"{parent}.{lines_list[i]}")
            new_list.append(lines_list[i + 1])
    return new_list


def formatting_plain(dict_diff, depth_key='', depth=0):
    lines = []
    for key, val in dict_diff.items():
        result = ""
        if val[0] is NESTED:
            result = formatting_plain(val[1], key, depth + 1)
            if depth_key != '':
                lines += add_parent(result, depth_key)
            else:
                lines.append(result)
        else:
            result = converting_vertice(val)
            # result = converting_vertice(key, val)
            if result is None:
                continue
            if depth_key == '':
                lines.append([key, result])
            else:
                lines.append([f"{depth_key}.{key}", result])
        lines = flatten(lines)

    if depth == 0:
        lines = collect_lines(lines)
        lines = ("\n").join(lines)
    return lines


# DATA = {
#     'common': ('nested', {
#         'follow': ('added', False),
#         'setting1': ('unchanged', 'Value 1'),
#         'setting2': ('removed', 200),
#         'setting3': ('changed', True, None),
#         'setting4': ('added', 'blah blah'),
#         'setting5': ('added', {'key5': 'value5'}),
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
#         'nest': ('changed', {
#             'key': 'value'
#         },
#             'str')
#     }),
#     'group2': ('removed', {
#         'abc': 12345,
#         'deep': {
#             'id': 45
#         }
#     }),
#     'group3': ('added', {
#         'deep': {
#             'id': {
#                 'number': 45
#             }
#         },
#         'fee': 100500
#     })
# }
# res = formatting_plain(DATA)
# print(res)

# {
#     'group1': ('nested', {
#         'baz': ('changed', 'bas', 'bars'),
#         'foo': ('unchanged', 'bar'),
#         'nest': ('changed', {
#             'key': 'value'
#         },
#             'str')
#     }),
#     'group2': ('removed', {
#         'abc': 12345,
#         'deep': {
#             'id': 45
#         }
#     }),
#     'group3': ('added', {
#         'fee': 100500
#     })
# }


# def get_bool_null_str(value_):
#     if isinstance(value_, bool) or value_ is None:
#         result = json.dumps(value_)
#     elif isinstance(value_, (int, float)):
#         result = f"{str(value_)}"
#     else:
#         result = f"\'{value_}\'"
#     return result


# def get_change_str(tiple_diff):
#     if isinstance(tiple_diff[1], dict):
#         res_bool_null = get_bool_null_str(tiple_diff[2])
#         result = f' was updated. From [complex value] to {res_bool_null}'
#     elif isinstance(tiple_diff[2], dict):
#         res_bool_null = get_bool_null_str(tiple_diff[1])
#         result = f' was updated. From {res_bool_null} to [complex value]'
#     elif isinstance(tiple_diff[1], dict) \
#             and isinstance(tiple_diff[2], dict):
#         result = ' was updated. From [complex value] to [complex value]'
#     else:
#         res_bool_null_1 = get_bool_null_str(tiple_diff[1])
#         res_bool_null_2 = get_bool_null_str(tiple_diff[2])
#         result = f" was updated. From {res_bool_null_1} to {res_bool_null_2}"
#     return result


# def looking_conditions(tiple_diff):
#     result = None
#     if tiple_diff[0] == ADDED:
#         if isinstance(tiple_diff[1], dict):
#             result = ' was added with value: [complex value]'
#         else:
#             res_bool_null = get_bool_null_str(tiple_diff[1])
#             result = f' was added with value: {res_bool_null}'
#     elif tiple_diff[0] == REMOVED:
#         result = ' was removed'
#     elif tiple_diff[0] == CHANGED:
#         result = get_change_str(tiple_diff)
#     else:
#         return result
#     return result


# def get_nested_str(*args):
#     dict_diff, result, path, deep = args[0]
#     if dict_diff[0] == NESTED:
#         for key, value in dict_diff[1].items():
#             result.extend(formatting_plain(value, f"{path}.{key}", deep + 1))
#     else:
#         result_app = looking_conditions(dict_diff)
#         if result_app is not None:
#             path = f"Property \'{path}\'{result_app}"
#             result.append(path)
#         else:
#             result = []
#     return result


# def formatting_plain(dict_diff, path='', deep=0):
#     result = []
#     if isinstance(dict_diff, tuple):
#         list_value = dict_diff, result, path, deep
#         result = get_nested_str(list_value)

#     elif isinstance(dict_diff, dict):
#         for key, value in dict_diff.items():
#             if deep == 0:
#                 result.extend(formatting_plain(value, path + key, deep + 1))
#             else:
#                 result.extend(formatting_plain(
#                     value, path + '.' + key, deep + 1))
#     if deep == 0:
#         return '\n'.join(result)
#     else:
#         return result
