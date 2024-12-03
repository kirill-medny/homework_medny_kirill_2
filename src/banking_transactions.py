# -*- coding: Windows-1251 -*-
import re
import json
import csv
import pandas as pd

def search_transactions(transactions, search_string):
    """
    Функция для поиска банковских операций по описанию.

    :param transactions: Список словарей с данными о банковских операциях.
    :param search_string: Строка для поиска в описании операций.
    :return: Список словарей, у которых в описании есть данная строка.
    """
    # Компилируем регулярное выражение для поиска
    pattern = re.compile(re.escape(search_string), re.IGNORECASE)

    # Фильтруем операции по описанию
    result = [transaction for transaction in transactions if pattern.search(transaction.get('description', ''))]

    return result


# Пример использования
transactions = [
    {'id': 1, 'description': 'Перевод на счет', 'amount': 100},
    {'id': 2, 'description': 'Оплата за услуги', 'amount': 200},
    {'id': 3, 'description': 'Перевод средств', 'amount': 150},
    {'id': 4, 'description': 'Покупка в магазине', 'amount': 50},
]

search_string = 'перевод'
filtered_transactions = search_transactions(transactions, search_string)

print(filtered_transactions)


def count_transactions_by_category(transactions, categories):
    """
    Функция для подсчета количества банковских операций по категориям.

    :param transactions: Список словарей с данными о банковских операциях.
    :param categories: Список категорий операций.
    :return: Словарь с категориями и количеством операций в каждой категории.
    """
    # Инициализируем словарь для хранения результатов
    category_count = {category: 0 for category in categories}

    # Подсчитываем количество операций для каждой категории
    for transaction in transactions:
        description = transaction.get('description', '')
        for category in categories:
            if category.lower() in description.lower():
                category_count[category] += 1

    return category_count


# Пример использования
transactions = [
    {'id': 1, 'description': 'Перевод на счет', 'amount': 100},
    {'id': 2, 'description': 'Оплата за услуги', 'amount': 200},
    {'id': 3, 'description': 'Перевод средств', 'amount': 150},
    {'id': 4, 'description': 'Покупка в магазине', 'amount': 50},
    {'id': 5, 'description': 'Оплата коммунальных услуг', 'amount': 75},
]

categories = ['перевод', 'оплата', 'покупка']
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



