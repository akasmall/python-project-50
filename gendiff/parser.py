import json
import yaml

F_JSON = 'json'
F_YAML = 'yaml'
F_YML = 'yml'


def bring_str_type(data_dict, format_):
    for i in data_dict:
        if isinstance(data_dict[i], dict):
            _ = bring_str_type(data_dict[i], format_)
        if isinstance(data_dict[i], bool) or data_dict[i] is None:
            data_dict[i] = json.dumps(data_dict[i])
    return data_dict


def parse(data_txt, extension):
    if extension == F_JSON:
        text_in_format = bring_str_type(json.loads(data_txt), F_JSON)
    if extension == F_YML or extension == F_YAML:
        res = yaml.safe_load(data_txt)
        text_in_format = bring_str_type(res, F_YAML)
    return text_in_format
