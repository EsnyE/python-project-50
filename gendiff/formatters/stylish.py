from typing import Any, List, Dict


def format_value(value: Any, depth: int = 0) -> str:

    if isinstance(value, dict):
        indent = '    ' * depth
        lines = ['{']
        for k, v in sorted(value.items()):
            formatted_v = format_value(v, depth + 1)
            lines.append(f"{indent}    {k}: {formatted_v}")
        lines.append('    ' * depth + '}')
        return '\n'.join(lines)
    
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    if isinstance(value, str):
        return value
    return str(value)


def format_stylish(ast: List[Dict], depth: int = 0) -> str:

    indent = '    ' * depth
    lines = []
    
    for node in ast:
        key = node['key']
        status = node['status']
        
        if status == 'nested':
            lines.append(f"{indent}    {key}: {{")
            lines.append(format_stylish(node['children'], depth + 1))
            lines.append(f"{indent}    }}")
        elif status == 'unchanged':
            value = format_value(node['value'], depth)
            lines.append(f"{indent}    {key}: {value}")
        elif status == 'added':
            value = format_value(node['value'], depth)
            lines.append(f"{indent}  + {key}: {value}")
        elif status == 'removed':
            value = format_value(node['value'], depth)
            lines.append(f"{indent}  - {key}: {value}")
        elif status == 'changed':
            old_value = format_value(node['old_value'], depth)
            new_value = format_value(node['new_value'], depth)
            lines.append(f"{indent}  - {key}: {old_value}")
            lines.append(f"{indent}  + {key}: {new_value}")
    
    return '\n'.join(lines)