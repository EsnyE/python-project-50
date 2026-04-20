from gendiff.scripts.parser import parse_file
from gendiff.formatters import apply_format


def build_ast(data1: dict, data2: dict) -> list:

    if not isinstance(data1, dict) or not isinstance(data2, dict):
        return []
    
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
        
            children = build_ast(data1[key], data2[key])
            result.append({
                'key': key,
                'status': 'nested',
                'children': children
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

    return apply_format(ast, format_name)