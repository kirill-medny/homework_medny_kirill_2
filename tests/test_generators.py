from typing import Iterable

import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.mark.parametrize(
    "transactions, currency_code, expected",
    [
        # Тест с пустым списком транзакций
        ([], "USD", []),
        # Тест с одной транзакцией, которая совпадает по валюте
        (
            [{"operationAmount": {"currency": {"code": "USD"}}}],
            "USD",
            [{"operationAmount": {"currency": {"code": "USD"}}}],
        ),
        # Тест с одной транзакцией, которая не совпадает по валюте
        ([{"operationAmount": {"currency": {"code": "EUR"}}}], "USD", []),
        # Тест с несколькими транзакциями, из которых одна совпадает по валюте
        (
            [
                {"operationAmount": {"currency": {"code": "EUR"}}},
                {"operationAmount": {"currency": {"code": "USD"}}},
                {"operationAmount": {"currency": {"code": "GBP"}}},
            ],
            "USD",
            [{"operationAmount": {"currency": {"code": "USD"}}}],
        ),
        # Тест с несколькими транзакциями, все из которых совпадают по валюте
        (
            [{"operationAmount": {"currency": {"code": "USD"}}}, {"operationAmount": {"currency": {"code": "USD"}}}],
            "USD",
            [{"operationAmount": {"currency": {"code": "USD"}}}, {"operationAmount": {"currency": {"code": "USD"}}}],
        ),
    ],
)
def test_filter_by_currency(transactions: Iterable[dict], currency_code: str, expected: Iterable[dict]) -> None:
    assert list(filter_by_currency(transactions, currency_code)) == expected


@pytest.mark.parametrize(
    "transactions, expected",
    [
        # Тест с пустым списком транзакций
        ([], []),
        # Тест с одной транзакцией
        ([{"description": "Перевод организации"}], ["Перевод организации"]),
        # Тест с несколькими транзакциями
        (
            [
                {"description": "Перевод со счета на счет"},
                {"description": "Перевод с карты на карту"},
                {"description": "Перевод организации"},
            ],
            ["Перевод со счета на счет", "Перевод с карты на карту", "Перевод организации"],
        ),
    ],
)
def test_transaction_descriptions(transactions: Iterable[dict], expected: Iterable[dict]) -> None:
    """
    Функция которая передает данные для проверки transaction_descriptions
    """
    assert list(transaction_descriptions(transactions)) == expected


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
