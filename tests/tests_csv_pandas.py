import unittest
from unittest.mock import MagicMock, mock_open, patch

import pandas as pd

from src.csv_pandas import read_csv, read_excel


class TestExternalQuery(unittest.TestCase):
    @patch("builtins.open", new_callable=mock_open, read_data="name,age\nVasya,30\nPetya,25")
    def test_read_csv(self, mock_file: MagicMock) -> None:
        """Тестируем функцию read_csv."""
        expected = [{"name": "Vasya", "age": "30"}, {"name": "Petya", "age": "25"}]
        result = read_csv("fake_path.csv")
        self.assertEqual(result, expected)

    @patch("csv.DictReader")
    @patch("builtins.open", new_callable=mock_open, read_data="fake data")
    def test_read_csv_dictreader(self, mock_file: MagicMock, mock_dictreader: MagicMock) -> None:
        """Тестируем функцию read_csv метод DictReader библиотеки csv."""
        mock_dictreader.return_value = [{"name": "Vasya", "age": "30"}, {"name": "Petya", "age": "25"}]
        expected_result = [{"name": "Vasya", "age": "30"}, {"name": "Petya", "age": "25"}]
        result = read_csv("fake_path.csv")
        self.assertEqual(result, expected_result)

    @patch("src.csv_pandas.pd.read_excel")
    def test_read_excel(self, mock_read_excel: MagicMock) -> None:
        """Тестируем функцию read_excel."""
        fake_data = {"Column1": [1, 2, 3], "Column2": ["A", "B", "C"]}
        mock_read_excel.return_value = pd.DataFrame(fake_data)
        expected_result = [
            {"Column1": 1, "Column2": "A"},
            {"Column1": 2, "Column2": "B"},
            {"Column1": 3, "Column2": "C"},
        ]
        result = read_excel("fake_path.xlsx")
        print(result)
        self.assertEqual(result, expected_result)
