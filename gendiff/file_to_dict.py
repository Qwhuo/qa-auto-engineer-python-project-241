from pathlib import Path

from gendiff.parse_files.parse_json import parse_json
from gendiff.parse_files.parse_yaml import parse_yaml


def to_dict(path):
    f = Path(path)
    if f.suffix == ".json":
        return parse_json(path)
    elif f.suffix == ".yaml" or f.suffix == ".yml":
        return parse_yaml(path)
    return None