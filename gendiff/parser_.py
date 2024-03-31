ADDED = "added"
REMOVED = "removed"
CHANGED = "changed"
UNCHANGED = "unchanged"
NESTED = "nested"


def go_all_keys(dict1, dict2, all_keys):
    dict_diff = {}
    for key_ in all_keys:
        if key_ in dict1 and key_ not in dict2:
            dict_diff[key_] = (REMOVED, dict1[key_])
        if key_ not in dict1 and key_ in dict2:
            dict_diff[key_] = (ADDED, dict2[key_])
        if key_ in dict1 and key_ in dict2 and dict1[key_] == dict2[key_]:
            dict_diff[key_] = (UNCHANGED, dict1[key_])
        if key_ in dict1 and key_ in dict2 and dict1[key_] != dict2[key_]:
            dict_diff[key_] = (CHANGED, dict1[key_], dict2[key_])
    return dict_diff


def parser_data(dict1, dict2):
    dict_diff = {}
    all_keys = dict1.keys() | dict2.keys()
    dict_diff = go_all_keys(dict1, dict2, all_keys)

    dict_diff = {k: dict_diff[k] for k in sorted(dict_diff)}
    res_diff = {}
    for i in dict_diff:
        if (dict_diff[i][0] == CHANGED
                and isinstance(dict_diff[i][1], dict)
                and isinstance(dict_diff[i][2], dict)):
            res_diff[i] = (NESTED, dict(parser_data(
                dict_diff[i][1],
                dict_diff[i][2]
            )))
        else:
            res_diff[i] = dict_diff[i]
    return res_diff
