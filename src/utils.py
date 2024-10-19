import json
import os.path
from typing import List, Dict, Union


def load_transactions(file_path: str) -> Union[dict, list]:
    """Функция принимает json возвращает list или dict"""
    if not os.path.exists(file_path):
        return []
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as json_file:
        try:
            data = json.load(json_file)
            if type(data) == list:
                return data
            else:
                return []
        except json.JSONDecodeError:
            return []

transactions = load_transactions('.data/operations.json')
print(transactions)