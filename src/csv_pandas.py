import csv

import pandas as pd


def read_csv(file_path: str) -> list[dict]:
    """Функция принимает в качестве аргумента путь к csv-файлу и возвращает его содержимое в виде списка словарей."""
    with open(file_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)


def read_excel(file_path: str) -> list[dict]:
    """Функция принимает в качестве аргумента путь к excel-файлу и возвращает его содержимое в виде списка словарей."""
    excel_data = pd.read_excel(file_path).to_dict(orient="records")
    return excel_data
