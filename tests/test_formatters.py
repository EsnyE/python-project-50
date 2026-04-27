from gendiff.formatters import json, plain, stylish
from gendiff.formatters.stylish import format_stylish, format_value


def test_formatters_import():
    assert stylish is not None
    assert plain is not None
    assert json is not None


def test_format_value_nested_dict():
    value = {'key': 'value', 'nested': {'a': 1}}
    result = format_value(value, 1)
    assert 'key' in result
    assert 'nested' in result


def test_format_value_list():
    value = [1, 2, 3]
    result = format_value(value, 1)
    assert '[1, 2, 3]' in result


def test_format_stylish_with_nested_lists():
    diff = {
        'items': {
            'status': 'added',
            'value': [1, 2, 3]
        }
    }
    result = format_stylish(diff)
    assert 'items' in result
    assert '1, 2, 3' in result


def test_format_stylish_empty_nested():
    diff = {
        'empty': {
            'status': 'nested',
            'children': {}
        }
    }
    result = format_stylish(diff)
    assert 'empty' in result
