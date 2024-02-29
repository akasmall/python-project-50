# from gendiff.stylish import stringify

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


# def compare_dict(dict1, dict2):
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


# def parser_data(data1, data2):
#     dict_diff = compare_dict(data1, data2)
#     str_dict_diff = stringify(dict_diff)
#     return str_dict_diff

# added(новый),
# removed(удаленный),
# changed(измененный),
# unchanged(неизменный)
# nested(вложенный)

    # keys_union = set(dict1.keys()) ^ set(dict2.keys())
    # keys_compound = set(dict1.keys()) & set(dict2.keys())
    # dict_diff.update(add_union_keys(dict1, dict2, keys_union))
    # dict_diff.update(add_compound_keys(dict1, dict2, keys_compound))

    # for key_ in dict1:
    #     if key_ in dict2 and dict1[key_] != dict2[key_]:
    #         dict_diff[key_] = (
    #             CHANGED,
    #             format_bool_dict(dict1[key_]),
    #             format_bool_dict(dict2[key_])
    #         )
    #     elif key_ in dict1 and key_ not in dict2:
    #         dict_diff[key_] = (REMOVED, format_bool_dict(dict1[key_]))
    #     elif key_ in dict2 and dict1[key_] == dict2[key_]:
    #         dict_diff[key_] = (UNCHANGED, format_bool_dict(dict1[key_]))
    # for key_ in dict2:
    #     if key_ in dict2 and key_ not in dict1:
    #         dict_diff[key_] = (ADDED, format_bool_dict(dict2[key_]))
# def add_union_keys(dict1, dict2, keys_union):
#     new_dict = dict()
#     for key_ in keys_union:
#         if key_ in dict1 and key_ not in dict2:
#             new_dict[key_] = (REMOVED, format_bool_dict(dict1[key_]))
#         if key_ not in dict1 and key_ in dict2:
#             new_dict[key_] = (ADDED, format_bool_dict(dict2[key_]))
#     return new_dict


# def add_compound_keys(dict1, dict2, keys_compound):
#     new_dict = dict()
#     for key_ in keys_compound:
#         if dict1[key_] != dict2[key_]:
#             new_dict[key_] = (
#                 CHANGED,
#                 format_bool_dict(dict1[key_]),
#                 format_bool_dict(dict2[key_])
#             )
#         else:
#             new_dict[key_] = (UNCHANGED, format_bool_dict(dict1[key_]))
#     return new_dict

# def go_all_keys(dict1, dict2, all_keys):
#     dict_diff = {}
#     for key_ in all_keys:
#         if key_ in dict1 and key_ not in dict2:
#             dict_diff[key_] = (REMOVED, format_bool_dict(dict1[key_]))
#         if key_ not in dict1 and key_ in dict2:
#             dict_diff[key_] = (ADDED, format_bool_dict(dict2[key_]))
#         if key_ in dict1 and key_ in dict2 and dict1[key_] == dict2[key_]:
#             dict_diff[key_] = (UNCHANGED, format_bool_dict(dict1[key_]))
#         if key_ in dict1 and key_ in dict2 and dict1[key_] != dict2[key_]:
#             dict_diff[key_] = (CHANGED,
#                                format_bool_dict(dict1[key_]),
#                                format_bool_dict(dict2[key_])
#                                )
#     return dict_diff

# def format_bool_dict(data_dict):
#     if isinstance(data_dict, bool):
#         return str(data_dict).lower()
#     if data_dict is None:
#         return "null"
#     return data_dict
