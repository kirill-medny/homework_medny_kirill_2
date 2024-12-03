# -*- coding: Windows-1251 -*-
import re
import json
import csv
import pandas as pd

def search_transactions(transactions, search_string):
    """
    ������� ��� ������ ���������� �������� �� ��������.

    :param transactions: ������ �������� � ������� � ���������� ���������.
    :param search_string: ������ ��� ������ � �������� ��������.
    :return: ������ ��������, � ������� � �������� ���� ������ ������.
    """
    # ����������� ���������� ��������� ��� ������
    pattern = re.compile(re.escape(search_string), re.IGNORECASE)

    # ��������� �������� �� ��������
    result = [transaction for transaction in transactions if pattern.search(transaction.get('description', ''))]

    return result


# ������ �������������
transactions = [
    {'id': 1, 'description': '������� �� ����', 'amount': 100},
    {'id': 2, 'description': '������ �� ������', 'amount': 200},
    {'id': 3, 'description': '������� �������', 'amount': 150},
    {'id': 4, 'description': '������� � ��������', 'amount': 50},
]

search_string = '�������'
filtered_transactions = search_transactions(transactions, search_string)

print(filtered_transactions)


def count_transactions_by_category(transactions, categories):
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
        description = transaction.get('description', '')
        for category in categories:
            if category.lower() in description.lower():
                category_count[category] += 1

    return category_count


# ������ �������������
transactions = [
    {'id': 1, 'description': '������� �� ����', 'amount': 100},
    {'id': 2, 'description': '������ �� ������', 'amount': 200},
    {'id': 3, 'description': '������� �������', 'amount': 150},
    {'id': 4, 'description': '������� � ��������', 'amount': 50},
    {'id': 5, 'description': '������ ������������ �����', 'amount': 75},
]

categories = ['�������', '������', '�������']
category_counts = count_transactions_by_category(transactions, categories)

print(category_counts)




def load_transactions_from_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)


def load_transactions_from_csv(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return list(csv.DictReader(file))


def load_transactions_from_xlsx(file_path):
    return pd.read_excel(file_path).to_dict(orient='records')


def filter_transactions(transactions, status):
    return [t for t in transactions if t['status'].lower() == status.lower()]


def sort_transactions(transactions, ascending):
    return sorted(transactions, key=lambda x: x['date'], reverse=not ascending)



