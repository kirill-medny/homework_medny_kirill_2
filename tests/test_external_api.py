import os
import unittest
from unittest.mock import MagicMock, patch

import requests

from src.external_api import currency_conversion

API_KEY = os.getenv("API_KEY")
API_URL = "https://api.apilayer.com/exchangerates_data/convert?to={to}&from={from_}&amount={amount}"


class TestCurrencyConversion(unittest.TestCase):

    @patch("src.external_api.requests.get")  # Мокаем requests.get
    def test_conversion_rub(self, mock_get: MagicMock) -> None:
        transaction = {"operationAmount": {"amount": 1000, "currency": {"code": "RUB"}}}
        result = currency_conversion(transaction)
        self.assertEqual(result, 1000.0)  # Проверяем, что результат равен 1000.0

    @patch("src.external_api.requests.get")  # Мокаем requests.get
    def test_conversion_usd(self, mock_get: MagicMock) -> None:
        transaction = {"operationAmount": {"amount": 100, "currency": {"code": "USD"}}}
        # Настраиваем мок-ответ
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"result": 7500.0}  # Предположим, что 100 USD = 7500 RUB
        mock_get.return_value = mock_response

        result = currency_conversion(transaction)
        self.assertEqual(result, 7500.0)  # Проверяем, что результат равен 7500.0

    @patch("src.external_api.requests.get")  # Мокаем requests.get
    def test_conversion_eur(self, mock_get: MagicMock) -> None:
        transaction = {"operationAmount": {"amount": 100, "currency": {"code": "EUR"}}}
        # Настраиваем мок-ответ
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"result": 8500.0}  # Предположим, что 100 EUR = 8500 RUB
        mock_get.return_value = mock_response

        result = currency_conversion(transaction)
        self.assertEqual(result, 8500.0)  # Проверяем, что результат равен 8500.0

    @patch("src.external_api.requests.get")  # Мокаем requests.get
    def test_conversion_invalid_currency(self, mock_get: MagicMock) -> None:
        transaction = {"operationAmount": {"amount": 100, "currency": {"code": "JPY"}}}  # Неподдерживаемая валюта
        result = currency_conversion(transaction)
        self.assertEqual(result, 0.0)  # Проверяем, что результат равен 0.0

    @patch("src.external_api.requests.get")  # Мокаем requests.get
    def test_conversion_no_amount(self, mock_get: MagicMock) -> None:
        transaction = {"operationAmount": {"currency": {"code": "USD"}}}  # Нет amount
        result = currency_conversion(transaction)
        self.assertEqual(result, 0.0)  # Проверяем, что результат равен 0.0

    @patch("src.external_api.requests.get")  # Мокаем requests.get
    def test_conversion_api_error(self, mock_get: MagicMock) -> None:
        transaction = {"operationAmount": {"amount": 100, "currency": {"code": "USD"}}}
        # Настраиваем мок-ответ для ошибки API
        mock_response = MagicMock()
        mock_response.status_code = 500  # Ошибка сервера
        mock_get.return_value = mock_response

        result = currency_conversion(transaction)
        self.assertEqual(result, 0.0)  # Проверяем, что результат равен 0.0

    @patch("src.external_api.requests.get")  # Мокаем requests.get
    def test_conversion_request_exception(self, mock_get: MagicMock) -> None:
        transaction = {"operationAmount": {"amount": 100, "currency": {"code": "USD"}}}
        # Настраиваем мок для генерации исключения
        mock_get.side_effect = requests.exceptions.RequestException("Network error")

        result = currency_conversion(transaction)
        self.assertEqual(result, 0.0)  # Проверяем, что результат равен 0.0
