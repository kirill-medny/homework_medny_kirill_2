# -*- coding: Windows-1251 -*-
import csv
import json
import re
from typing import Any, Dict, Hashable, List

import pandas as pd


def search_transactions(transactions: List[Dict[str, Any]], search_string: str) -> List[Dict[str, Any]]:
    """
    ������� ��� ������ ���������� �������� �� ��������.

    :param transactions: ������ �������� � ������� � ���������� ���������.
    :param search_string: ������ ��� ������ � �������� ��������.
    :return: ������ ��������, � ������� � �������� ���� ������ ������.
    """
    # ����������� ���������� ��������� ��� ������
    pattern = re.compile(re.escape(search_string), re.IGNORECASE)

    # ��������� �������� �� ��������
    result = [transaction for transaction in transactions if pattern.search(transaction.get("description", ""))]

    return result


# ������ �������������
transactions = [
    {"id": 1, "description": "������� �� ����", "amount": 100},
    {"id": 2, "description": "������ �� ������", "amount": 200},
    {"id": 3, "description": "������� �������", "amount": 150},
    {"id": 4, "description": "������� � ��������", "amount": 50},
]

search_string = "�������"
filtered_transactions = search_transactions(transactions, search_string)

print(filtered_transactions)


def count_transactions_by_category(transactions: List[Dict[str, Any]], categories: List[str]) -> Dict[str, int]:
    """
    ������� ��� �������� ���������� ���������� �������� �� ����������.

    :param transactions: ������ �������� � ������� � ���������� ���������.
    :param categories: ������ ��������� ��������.
    :return: ������� � ����������� � ����������� �������� � ������ ���������.
    """
    # �������������� ������� ��� �������� �����������
    category_count = {category: 0 for category in categories}

    # ������������ ���������� �������� ��� ������ ���������
    for transaction in transactions:
        description = transaction.get("description", "")
        for category in categories:
            if category.lower() in description.lower():
                category_count[category] += 1

    return category_count


# ������ �������������
transactions = [
    {"id": 1, "description": "������� �� ����", "amount": 100},
    {"id": 2, "description": "������ �� ������", "amount": 200},
    {"id": 3, "description": "������� �������", "amount": 150},
    {"id": 4, "description": "������� � ��������", "amount": 50},
    {"id": 5, "description": "������ ������������ �����", "amount": 75},
]

categories = ["�������", "������", "�������"]
category_counts = count_transactions_by_category(transactions, categories)

print(category_counts)


# def load_transactions_from_json(file_path: pathlib.Path) -> List[Dict[str, Any]]:
#     with open(file_path, "r", encoding="utf-8") as file:
#         return json.load(file)
def load_transactions_from_json(file_path: str) -> List[Dict[str, Any]]:
    """
    ��������� ���������� �� JSON-�����.
    Args:
        file_path: ���� � JSON-�����.
    Returns:
        ������ ��������, ��� ������ ������� ������������ ����������. ���������� ������ ������ ��� ������.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            # �������� �� ������������ ������: ������������, ��� ������ - ��� ������ ��������
            if isinstance(data, list) and all(isinstance(item, dict) for item in data):
                return data
            else:
                print("������: JSON-���� �� �������� ������ ��������.")
                return []
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"������ ��� �������� �����: {e}")
        return []


# def load_transactions_from_csv(file_path: pathlib.Path) -> List[Dict[str, Any]]:
#     with open(file_path, "r", encoding="utf-8") as file:
#         return list(csv.DictReader(file))


def load_transactions_from_csv(file_path: str) -> List[Dict[str, Any]]:
    """
    ��������� ���������� �� CSV-�����.

    Args:
        file_path: ���� � CSV-�����.

    Returns:
        ������ ��������, ��� ������ ������� ������������ ����������. ���������� ������ ������ ��� ������.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError:
        print(f"������: ���� {file_path} �� ������.")
        return []
    except csv.Error as e:
        print(f"������ ��� ������ CSV-�����: {e}")
        return []


# def load_transactions_from_xlsx(file_path: pathlib.Path) -> List[Dict[str, Any]]:
#     return pd.read_excel(file_path).to_dict(orient="records")
def load_transactions_from_xlsx(file_path: str) -> List[Dict[Hashable, Any]]:
    """
    ��������� ���������� �� ����� XLSX � ���������� �� � ���� ������ ��������.

    Args:
        file_path: ���� � ����� XLSX.

    Returns:
     ������ ��������, ��� ������ ������� ������������ ���� ����������. ���������� ������ ������, ���� ��������� ������.
    """
    try:
        return pd.read_excel(file_path).to_dict(orient="records")
    except (FileNotFoundError, pd.errors.EmptyDataError, pd.errors.ParserError) as e:
        print(f"������ ��� �������� �����: {e}")  # ����� ������������� ��������� �� ������
        return []


def filter_transactions(transactions: list[dict[str, Any]], status: str) -> List[Dict[str, Any]]:
    return [t for t in transactions if t["status"].lower() == status.lower()]


def sort_transactions(transactions: list[dict[str, Any]], ascending: bool) -> List[Dict[str, Any]]:
    return sorted(transactions, key=lambda x: x["date"], reverse=not ascending)
