def format_stylish(diff):
    result = '{\n' + tree_view(diff) + '\n}'
    return result


def tree_view(diff, depth=1):
    lines = []
    for key, (type, value) in sorted(diff.items()):
        lines = create_formatted_line(lines, key, value, depth, type)
    result = '\n'.join(lines)
    return result


def create_formatted_line(lines, key, value, depth, type):
    if type == 'nested':
        indent = '    ' * depth
        child_diff = tree_view(value, depth + 1)
        formatted_value = f'{{\n{child_diff}\n{indent}}}'
        lines.append(f"{indent}    {key}: {formatted_value}")
    elif type == 'changed':
        lines = changed_data_diff(lines, value, depth, key)
    elif type == 'added':
        indent = '    ' * (depth - 1)
        formatted_value = format_value(value, depth + 1)
        lines.append(f"{indent}  + {key}: {formatted_value}")
    elif type == 'removed':
        indent = '    ' * (depth - 1)
        formatted_value = format_value(value, depth + 1)
        lines.append(f"{indent}  - {key}: {formatted_value}")
    else:
        indent = '    ' * (depth - 1)
        formatted_value = format_value(value, depth + 1)
        lines.append(f"{indent}    {key}: {formatted_value}")
    return lines


def format_value(value, depth):
    if isinstance(value, dict):
        indent = '    ' * (depth - 1)
        lines = []
        for key, val in value.items():
            formatted_value = format_value(val, depth + 1)
            lines.append(f"{'    ' * depth}{key}: {formatted_value}")
        return '{\n' + '\n'.join(lines) + '\n' + indent + '}'
    elif isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    return str(value)


def changed_data_diff(lines, value, depth, key):
    old, new = value
    indent = '    ' * (depth - 1)
    formatted_old = format_value(old, depth + 1)
    formatted_new = format_value(new, depth + 1)
    lines.append(f"{indent}  - {key}: {formatted_old}")
    lines.append(f"{indent}  + {key}: {formatted_new}")
    return lines