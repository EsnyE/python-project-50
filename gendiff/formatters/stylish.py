def format_stylish(diff, depth=1):
    if isinstance(diff, list):
        diff_dict = {item['key']: item for item in diff}
    else:
        diff_dict = diff
    
    if not diff_dict:
        return '{}'
    
    base_indent = '    ' * (depth - 1)
    item_indent = base_indent + '    '
    lines = []
    
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
                old_fmt = format_value(old, depth + 1)
                new_fmt = format_value(new, depth + 1)
                lines.append(f"{base_indent}  - {key}: {old_fmt}")
                lines.append(f"{base_indent}  + {key}: {new_fmt}")
                
            else:  # unchanged
                data = value.get('value')
                lines.append(f"{item_indent}{key}: {format_value(data, depth + 1)}")
    
    result = '{\n' + '\n'.join(lines) + '\n' + base_indent + '}'
    return result


def format_value(value, depth):
    if isinstance(value, dict):
        indent = '    ' * depth
        lines = []
        for k, v in value.items():
            lines.append(f"{indent}{k}: {format_value(v, depth + 1)}")
        return '{\n' + '\n'.join(lines) + '\n' + ('    ' * (depth - 1)) + '}'
    elif value is None:
        return 'null'
    elif isinstance(value, bool):
        return str(value).lower()
    else:
        return str(value)