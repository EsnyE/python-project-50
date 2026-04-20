import os
from gendiff import generate_diff


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