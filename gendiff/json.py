import json


def stringify_json(dict_diff):
    res = json.dumps(dict_diff, indent=4)
    return res
