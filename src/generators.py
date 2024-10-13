"""Модуль генераторов для обработки массивов транзакций"""

from typing import Iterable, Iterator


def filter_by_currency(transactions: Iterable[dict], currency_code: str) -> Iterator[dict]:
    """Функция принимает список словарей (или объект-генератор) с банковскими
    операциями и возвращает итератор, который выдает по очереди операции,
    в которых указана заданная валюта."""
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency_code:
            yield transaction


def transaction_descriptions(transactions: Iterable[dict]) -> Iterator[str]:
    """Функция принимает список словарей (или объект-генератор) с банковскими
    операциями и возвращает итератор, который выдает описание каждой операции
    по очереди."""
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start: int, stop: int) -> Iterator[str]:
    """Генератор номеров банковских карт в формате XXXX XXXX XXXX XXXX
    Диапазоны передаются как параметры генератора."""
    for num in range(start, stop + 1):
        number = "0" * (16 - len(str(num))) + str(num)
        string_to_return = ""
        block_counter = 0
        for digit in number:
            block_counter += 1
            if block_counter <= 4:
                string_to_return += digit
            else:
                string_to_return += " " + digit
                block_counter = 1
        yield string_to_return
