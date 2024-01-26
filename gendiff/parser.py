def build_diff(dict1, dict2, key_):
    result_str = ""
    if key_ in dict1 and key_ not in dict2:
        result_str = f"  - {key_}: {dict1[key_]}\n"
        return result_str
    if key_ in dict2 and key_ not in dict1:
        result_str = f"  + {key_}: {dict2[key_]}\n"
        return result_str
    if key_ in dict1 and key_ in dict2 and dict1[key_] == dict2[key_]:
        result_str = f"    {key_}: {dict1[key_]}\n"
        return result_str
    result_str = f"  - {key_}: {dict1[key_]}\n  + {key_}: {dict2[key_]}\n"
    return result_str


def compare_dict(dict1, dict2):
    keys_union = sorted(set(dict1.keys()) | set(dict2.keys()))
    res = "{\n"
    for i in keys_union:
        res += build_diff(dict1, dict2, i)
    res += "}"
    print(res)
    return res


def format_bool_dict(data_dict):
    new_file_txt = dict()
    for key_, value_ in data_dict.items():
        new_value_ = value_
        if isinstance(value_, bool):
            new_value_ = str(value_).lower()
        new_file_txt[key_] = new_value_
    return new_file_txt


def parser_data(data1, data2):
    format_data1 = format_bool_dict(data1)
    format_data2 = format_bool_dict(data2)
    dict_diff = compare_dict(format_data1, format_data2)
    return dict_diff
