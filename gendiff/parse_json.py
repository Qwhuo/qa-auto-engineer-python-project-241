import json
from pathlib import Path


def parse_json(path):
    p = Path(path)
    if not p.is_absolute():
        p = p.cwd() / p
    with p.open() as f:
        json_data = json.load(f)
    return json_data