ADDED = "added"
REMOVED = "removed"
CHANGED = "changed"
UNCHANGED = "unchanged"
NESTED = "nested"


def get_diff(dict1, dict2):  # noqa C901
    dict_diff = {}
    all_keys = dict1.keys() | dict2.keys()
    all_keys_sort = sorted(all_keys)
    for i in all_keys_sort:
        if i in dict1 and i not in dict2:
            dict_diff[i] = (REMOVED, dict1[i])
        if i not in dict1 and i in dict2:
            dict_diff[i] = (ADDED, dict2[i])
        if i in dict1 and i in dict2 and dict1[i] == dict2[i]:
            dict_diff[i] = (UNCHANGED, dict1[i])
        if i in dict1 and i in dict2 and dict1[i] != dict2[i]:
            if (isinstance(dict1[i], dict) and isinstance(dict2[i], dict)):
                dict_diff[i] = (NESTED, dict(get_diff(dict1[i], dict2[i])))
            else:
                dict_diff[i] = (CHANGED, dict1[i], dict2[i])
    return dict_diff
