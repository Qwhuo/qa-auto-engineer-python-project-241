import yaml
from pathlib import Path

def parse_yaml(path) -> dict:
    p = Path(path)
    if not p.is_absolute():
        p = p.cwd() / path
    with open(p, "r", encoding="utf-8") as f:
        yaml_data = yaml.safe_load(f)
    return yaml_data