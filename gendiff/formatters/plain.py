from typing import Any, List, Dict
def format_plain(ast, path=''):
    lines = []
    
    if isinstance(ast, list):
        ast_dict = {item['key']: item for item in ast}
    else:
        ast_dict = ast
    
    for key, value in sorted(ast_dict.items()):
        if isinstance(value, dict) and 'status' in value:
            status = value['status']
            current_path = f"{path}.{key}" if path else key
            
            if status == 'nested':
                children = format_plain(value['children'], current_path)
                lines.append(children)
                
            elif status == 'added':
                data = value.get('value')
                formatted = format_plain_value(data)
                lines.append(
                    f"Property '{current_path}' was added with value: {formatted}"
                )
                
            elif status == 'removed':
                lines.append(f"Property '{current_path}' was removed")
                
            elif status == 'changed':
                old = value.get('old_value')
                new = value.get('new_value')
                formatted_old = format_plain_value(old)
                formatted_new = format_plain_value(new)
                lines.append(
                    f"Property '{current_path}' was updated. "
                    f"From {formatted_old} to {formatted_new}"
                )
    
    return '\n'.join(filter(None, lines))


def format_plain_value(value):
    if isinstance(value, dict):
        return '[complex value]'
    elif value is None:
        return 'null'
    elif isinstance(value, bool):
        return str(value).lower()
    elif isinstance(value, str):
        return f"'{value}'"
    else:
        return str(value)