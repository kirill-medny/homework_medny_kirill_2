import unittest
from unittest.mock import patch, mock_open
import json
import csv
import pandas as pd

# Предполагаем, что функции load_transactions_from_json, load_transactions_from_csv,
# load_transactions_from_xlsx, filter_transactions и sort_transactions уже определены в вашем коде.

class TestTransactionFunctions(unittest.TestCase):

    def setUp(self):
        # Пример данных для тестирования
        self.transactions = [
            {'date': '2023-01-01', 'description': 'Транзакция 1', 'status': 'EXECUTED', 'account': '1234567890123456', 'amount': 1000, 'currency': 'RUB'},
            {'date': '2023-01-02', 'description': 'Транзакция 2', 'status': 'CANCELED', 'account': '1234567890123456', 'amount': 2000, 'currency': 'USD'},
            {'date': '2023-01-03', 'description': 'Транзакция 3', 'status': 'EXECUTED', 'account': '1234567890123456', 'amount': 1500, 'currency': 'RUB'},
            {'date': '2023-01-04', 'description': 'Транзакция 4', 'status': 'PENDING', 'account': '1234567890123456', 'amount': 500, 'currency': 'EUR'},
        ]

    @patch("builtins.open", new_callable=mock_open, read_data='[{"date": "2023-01-01", "description": "Транзакция 1", "status": "EXECUTED", "account": "1234567890123456", "amount": 1000, "currency": "RUB"}]')
    def test_load_transactions_from_json(self, mock_file):
        transactions = load_transactions_from_json('dummy_path.json')
        self.assertEqual(len(transactions), 1)
        self.assertEqual(transactions[0]['description'], 'Транзакция 1')

    @patch("builtins.open", new_callable=mock_open, read_data='date,description,status,account,amount,currency\n2023-01-01,Транзакция 1,EXECUTED,1234567890123456,1000,RUB\n')
    def test_load_transactions_from_csv(self, mock_file):
        transactions = load_transactions_from_csv('dummy_path.csv')
        self.assertEqual(len(transactions), 1)
        self.assertEqual(transactions[0]['description'], 'Транзакция 1')

    @patch("pandas.read_excel")
    def test_load_transactions_from_xlsx(self, mock_read_excel):
        mock_read_excel.return_value = pd.DataFrame(self.transactions)
        transactions = load_transactions_from_xlsx('dummy_path.xlsx')
        self.assertEqual(len(transactions), 4)
        self.assertEqual(transactions[0]['description'], 'Транзакция 1')

    def test_filter_transactions(self):
        filtered = filter_transactions(self.transactions, 'EXECUTED')
        self.assertEqual(len(filtered), 2)
        self.assertEqual(filtered[0]['description'], 'Транзакция 1')

    def test_sort_transactions_ascending(self):
        sorted_transactions = sort_transactions(self.transactions, ascending=True)
        self.assertEqual(sorted_transactions[0]['date'], '2023-01-01')

    def test_sort_transactions_descending(self):
        sorted_transactions = sort_transactions(self.transactions, ascending=False)
        self.assertEqual(sorted_transactions[0]['date'], '2023-01-04')

if __name__ == "__main__":
    unittest.main()

