from gendiff.formatters.stylish import format_stylish
from gendiff.formatters.plain import format_plain
from gendiff.formatters.json import format_json


def apply_format(ast, format_name: str) -> str:

    if format_name == 'stylish':
        return format_stylish(ast)
    elif format_name == 'plain':
        return format_plain(ast)
    elif format_name == 'json':
        return format_json(ast)
    else:
        raise ValueError(f"Unknown format: {format_name}")