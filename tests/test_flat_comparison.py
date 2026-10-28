import pytest
from pathlib import Path

from gendiff.stylish_diff import form_stylish
from gendiff.plain_diff import form_plain
from gendiff.parse_files.parse_json import parse_json
from gendiff.parse_files.parse_yaml import parse_yaml
from gendiff.gather_difference import form_difference_dict
from gendiff.file_to_dict import to_dict

@pytest.fixture
def expected():
    p = Path(__file__).parent / "flat_expected.txt"
    with open(p, "r") as f:
        expected = f.read()
    return expected

@pytest.fixture
def expected_plain():
    p = Path(__file__).parent / "plain_expected.txt"
    with open(p, "r") as f:
        expected = f.read()
    return expected

def test_flat_dict_comparison(expected):
    d1 = {
      "host": "hexlet.io",
      "timeout": 50,
      "proxy": "123.234.53.22",
      "follow": 'false'
    }
    d2 = {
      "timeout": 20,
      "verbose": 'true',
      "host": "hexlet.io"
    }
    diff = form_difference_dict(d1, d2)
    assert expected == form_stylish(diff)

def test_flat_json_comparison(expected):
    p1 = Path(__file__).parent / "d1.json"
    p2 = Path(__file__).parent / "d2.json"
    d1 = parse_json(p1)
    d2 = parse_json(p2)
    diff = form_difference_dict(d1, d2)
    assert expected == form_stylish(diff)

def test_yaml_to_dict_convert():
    one_dict = {
      "host": "hexlet.io",
      "timeout": 50,
      "proxy": "123.234.53.22",
      "follow": False
    }
    p = Path(__file__).parent / "d1.yml"
    assert parse_yaml(p) == one_dict

def test_flat_yaml_comparison(expected):
    p1 = Path(__file__).parent / "d1.yml"
    p2 = Path(__file__).parent / "d2.yml"
    d1 = parse_yaml(p1)
    d2 = parse_yaml(p2)
    diff = form_difference_dict(d1, d2)
    assert expected == form_stylish(diff)

def test_diff_dict_generation():
    d1 = {
        "apple": 33,
        "banana": 12,
        "yoghurt": 3
    }
    d2 = {
        "apple": 33,
        "strawberry": 18,
        "yoghurt": 5
    }
    diff_exp = {
        "apple": [33, 33],
        "banana": [12, None],
        "strawberry": [None, 18],
        "yoghurt": [3, 5]
    }
    assert diff_exp == form_difference_dict(d1, d2)

def test_plain_json_comparison(expected_plain):
    p1 = Path(__file__).parent / "d1.json"
    p2 = Path(__file__).parent / "d2.yml"
    d1 = parse_yaml(p1)
    d2 = parse_yaml(p2)
    diff = form_difference_dict(d1, d2)
    assert expected_plain == form_plain(diff)

def test_file_to_dict_convert():
    expected = {
        "host": "hexlet.io",
        "timeout": 50,
        "proxy": "123.234.53.22",
        "follow": False
    }
    p_json = Path(__file__).parent / "d1.json"
    p_yml = Path(__file__).parent / "d1.yml"
    assert to_dict(p_json) == expected
    assert to_dict(p_yml) == expected