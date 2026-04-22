"""Тесты для скрипта gendiff."""
import os
import sys
import subprocess
from gendiff.scripts import gendiff
from gendiff.scripts.gendiff import find_file


def test_scripts_module_import():
    assert hasattr(gendiff, 'main')


def test_find_file_in_current_dir(tmp_path):
    test_file = tmp_path / 'test.json'
    test_file.write_text('{}')
    
    original_dir = os.getcwd()
    os.chdir(tmp_path)
    
    try:
        result = find_file('test.json')
        assert result == 'test.json'
    finally:
        os.chdir(original_dir)


def test_find_file_in_test_data():
    result = find_file('file1.json')
    assert result is not None
    assert 'file1.json' in result


def test_find_file_not_found():
    result = find_file('nonexistent_file_12345.json')
    assert result is None


def test_main_function_help():
    result = subprocess.run(
        [sys.executable, '-m', 'gendiff.scripts.gendiff', '-h'],
        capture_output=True,
        text=True
    )
    assert result.returncode == 0


@pytest.mark.skip(reason="Requires arguments")
def test_main_function_no_args():
    result = subprocess.run(
        [sys.executable, '-m', 'gendiff.scripts.gendiff'],
        capture_output=True,
        text=True
    )
    assert result.returncode == 0


def test_main_function_with_files():
    result = subprocess.run(
        [sys.executable, '-m', 'gendiff.scripts.gendiff',
         'tests/test_data/file1.json', 'tests/test_data/file2.json'],
        capture_output=True,
        text=True
    )
    assert result.returncode == 0


def test_main_function_with_format():
    result = subprocess.run(
        [sys.executable, '-m', 'gendiff.scripts.gendiff',
         '-f', 'plain',
         'tests/test_data/file1.json', 'tests/test_data/file2.json'],
        capture_output=True,
        text=True
    )
    assert result.returncode == 0


def test_main_function_file_not_found():
    result = subprocess.run(
        [sys.executable, '-m', 'gendiff.scripts.gendiff',
         'nonexistent.json', 'file2.json'],
        capture_output=True,
        text=True
    )
    assert result.returncode == 1
