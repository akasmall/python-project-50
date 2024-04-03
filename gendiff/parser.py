import json
import yaml

F_JSON = 'json'
F_YAML = ['yml', 'yaml']


def parse(data_txt, extension):
    if extension == F_JSON:
        text_in_format = json.loads(data_txt)
    if extension in F_YAML:
        text_in_format = yaml.safe_load(data_txt)
    return text_in_format
