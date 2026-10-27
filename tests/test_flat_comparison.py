import pytest
from pathlib import Path

from gendiff.compare_dicts import compare
from gendiff.parse_json import parse_json

@pytest.fixture
def expected():
    p = Path("/Users/Q/PycharmProjects/qa-auto-engineer-python-project-241/tests/flat_expected.txt")
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
    assert expected == compare(d1, d2)

def test_flat_json_comparison(expected):
    p1 = Path("/Users/Q/PycharmProjects/qa-auto-engineer-python-project-241/tests/d1.json")
    p2 = Path("/Users/Q/PycharmProjects/qa-auto-engineer-python-project-241/tests/d2.json")
    d1 = parse_json(p1)
    d2 = parse_json(p2)
    assert expected == compare(d1, d2)
