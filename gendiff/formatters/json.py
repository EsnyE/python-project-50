import json
from typing import Dict, List


def format_json(ast: List[Dict]) -> str:
    return json.dumps(ast, indent=2, ensure_ascii=False)