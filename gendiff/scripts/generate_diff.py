from gendiff.file_to_dict import to_dict
from gendiff.gather_difference import form_difference_dict
from gendiff.formatters.stylish_diff import form_stylish
from gendiff.formatters.plain_diff import form_plain
from gendiff.formatters.json_diff import form_json


def generate_diff(path1, path2, format="stylish"):
    formats = {
        "stylish": form_stylish,
        "plain": form_plain,
        "json": form_json,
    }
    d1 = to_dict(path1)
    d2 = to_dict(path2)
    if d1 is None or d2 is None:
        raise FileNotFoundError("Something went wrong")
    diff = form_difference_dict(d1, d2)
    result = formats[format](diff)
    return result
