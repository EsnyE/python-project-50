import os
from typing import Any, Dict, List
from gendiff.parser import parse_file
from gendiff.formatters.stylish import format_stylish
from gendiff.formatters.plain import format_plain
from gendiff.formatters.json import format_json


def build_ast(data1: Dict, data2: Dict) -> List[Dict]:

    all_keys = sorted(set(data1.keys()) | set(data2.keys()))
    result = []
    
    for key in all_keys:
        if key not in data1:
            result.append({
                'key': key,
                'status': 'added',
                'value': data2[key]
            })
        elif key not in data2:
            result.append({
                'key': key,
                'status': 'removed',
                'value': data1[key]
            })
        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            result.append({
                'key': key,
                'status': 'nested',
                'children': build_ast(data1[key], data2[key])
            })
        elif data1[key] == data2[key]:
            result.append({
                'key': key,
                'status': 'unchanged',
                'value': data1[key]
            })
        else:
            result.append({
                'key': key,
                'status': 'changed',
                'old_value': data1[key],
                'new_value': data2[key]
            })
    
    return result


def generate_diff(file_path1: str, file_path2: str, format_name: str = 'stylish') -> str:

    data1 = parse_file(file_path1)
    data2 = parse_file(file_path2)
    
    ast = build_ast(data1, data2)
    
    if format_name == 'stylish':
        result = format_stylish(ast)
        return f"{{\n{result}\n}}"
    elif format_name == 'plain':
        return format_plain(ast)
    elif format_name == 'json':
        return format_json(ast)
    else:
        raise ValueError(f"Unknown format: {format_name}")