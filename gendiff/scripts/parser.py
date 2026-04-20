import json
import os
from typing import Dict, Any


def parse_file(file_path: str) -> Dict[str, Any]:

    file_extension = _get_file_extension(file_path)
    
    if file_extension != '.json':
        raise ValueError(f"Unsupported file format: {file_extension}. Only .json is supported.")
    
    content = _read_file_content(file_path)
    return json.loads(content)


def _get_file_extension(file_path: str) -> str:

    _, extension = os.path.splitext(file_path)
    return extension.lower()


def _read_file_content(file_path: str) -> str:
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()