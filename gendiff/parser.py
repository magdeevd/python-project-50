import json
import yaml
from pathlib import Path


def get_extension(filepath):
    file_path = Path(filepath)
    file_extension = file_path.suffix

    return file_extension


def parsefile(filepath):
    extension = get_extension(filepath)

    with open(filepath, 'r') as file:
        if extension == '.json':
            return json.load(file)
        elif extension in ('.yaml', '.yml'):
            return yaml.load(file, Loader=yaml.Loader)
