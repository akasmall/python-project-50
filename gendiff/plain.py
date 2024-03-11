# from gendiff.parser import ADDED, CHANGED, REMOVED, UNCHANGED

ADDED = "added"
REMOVED = "removed"
CHANGED = "changed"
NESTED = "nested"
UNCHANGED = "unchanged"


def get_bool_null_str(value_):
    if value_ == 'true' or value_ == 'false' or value_ == 'null':
        return value_
    else:
        return f"'{value_}'"


def line_for_changed(tiple_diff):
    if isinstance(tiple_diff[1], dict):
        res_bool_null = get_bool_null_str(tiple_diff[2])
        result = f" was updated. From [complex value] to {res_bool_null}"
        # result = f" was updated. From [complex value] to '{tiple_diff[2]}'"
    elif isinstance(tiple_diff[2], dict):
        res_bool_null = get_bool_null_str(tiple_diff[1])
        result = f" was updated. From {res_bool_null} to [complex value]"
        # result = f" was updated. From '{tiple_diff[1]}' to [complex value]"
    elif isinstance(tiple_diff[1], dict) \
            and isinstance(tiple_diff[2], dict):
        result = " was updated. From [complex value] to [complex value]"
    else:
        res_bool_null_1 = get_bool_null_str(tiple_diff[1])
        res_bool_null_2 = get_bool_null_str(tiple_diff[2])
        result = f" was updated. From {res_bool_null_1} to {res_bool_null_2}"
        # result = f" was updated. From '{tiple_diff[1]}' to " + \
        #     f"'{tiple_diff[2]}'"
    return result


def looking_conditions(tiple_diff):
    result = None
    if tiple_diff[0] == ADDED:
        if isinstance(tiple_diff[1], dict):
            result = " was added with value: [complex value]"
        else:
            res_bool_null = get_bool_null_str(tiple_diff[1])
            result = f" was added with value: {res_bool_null}"
            # result = f" was added with value: '{tiple_diff[1]}'"
    elif tiple_diff[0] == REMOVED:
        result = ' was removed'
    elif tiple_diff[0] == CHANGED:
        result = line_for_changed(tiple_diff)
    else:
        return result
    return result


def get_line_for_nested(*args):
    dict_diff, result, path, deep = args[0]
    if dict_diff[0] == 'nested':
        for key, value in dict_diff[1].items():
            result.extend(stringify_plain(
                # value, f"'{path}.{key}'", deep + 1))
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
