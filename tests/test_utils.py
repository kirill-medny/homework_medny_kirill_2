import unittest
from unittest.mock import MagicMock, patch

from src.utils import read_file


class TestReadFile(unittest.TestCase):

    @patch("src.utils._read_json")
    def test_read_json_file(self, mock_read_json: MagicMock) -> None:
        # Настройка mock-ответа
        mock_read_json.return_value = [{"key": "value"}]
        result = read_file("test.json")
        mock_read_json.assert_called_once_with("test.json")
        self.assertEqual(result, [{"key": "value"}])

    @patch("src.utils._read_csv")
    def test_read_csv_file(self, mock_read_csv: MagicMock) -> None:
        # Настройка mock-ответа
        mock_read_csv.return_value = [{"column1": "data1", "column2": "data2"}]
        result = read_file("test.csv")
        mock_read_csv.assert_called_once_with("test.csv")
        self.assertEqual(result, [{"column1": "data1", "column2": "data2"}])

    @patch("src.utils._read_xlsx")
    def test_read_xlsx_file(self, mock_read_xlsx: MagicMock) -> None:
        # Настройка mock-ответа
        mock_read_xlsx.return_value = [{"column1": "data1", "column2": "data2"}]
        result = read_file("test.xlsx")
        mock_read_xlsx.assert_called_once_with("test.xlsx")
        self.assertEqual(result, [{"column1": "data1", "column2": "data2"}])

    def test_read_file_with_invalid_extension(self) -> None:
        # Проверяем, что функция возвращает пустой список для неподдерживаемого формата
        result = read_file("test.txt")
        self.assertEqual(result, [])

    def test_read_file_with_no_extension(self) -> None:
        # Проверяем, что функция возвращает пустой список для файла без расширения
        result = read_file("test")
        self.assertEqual(result, [])
