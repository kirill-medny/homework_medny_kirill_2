from typing import Iterable

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency(transactions: Iterable[dict]) -> None:
    """
    Функция которая передает данные для проверки filter_by_currency
    """
    filter_currency = filter_by_currency(transactions, "USD")
    assert next(filter_currency) == {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }


def test_transaction_descriptions(transactions: Iterable[dict]) -> None:
    """
    Функция которая передает данные для проверки transaction_descriptions
    """
    transaction_descr = transaction_descriptions(transactions)
    assert next(transaction_descr) == "Перевод организации"
    assert next(transaction_descr) == "Перевод со счета на счет"
    assert next(transaction_descr) == "Перевод со счета на счет"
    assert next(transaction_descr) == "Перевод с карты на карту"
    assert next(transaction_descr) == "Перевод организации"


def test_card_number_generator() -> None:
    """
    Функция которая передает данные для проверки card_number_generator
    """
    generator = card_number_generator(1, 6)
    assert next(generator) == "0000 0000 0000 0001"
    assert next(generator) == "0000 0000 0000 0002"
    assert next(generator) == "0000 0000 0000 0003"
    assert next(generator) == "0000 0000 0000 0004"
    assert next(generator) == "0000 0000 0000 0005"
    assert next(generator) == "0000 0000 0000 0006"
