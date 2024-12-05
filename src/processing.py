import logging
import os
import re
from collections import Counter
from datetime import datetime
from typing import Any

# Запуск pytest происходит из корневой директории проекта, а запуск скрипта из директории src.
# Эта конструкция нужна для выравнивания путей.
path = os.path.join("logs", "processing.log")

# Базовые настройки логгера
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(path, "w")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")

file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def filter_by_state(transactions_list: list, state: str = "EXECUTED") -> list:
    """Функция возвращает список словарей, содержащий только те словари, у которых ключ 'state' соответствует\
    указанному значению в параметре state."""
    if not transactions_list:
        logger.error(f"Передан пустой список операций {transactions_list}.")
        raise ValueError("Список операций не должен быть пустым!")

    result = []
    for transaction in transactions_list:
        if transaction == {}:
            continue
        if transaction["state"] == state:
            result.append(transaction)

    logger.info(f"Список операций успешно отфильтрован по статусу {state}.")
    return result


def filter_by_rub_json(transactions_list: list) -> list:
    """Функция возвращает список словарей, содержащий только те словари, у которых ключ 'code' равен RUB."""
    if not transactions_list:
        logger.error(f"Передан пустой список операций {transactions_list}.")
        raise ValueError("Список операций не должен быть пустым!")

    result = []
    for transaction in transactions_list:
        if transaction == {}:
            continue
        if transaction["operationAmount"]["currency"]["code"] == "RUB":
            result.append(transaction)

    logger.info("Список операций успешно отфильтрован по ключу code=RUB.")
    return result


def filter_by_rub_cvs_xlsx(transactions_list: list) -> list:
    """Функция возвращает список словарей, содержащий только те словари, у которых ключ 'code' равен RUB."""
    if not transactions_list:
        logger.error(f"Передан пустой список операций {transactions_list}.")
        raise ValueError("Список операций не должен быть пустым!")

    result = []
    for transaction in transactions_list:
        if transaction == {}:
            continue
        if transaction["currency_code"] == "RUB":
            result.append(transaction)

    logger.info("Список операций успешно отфильтрован по ключу code=RUB.")
    return result


def sort_by_date(transactions_list: list, sorting_order: int | bool = 1) -> list:
    """Функция возвращает новый список, отсортированный по дате."""
    if not transactions_list:
        logger.error(f"Передан пустой список операций {transactions_list}.")
        raise ValueError("Список операций не должен быть пустым!")

    # Преобразуем строки дат в объекты datetime для корректной сортировки
    def get_date_key(transaction: dict[str, Any]) -> datetime:
        date_str = transaction.get("date")  # Получаем значение даты
        if isinstance(date_str, str) and len(date_str) >= 10:  # Проверяем, что это строка и она достаточно длинная
            try:
                return datetime.strptime(date_str[:10], "%Y-%m-%d")
            except ValueError:
                logger.error(f"Неверный формат даты: {date_str}")
                return datetime.min  # Возвращаем минимальную дату, если формат неверный
        return datetime.min  # Возвращаем минимальную дату, если дата отсутствует или не строка

    try:
        sorted_transactions = sorted(
            transactions_list,
            key=get_date_key,
            reverse=sorting_order == 0,  # Если sorting_order 0, сортируем по возрастанию
        )
    except Exception as e:
        logger.error(f"Ошибка при сортировке транзакций: {e}")
        raise

    logger.info(
        f"Список операций успешно отсортирован по дате {'по убыванию' if sorting_order == 0 else 'по возрастанию'}."
    )
    return sorted_transactions


def find_transactions(transactions_list: list, key_string: str) -> list:
    """Принимает список словарей с данными о банковских операциях и строку поиска. Возвращает список словарей, у \
    которых в описании есть данная строка."""
    templates = [
        "перевод с карты на карту",
        "перевод организации",
        "перевод со счета на счет",
        "открытие вклада",
        "перевод с карты на счет",
    ]
    key_list = []
    pattern = re.compile(key_string.lower())
    for temp in templates:
        if re.search(pattern, temp):
            key_list.append(temp)

    filtered_transactions_list = []
    for key in key_list:
        for transaction in transactions_list:
            if transaction == {}:
                continue
            if transaction["description"].lower() != key:
                continue
            filtered_transactions_list.append(transaction)

    logger.info(f"Список операций успешно отфильтрован по описанию {key_string}.")
    return filtered_transactions_list


def group_transactions_by_category(transactions_list: list) -> dict:
    """Принимает список словарей с данными о банковских операциях и список категорий операций, а возвращать словарь, \
    в котором ключи — это названия категорий, а значения — это количество операций в каждой категории."""
    description_list = [
        transaction.get("description")
        for transaction in transactions_list
        if transaction.get("description") is not None
    ]
    grouped_transactions = Counter(description_list)

    logger.info("Список операций успешно сгрупирован по названиям категорий.")
    return dict(grouped_transactions)
