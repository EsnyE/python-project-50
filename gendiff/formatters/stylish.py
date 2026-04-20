def format_stylish(diff, depth=1):
    """
    Форматирует дерево различий в стильный формат.
    
    Args:
        diff: список или словарь с деревом различий
        depth: текущий уровень вложенности
    
    Returns:
        str: отформатированная строка в stylish формате
    """
    # Базовый отступ для текущего уровня
    base_indent = '    ' * (depth - 1)
    # Отступ для элементов внутри структуры
    item_indent = '    ' * depth
    
    lines = []

    # Если diff - это список, преобразуем его в словарь для обработки
    if isinstance(diff, list):
        diff_dict = {item['key']: item for item in diff}
    else:
        diff_dict = diff
    
    for key, value in sorted(diff_dict.items()):
        if isinstance(value, dict) and 'status' in value:
            status = value['status']
            
            if status == 'nested':
                children = format_stylish(value['children'], depth + 1)
                lines.append(f"{item_indent}{key}: {children}")
                
            elif status == 'added':
                data = value.get('value')
                formatted = format_value(data, depth + 1)
                lines.append(f"{base_indent}  + {key}: {formatted}")
                
            elif status == 'removed':
                data = value.get('value')
                formatted = format_value(data, depth + 1)
                lines.append(f"{base_indent}  - {key}: {formatted}")
                
            elif status == 'changed':
                old = value.get('old_value')
                new = value.get('new_value')
                lines.append(f"{base_indent}  - {key}: {format_value(old, depth + 1)}")
                lines.append(f"{base_indent}  + {key}: {format_value(new, depth + 1)}")
                
            else:  # unchanged
                data = value.get('value')
                lines.append(f"{item_indent}{key}: {format_value(data, depth + 1)}")
    
    result = '{\n' + '\n'.join(lines) + '\n' + base_indent + '}'
    return result


def format_value(value, depth):
    """
    Форматирует значение в зависимости от его типа.
    
    Args:
        value: значение для форматирования
        depth: текущий уровень вложенности
    
    Returns:
        str: отформатированное значение
    """
    if isinstance(value, dict):
        base_indent = '    ' * (depth - 1)
        item_indent = '    ' * depth
        lines = []
        for k, v in value.items():
            lines.append(f"{item_indent}{k}: {format_value(v, depth + 1)}")
        return '{\n' + '\n'.join(lines) + '\n' + base_indent + '}'
    elif value is None:
        return 'null'
    elif isinstance(value, bool):
        return str(value).lower()
    elif isinstance(value, str):
        return value
    else:
        return str(value)