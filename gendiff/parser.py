def build_differ(dict1, dict2, key_):
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
        res += build_differ(dict1, dict2, i)
    res += "}"
    print(res)
    return res


def format_values_dict(file_txt):
    new_file_txt = dict()
    for key_, value_ in file_txt.items():
        new_value_ = value_
        if isinstance(value_, bool):
            new_value_ = str(value_).lower()
        new_file_txt[key_] = new_value_
    return new_file_txt
