from typing import Any, List, Dict


def format_value(value: Any, depth: int = 0) -> str:
    """Форматирует значение для вывода с учетом вложенности."""
    if isinstance(value, dict):
        indent = '    ' * depth
        current_indent = '    ' * (depth + 1)
        lines = ['{']
        for k, v in sorted(value.items()):
            formatted_v = format_value(v, depth + 1)
            lines.append(f"{current_indent}{k}: {formatted_v}")
        lines.append(f"{indent}}}")
        return '\n'.join(lines)
    
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    if isinstance(value, str):
        return value
    return str(value)


def format_stylish(ast: List[Dict], depth: int = 0) -> str:
    """Форматирует AST в стиле stylish."""
    indent = '    ' * depth
    current_indent = '    ' * (depth + 1)
    lines = []
    
    for node in ast:
        key = node['key']
        status = node['status']
        
        if status == 'nested':
            lines.append(f"{indent}{key}: {{")
            lines.append(format_stylish(node['children'], depth + 1))
            lines.append(f"{indent}}}")
        elif status == 'unchanged':
            value = format_value(node['value'], depth + 1)
            lines.append(f"{indent}{key}: {value}")
        elif status == 'added':
            value = format_value(node['value'], depth + 1)
            lines.append(f"{indent}+ {key}: {value}")
        elif status == 'removed':
            value = format_value(node['value'], depth + 1)
            lines.append(f"{indent}- {key}: {value}")
        elif status == 'changed':
            old_value = format_value(node['old_value'], depth + 1)
            new_value = format_value(node['new_value'], depth + 1)
            lines.append(f"{indent}- {key}: {old_value}")
            lines.append(f"{indent}+ {key}: {new_value}")
    
    return '\n'.join(lines)