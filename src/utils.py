import json


def load_transactions(file_path: str) -> list:
    """Функция принимает json возвращает list или dict"""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            repos = json.load(file)
        if isinstance(repos, list):
            return repos
        else:
            return []
    except Exception as e:
        print(f"Ошибка {e}")
        return []
