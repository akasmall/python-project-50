def build_str_diff(dict_diff):
    str_diff = "{\n"
    for key_ in dict_diff:
        if dict_diff[key_][0] == 'removed':
            str_diff += f"  - {key_}: {dict_diff[key_][1]}\n"
        elif dict_diff[key_][0] == 'unchanged':
            str_diff += f"    {key_}: {dict_diff[key_][1]}\n"
        elif dict_diff[key_][0] == 'added':
            str_diff += f"  + {key_}: {dict_diff[key_][1]}\n"
        elif dict_diff[key_][0] == 'changed':
            str_diff += f"  - {key_}: {dict_diff[key_][1]}\n"
            str_diff += f"  + {key_}: {dict_diff[key_][2]}\n"
    str_diff += "}"
    print(str_diff)
    return str_diff
