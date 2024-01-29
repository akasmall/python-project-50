# def build_diff(dict1, dict2, key_):
#     result_str = ""
#     if key_ in dict1 and key_ not in dict2:
#         result_str = f"  - {key_}: {dict1[key_]}\n"
#         return result_str
#     if key_ in dict2 and key_ not in dict1:
#         result_str = f"  + {key_}: {dict2[key_]}\n"
#         return result_str
#     if key_ in dict1 and key_ in dict2 and dict1[key_] == dict2[key_]:
#         result_str = f"    {key_}: {dict1[key_]}\n"
#         return result_str
#     result_str = f"  - {key_}: {dict1[key_]}\n  + {key_}: {dict2[key_]}\n"
#     return result_str
def build_diff(dict_diff):
    # надо закончить
    return dict_diff


def format_bool_dict(data_dict):
    if isinstance(data_dict, bool):
        return str(data_dict).lower()
    return data_dict


def add_union_keys(dict1, dict2, keys_union):
    new_dict = dict()
    for key_ in keys_union:
        if key_ in dict1 and key_ not in dict2:
            new_dict[key_] = ("removed", format_bool_dict(dict1[key_]))
        if key_ not in dict1 and key_ in dict2:
            new_dict[key_] = ("added", format_bool_dict(dict2[key_]))
    return new_dict


def add_compound_keys(dict1, dict2, keys_compound):
    new_dict = dict()
    for key_ in keys_compound:
        if dict1[key_] != dict2[key_]:
            new_dict[key_] = (
                "changed",
                format_bool_dict(dict1[key_]),
                format_bool_dict(dict2[key_])
            )
        else:
            new_dict[key_] = ("unchanged", format_bool_dict(dict1[key_]))
    return new_dict


def compare_dict(dict1, dict2):
    dict_diff = dict()
    keys_union = set(dict1.keys()) ^ set(dict2.keys())
    keys_compound = set(dict1.keys()) & set(dict2.keys())
    dict_diff.update(add_union_keys(dict1, dict2, keys_union))
    dict_diff.update(add_compound_keys(dict1, dict2, keys_compound))
    # print({k: dict_diff[k] for k in sorted(dict_diff)})
    return {k: dict_diff[k] for k in sorted(dict_diff)}


def parser_data(data1, data2):
    format_data1 = format_bool_dict(data1)
    format_data2 = format_bool_dict(data2)
    dict_diff = compare_dict(format_data1, format_data2)
    print(dict_diff)
    str_dict_diff = build_diff(dict_diff)
    return str_dict_diff

# added(новый),
# removed(удаленный),
# changed(измененный),
# unchanged(неизменный)
