def format_stylish(diff, depth=1):
    indent = '    ' * (depth - 1)
    lines = []

    if isinstance(diff, list):
        diff_dict = {item['key']: item for item in diff}
    else:
        diff_dict = diff
    
    for key, value in sorted(diff_dict.items()):
        if isinstance(value, dict) and 'status' in value:
            status = value['status']
            
            if status == 'nested':
                children = format_stylish(value['children'], depth + 1)
                lines.append(f"{indent}    {key}: {children}")
                
            elif status == 'added':
                data = value.get('value')
                formatted = format_value(data, depth + 1)
                lines.append(f"{indent}  + {key}: {formatted}")
                
            elif status == 'removed':
                data = value.get('value')
                formatted = format_value(data, depth + 1)
                lines.append(f"{indent}  - {key}: {formatted}")
                
            elif status == 'changed':
                old = value.get('old_value')
                new = value.get('new_value')
                lines.append(f"{indent}  - {key}: {format_value(old, depth + 1)}")
                lines.append(f"{indent}  + {key}: {format_value(new, depth + 1)}")
                
            else:  # unchanged
                data = value.get('value')
                lines.append(f"{indent}    {key}: {format_value(data, depth + 1)}")
    
    result = '{\n' + '\n'.join(lines) + '\n' + indent + '}'
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
    elif isinstance(value, str):
        return value
    else:
        return str(value)