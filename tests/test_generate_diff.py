import os
import pytest
from gendiff import generate_diff
from gendiff.formatters.stylish import format_stylish
from gendiff.formatters.plain import format_plain
from gendiff.formatters.json import format_json
import json


def get_fixture_path(filename):

    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, 'test_data', filename)


def read_fixture(filename):

    with open(get_fixture_path(filename), 'r', encoding='utf-8') as f:
        return f.read()


def test_generate_diff_json_stylish():

    file1 = get_fixture_path('file1.json')
    file2 = get_fixture_path('file2.json')
    
    expected = read_fixture('expected_stylish.txt')
    result = generate_diff(file1, file2, 'stylish')
    
    assert result == expected


def test_generate_diff_yaml_stylish():

    file1 = get_fixture_path('file1.yml')
    file2 = get_fixture_path('file2.yml')
    
    expected = read_fixture('expected_stylish.txt')
    result = generate_diff(file1, file2, 'stylish')
    
    assert result == expected


def test_generate_diff_default_formatter():

    file1 = get_fixture_path('file1.json')
    file2 = get_fixture_path('file2.json')
    
    expected = read_fixture('expected_stylish.txt')
    result = generate_diff(file1, file2)
    
    assert result == expected


def test_generate_diff_flat_json():

    file1 = get_fixture_path('flat1.json')
    file2 = get_fixture_path('flat2.json')
    
    result = generate_diff(file1, file2)
    
    assert '  - follow: false' in result
    assert '    host: hexlet.io' in result
    assert '  + verbose: true' in result


def test_generate_diff_identical_files():

    file1 = get_fixture_path('file1.json')
    
    result = generate_diff(file1, file1)
    
    assert '  - ' not in result
    assert '  + ' not in result


def test_generate_diff_mixed_formats():

    json_file = get_fixture_path('file1.json')
    yaml_file = get_fixture_path('file2.yml')
    
    expected = read_fixture('expected_stylish.txt')
    result = generate_diff(json_file, yaml_file)
    
    assert result == expected

# Покрытие

def test_format_stylish_empty():
    diff = {}
    result = format_stylish(diff)
    assert result == '{\n}'


def test_format_stylish_nested():
    diff = {
        'common': {
            'status': 'nested',
            'children': {
                'key': {'status': 'unchanged', 'value': 'value'}
            }
        }
    }
    result = format_stylish(diff)
    assert 'common' in result
    assert 'key' in result


def test_format_stylish_boolean():
    diff = {
        'flag': {'status': 'added', 'value': True}
    }
    result = format_stylish(diff)
    assert 'true' in result


def test_format_stylish_null():
    diff = {
        'value': {'status': 'added', 'value': None}
    }
    result = format_stylish(diff)
    assert 'null' in result


def test_format_plain_added(): 
    diff = {
        'key': {'status': 'added', 'value': 'value'}
    }
    result = format_plain(diff)
    assert "Property 'key' was added with value: 'value'" in result


def test_format_plain_removed():
    diff = {
        'key': {'status': 'removed'}
    }
    result = format_plain(diff)
    assert "Property 'key' was removed" in result


def test_format_plain_changed():
    diff = {
        'key': {
            'status': 'changed',
            'old_value': 'old',
            'new_value': 'new'
        }
    }
    result = format_plain(diff)
    assert "was updated" in result


def test_format_plain_nested():
    diff = {
        'parent': {
            'status': 'nested',
            'children': {
                'child': {'status': 'added', 'value': 'value'}
            }
        }
    }
    result = format_plain(diff)
    assert "parent.child" in result


def test_format_plain_complex_value():
    diff = {
        'dict': {'status': 'added', 'value': {'a': 1}}
    }
    result = format_plain(diff)
    assert '[complex value]' in result


def test_format_json():
    diff = {'key': {'status': 'added', 'value': 'value'}}
    result = format_json(diff)
    parsed = json.loads(result)
    assert 'key' in parsed


def test_generate_diff_plain_format():
    file1 = get_fixture_path('file1.json')
    file2 = get_fixture_path('file2.json')
    result = generate_diff(file1, file2, 'plain')
    assert isinstance(result, str)
    assert len(result) > 0


def test_generate_diff_json_format():
    file1 = get_fixture_path('file1.json')
    file2 = get_fixture_path('file2.json')
    result = generate_diff(file1, file2, 'json')
    parsed = json.loads(result)
    assert isinstance(parsed, dict)


def test_generate_diff_unknown_format():
    with pytest.raises(ValueError):
        generate_diff('file1.json', 'file2.json', 'unknown')


def test_import():
    __import__('gendiff')
    __import__('gendiff.parser')
    __import__('gendiff.formatters.stylish')
    assert True
