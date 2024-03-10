# import itertools
# from gendiff.parser import ADDED, CHANGED, REMOVED, UNCHANGED

ADDED = "added"
REMOVED = "removed"
CHANGED = "changed"
NESTED = "nested"
UNCHANGED = "unchanged"


# def getting_padding(val):
#     if val[0] == ADDED:
#         indent_ = PLUS
#     elif val[0] == REMOVED:
#         indent_ = MINUS
#     else:
#         indent_ = SPACE
#     return indent_

# if current_value[0] == NESTED:
#     iter_(current_value[1])
# elif not isinstance(current_value[0], tuple):
#     pass
# elif current_value[0] == UNCHANGED:
#     continue
# else:

# def looking_conditions(iter_, *args):
#     lines, key, val, deep, value_from, value_to = args[0]
#     result = None
#     if val[0] == NESTED:
#         lines.append(iter_(val[1], deep + 1))
#     elif val[0] == ADDED:
#         result = f' was added with value: {val[1]}'
#     elif val[0] == REMOVED:
#         result = ' was removed'
#     elif val[0] == CHANGED:
#         result = f' was updated. From {val[1]} to {val[2]}'
#     else:
#         return result
#     return result

def looking_conditions(tiple_diff):
    result = None
    if tiple_diff[0] == ADDED:
        if isinstance(tiple_diff[1], dict):
            result = " was added with value: [complex value]"
        else:
            result = f" was added with value: '{tiple_diff[1]}'"
    elif tiple_diff[0] == REMOVED:
        result = ' was removed'
    elif tiple_diff[0] == CHANGED:
        if isinstance(tiple_diff[1], dict):
            result = f" was updated. From [complex value] to '{tiple_diff[2]}'"
        elif isinstance(tiple_diff[2], dict):
            result = f" was updated. From '{tiple_diff[1]}' to [complex value]"
        elif isinstance(tiple_diff[1], dict) \
                and isinstance(tiple_diff[2], dict):
            result = " was updated. From [complex value] to [complex value]"
        else:
            result = f" was updated. From '{tiple_diff[1]}' to " + \
                f"'{tiple_diff[2]}'"
    else:
        return result
    return result


def stringify_plain(dict_diff, path='', deep=0):
    result = []
    if isinstance(dict_diff, tuple):
        if dict_diff[0] == 'nested':
            for key, value in dict_diff[1].items():
                result.extend(stringify_plain(
                    # value, f"'{path}.{key}'", deep + 1))
                    value, path + '.' + key, deep + 1))
        else:
            result_app = looking_conditions(dict_diff)
            # is_value_none()
            if result_app is not None:
                path = f"Property '{path}'{result_app}"
                # path = f'{path}{result_app}'
                result.append(path)
            else:
                result = []
    elif isinstance(dict_diff, dict):
        for key, value in dict_diff.items():
            if deep == 0:
                result.extend(stringify_plain(
                    # value, f"'{path}{key}'", deep + 1))
                    value, path + key, deep + 1))
            else:
                result.extend(stringify_plain(
                    # value, f"'{path}.{key}'", deep + 1))
                    value, path + '.' + key, deep + 1))
    # result.append = result[len(result) - 1][1:]
    # print(result)
    if deep == 0:
        return '\n'.join(result)
    else:
        return result


# def get_leaf_paths(data, path=''):
#     result = []
#     if isinstance(data, tuple):
#         if data[0] == 'nested':
#             for key, value in data[1].items():
#                 result.extend(get_leaf_paths(value, path + '/' + key))
#         else:
#             result.append(path)
#     elif isinstance(data, dict):
#         for key, value in data.items():
#             result.extend(get_leaf_paths(value, path + '/' + key))
#     return result


# leaf_paths = get_leaf_paths(data)
# for path in leaf_paths:
#     if 'nested' not in path:
#         print(path)
