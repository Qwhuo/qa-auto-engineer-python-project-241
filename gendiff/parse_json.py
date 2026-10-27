import json
from pathlib import Path


def parse_json(path):
    p = Path(path)
    if not p.is_absolute():
        p = p.cwd() / p
    json_data = json.load(open(p))
    return json_data