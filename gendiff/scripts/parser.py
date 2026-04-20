import json
import os
from typing import Dict, Any


def parse_file(file_path: str) -> Dict[str, Any]:

    _, ext = os.path.splitext(file_path)
    ext = ext.lower()
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if ext == '.json':
        return json.loads(content)
    elif ext in ('.yml', '.yaml'):
        try:
            import yaml
            return yaml.safe_load(content)
        except ImportError:
            raise RuntimeError("PyYAML is required for YAML support")
    else:
        raise ValueError(f"Unsupported file format: {ext}")