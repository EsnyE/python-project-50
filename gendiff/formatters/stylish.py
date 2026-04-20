def format_stylish(diff, depth=1):
    indent = '    ' * (depth - 1)
    lines = []
    
    for key, value in sorted(diff.items()):
        if isinstance(value, dict) and 'status' in value:
            status = value['status']
            data = value.get('value')
            
            if status == 'nested':
                children = format_stylish(value['children'], depth + 1)
                lines.append(f"{indent}    {key}: {children}")
            elif status == 'added':
                formatted = format_value(data, depth + 1)
                lines.append(f"{indent}  + {key}: {formatted}")
            elif status == 'removed':
                formatted = format_value(data, depth + 1)
                lines.append(f"{indent}  - {key}: {formatted}")
            elif status == 'changed':
                old = value.get('old_value')
                new = value.get('new_value')
                lines.append(f"{indent}  - {key}: {format_value(old, depth + 1)}")
                lines.append(f"{indent}  + {key}: {format_value(new, depth + 1)}")
            else:
                lines.append(f"{indent}    {key}: {format_value(data, depth + 1)}")
    
    return '{\n' + '\n'.join(lines) + '\n' + indent + '}'