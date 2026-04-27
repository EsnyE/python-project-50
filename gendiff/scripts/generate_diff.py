from typing import Dict

from gendiff.formatters.json import format_json
from gendiff.formatters.plain import format_plain
from gendiff.formatters.stylish import format_stylish
from gendiff.parser import parse_file


def build_ast(data1: Dict, data2: Dict) -> Dict:
    all_keys = sorted(set(data1.keys()) | set(data2.keys()))
    ast = {}
    
    for key in all_keys:
        if key not in data1:
            ast[key] = {'status': 'added', 'value': data2[key]}
        elif key not in data2:
            ast[key] = {'status': 'removed', 'value': data1[key]}
        elif data1[key] == data2[key]:
            ast[key] = {'status': 'unchanged', 'value': data1[key]}
        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            ast[key] = {
                'status': 'nested',
                'children': build_ast(data1[key], data2[key])
            }
        else:
            ast[key] = {
                'status': 'changed',
                'old_value': data1[key],
                'new_value': data2[key]
            }
    
    return ast


def generate_diff(
    file_path1: str, file_path2: str, format_name: str = 'stylish'
) -> str:
    data1 = parse_file(file_path1)
    data2 = parse_file(file_path2)
    ast = build_ast(data1, data2)
    
    if format_name == 'stylish':
        return format_stylish(ast)
    elif format_name == 'plain':
        return format_plain(ast)
    elif format_name == 'json':
        return format_json(ast)
    else:
        raise ValueError(f"Unknown format: {format_name}")