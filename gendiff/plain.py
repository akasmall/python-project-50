import json

ADDED = "added"
REMOVED = "removed"
CHANGED = "changed"
NESTED = "nested"
UNCHANGED = "unchanged"


# def custom_encoder(obj):
#     if isinstance(obj, bool):
#         return "true" if obj else "false"
#     elif isinstance(obj, (int, float)):
#         # elif isinstance(obj, (int, float, str)):
#         res = "'" + str(obj) + "'"
#         # res = "'" + str(obj) + "'"
#         return res
#     elif obj is None:
#         return "null"
#     raise TypeError(
#         f'Object of type {type(obj).__name__} is not JSON serializable')


def get_bool_null_str(value_):
    if isinstance(value_, bool) or value_ is None:
        result = json.dumps(value_)
    # elif isinstance(value_, (int, float)):
    else:
        result = json.dumps(str(value_))
        # result = value_
    return result


def line_for_changed(tiple_diff):
    if isinstance(tiple_diff[1], dict):
        # res_bool_null = json.dumps(tiple_diff[2], default=custom_encoder)
        res_bool_null = get_bool_null_str(tiple_diff[2])
        result = f' was updated. From [complex value] to {res_bool_null}'
    elif isinstance(tiple_diff[2], dict):
        # res_bool_null = json.dumps(tiple_diff[1], default=custom_encoder)
        res_bool_null = get_bool_null_str(tiple_diff[1])
        result = f' was updated. From {res_bool_null} to [complex value]'
    elif isinstance(tiple_diff[1], dict) \
            and isinstance(tiple_diff[2], dict):
        result = ' was updated. From [complex value] to [complex value]'
    else:
        # res_bool_null_1 = json.dumps(tiple_diff[1], default=custom_encoder)
        # res_bool_null_2 = json.dumps(tiple_diff[2], default=custom_encoder)
        res_bool_null_1 = get_bool_null_str(tiple_diff[1])
        res_bool_null_2 = get_bool_null_str(tiple_diff[2])
        result = f" was updated. From {res_bool_null_1} to {res_bool_null_2}"
    return result


def looking_conditions(tiple_diff):
    result = None
    if tiple_diff[0] == ADDED:
        if isinstance(tiple_diff[1], dict):
            result = ' was added with value: [complex value]'
        else:
            # res_bool_null = json.dumps(tiple_diff[1], default=custom_encoder)
            res_bool_null = get_bool_null_str(tiple_diff[1])
            result = f' was added with value: {res_bool_null}'
    elif tiple_diff[0] == REMOVED:
        result = ' was removed'
    elif tiple_diff[0] == CHANGED:
        result = line_for_changed(tiple_diff)
    else:
        return result
    return result


def get_line_for_nested(*args):
    dict_diff, result, path, deep = args[0]
    if dict_diff[0] == NESTED:
        for key, value in dict_diff[1].items():
            result.extend(stringify_plain(
                value, path + '.' + key, deep + 1))
    else:
        result_app = looking_conditions(dict_diff)
        if result_app is not None:
            path = f"Property '{path}'{result_app}"
            result.append(path)
        else:
            result = []
    return result


def stringify_plain(dict_diff, path='', deep=0):
    result = []
    if isinstance(dict_diff, tuple):
        list_value = dict_diff, result, path, deep
        result = get_line_for_nested(list_value)

    elif isinstance(dict_diff, dict):
        for key, value in dict_diff.items():
            if deep == 0:
                result.extend(stringify_plain(
                    value, path + key, deep + 1))
            else:
                result.extend(stringify_plain(
                    value, path + '.' + key, deep + 1))
    if deep == 0:
        return '\n'.join(result)
    else:
        return result
