import math
import pytest

from fhirpathpy import evaluate


@pytest.mark.parametrize(
    ("resource", "path", "expected"),
    [
        ({"a": 42}, "a + 2", [44]),
        ({"a": 42}, "a - 2", [40]),
        ({"a": 42}, "a * 2", [84]),
        ({"a": 42}, "a / 2", [21.0]),
        ({"a": 42}, "a mod 2", [0]),
        ({"a": 42}, "a div 2", [21]),
    ],
)
def infix_math_functions_test(resource, path, expected):
    assert evaluate(resource, path) == expected


"""
@pytest.mark.parametrize(("resource", "path", "expected"), [
    # or
    ({"a": True, "b": True}, "a or b", [True]),
    ({"a": True, "b": False}, "a or b", [True]),
    ({"a": False, "b": False}, "a or b", [False]),
    # and
    ({"a": True, "b": True}, "a and b", [True]),
    ({"a": True, "b": False}, "a and b", [False]),
    ({"a": False, "b": False}, "a and b", [False]),
    # xor
    ({"a": True, "b": True}, "a xor b", [False]),
    ({"a": True, "b": False}, "a xor b", [True]),
    ({"a": False, "b": False}, "a xor b", [False]),
    # implies
    ({"a": True, "b": True}, "a implies b", [True]),
    ({"a": True, "b": False}, "a implies b", [False]),
    ({"a": False, "b": False}, "a implies b", [True]),
])
def simple_logic_expressions_test(resource, path, expected):
    assert evaluate(resource, path) == expected
"""


@pytest.mark.parametrize(
    ("resource", "path", "expected"),
    [
        ({"a": -42}, "a.abs()", [42]),
        ({"a": 42.25}, "a.ceiling()", [43]),
        ({"a": 42.75}, "a.ceiling()", [43]),
        ({"a": 42.25}, "a.floor()", [42]),
        ({"a": 42.75}, "a.floor()", [42]),
        ({"a": 42.25}, "a.round(-1)", [40.0]),
        ({"a": 42.25}, "a.round(0)", [42]),
        ({"a": 42.25}, "a.round(1)", [42.2]),
        ({"a": 9}, "a.sqrt()", [3]),
        ({"a": 3}, "a.exp()", [math.exp(3)]),
        ({"a": 3}, "a.ln()", [math.log(3)]),
        ({"a": 3}, "a.log(3)", [math.log(3, 3)]),
        ({"a": 3}, "a.truncate()", [math.trunc(3)]),
    ],
)
def math_functions_test(resource, path, expected):
    assert evaluate(resource, path) == expected


@pytest.mark.parametrize(
    ("resource", "path", "expected"),
    [
        ({"a": "lorem ipsum"}, "a.indexOf('ipsum')", [6]),
        ({"a": "lorem ipsum"}, "a.substring(6, 2)", ["ip"]),
        ({"a": "lorem ipsum"}, "a.startsWith('lorem')", [True]),
        ({"a": "lorem ipsum"}, "a.endsWith('ipsum')", [True]),
        ({"a": "lorem ipsum"}, "a.contains('sum')", [True]),
        ({"a": "lorem ipsum"}, "a.replace('rem', 'l')", ["lol ipsum"]),
        ({"a": "lorem ipsum"}, "a.matches('l.+')", [True]),
        ({"a": "lorem ipsum"}, "a.matches('k.+')", [False]),
        ({"a": "lorem ipsum"}, "a.replaceMatches('lorem|ipsum', 'go')", ["go go"]),
        ({"a": "lorem ipsum"}, "a.length()", [11]),
    ],
)
def string_functions_test(resource, path, expected):
    assert evaluate(resource, path) == expected


"""
'select'
'ofType'
"""


@pytest.mark.parametrize(
    ("resource", "path", "expected"),
    [
        ({"list": []}, "list.single()", []),
        ({"list": [1]}, "list.single()", [1]),
        # ({"list": [1, 2]}, "list.single()", [1]),
        # ({"list": []}, "list.first()", [2]),
        ({"list": [2, 3]}, "list.first()", [2]),
        # ({"list": []}, "list.last()", [2]),
        ({"list": [2, 3]}, "list.last()", [3]),
        ({"list": [1, 2, 3, 4]}, "list.tail()", [2, 3, 4]),
        ({"list": [1, 2, 3, 4]}, "list.take(2)", [1, 2]),
        ({"list": [1, 2, 3, 4]}, "list.skip(2)", [3, 4]),
        ({"list": [1.0, 2.0, 3.0, 4.0]}, "list.where($this <= 2.0)", [1, 2]),
        # ({"list": [{"a": 1}, {"a": 2}, {"a": 3}, {"a": 4}]}, "list.select(a)", [1, 2, 3, 4]),
    ],
)
def filtering_functions_test(resource, path, expected):
    assert evaluate(resource, path) == expected


@pytest.mark.parametrize(
    ("resource", "path", "expected"),
    [({"a": 42.0}, "a > 40", [True]), ({"a": 42.0}, "a < 40", [False]),],
)
def equality_functions_test(resource, path, expected):
    assert evaluate(resource, path) == expected
