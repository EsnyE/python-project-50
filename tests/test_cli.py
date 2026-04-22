import os
import sys
import pytest
from unittest.mock import patch, MagicMock
from gendiff import cli
from gendiff.cli import parse_args
from gendiff.cli import main
from gendiff.generate_diff import generate_diff

def test_cli_module_import():
    assert hasattr(cli, 'main')


def test_parse_args():
    test_args = ['gendiff', 'file1.json', 'file2.json']
    with patch('sys.argv', test_args):
        args = parse_args()
        assert args.first_file == 'file1.json'
        assert args.second_file == 'file2.json'
        assert args.format == 'stylish'


def test_parse_args_with_format():
    test_args = ['gendiff', '-f', 'plain', 'file1.json', 'file2.json']
    with patch('sys.argv', test_args):
        args = parse_args()
        assert args.first_file == 'file1.json'
        assert args.second_file == 'file2.json'
        assert args.format == 'plain'


def test_main_function_stylish():
    test_args = ['gendiff', 'file1.json', 'file2.json']
    with patch('sys.argv', test_args):
        with patch('gendiff.cli.generate_diff') as mock_generate:
            mock_generate.return_value = 'diff output'
            with patch('builtins.print') as mock_print:
                result = main()
                mock_generate.assert_called_once_with(
                    'file1.json', 'file2.json', 'stylish'
                )
                mock_print.assert_called_once_with('diff output')
                assert result == 0


def test_main_function_plain():
    test_args = ['gendiff', '-f', 'plain', 'file1.json', 'file2.json']
    with patch('sys.argv', test_args):
        with patch('gendiff.cli.generate_diff') as mock_generate:
            mock_generate.return_value = 'plain diff'
            with patch('builtins.print') as mock_print:
                result = main()
                mock_generate.assert_called_once_with(
                    'file1.json', 'file2.json', 'plain'
                )
                mock_print.assert_called_once_with('plain diff')
                assert result == 0


def test_main_function_file_not_found():
    test_args = ['gendiff', 'nonexistent.json', 'file2.json']
    with patch('sys.argv', test_args):
        result = main()
        assert result == 1


def test_main_function_exception():
    test_args = ['gendiff', 'file1.json', 'file2.json']
    with patch('sys.argv', test_args):
        with patch('gendiff.cli.generate_diff') as mock_generate:
            mock_generate.side_effect = Exception('Test error')
            with patch('builtins.print') as mock_print:
                result = main()
                mock_print.assert_called_once()
                assert result == 1
