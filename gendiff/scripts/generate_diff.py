from gendiff.parse_json import parse_json
from gendiff.compare_dicts import compare


def generate_diff(path1, path2):
    try:
        d1 = parse_json(path1)
        d2 = parse_json(path2)
        result = compare(d1, d2)
        return result
    except FileNotFoundError:
        print("File not found")
