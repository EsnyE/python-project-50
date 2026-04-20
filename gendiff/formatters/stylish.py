# formatters/stylish.py

from typing import Any, List, Dict


def format_value(value: Any) -> str:
    """Форматирует значение для вывода."""
    if value is None:
        return 'null'
    if isinstance(value, bool):
        return str(value).lower()
    if isinstance(value, str):
        return value
    if isinstance(value, dict):
        return '[complex value]'
    return str(value)


def format_stylish(ast: List[Dict], depth: int = 0) -> str:
    """
    Форматирует AST в стиле stylish.
    """
    if not ast:
        return ''
    
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
            value = format_value(node['value'])
            lines.append(f"{indent}    {key}: {value}")
        
        elif status == 'added':
            value = format_value(node.get('new_value', node.get('value')))
            lines.append(f"{indent}  + {key}: {value}")
        
        elif status == 'removed':
            value = format_value(node.get('old_value', node.get('value')))
            lines.append(f"{indent}  - {key}: {value}")
        
        elif status == 'changed':
            old_value = format_value(node['old_value'])
            new_value = format_value(node['new_value'])
            lines.append(f"{indent}  - {key}: {old_value}")
            lines.append(f"{indent}  + {key}: {new_value}")
    
    return '\n'.join(lines)