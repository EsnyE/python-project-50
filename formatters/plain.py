from typing import Any, List, Dict


def format_value(value: Any) -> str:
    if isinstance(value, dict):
        return '[complex value]'
    if value is None:
        return 'null'
    if isinstance(value, bool):
        return str(value).lower()
    if isinstance(value, str):
        return f"'{value}'"
    return str(value)


def format_plain(ast: List[Dict], path: str = '') -> str:

    lines = []
    
    for node in ast:
        key = node['key']
        current_path = f"{path}.{key}" if path else key
        status = node['status']
        
        if status == 'nested':
            lines.append(format_plain(node['children'], current_path))
        elif status == 'added':
            value = format_value(node['new_value'])
            lines.append(f"Property '{current_path}' was added with value: {value}")
        elif status == 'removed':
            lines.append(f"Property '{current_path}' was removed")
        elif status == 'changed':
            old_value = format_value(node['old_value'])
            new_value = format_value(node['new_value'])
            lines.append(f"Property '{current_path}' was updated. From {old_value} to {new_value}")
    
    return '\n'.join(lines)