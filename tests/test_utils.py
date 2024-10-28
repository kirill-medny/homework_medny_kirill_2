import json
import unittest
from unittest.mock import MagicMock, mock_open, patch

from src.utils import load_transactions


class TestGetTransactions(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open, read_data='[{"transaction": "data1"}, {"transaction": "data2"}]')
    def test_load_transactions_valid_file(self, mock_file: MagicMock) -> None:
        expected_data = [{"transaction": "data1"}, {"transaction": "data2"}]
        result = load_transactions("fake_path.json")
        self.assertEqual(result, expected_data)
        mock_file.assert_called_once_with("fake_path.json", "r", encoding="Windows-1251")

    @patch("builtins.open", new_callable=mock_open, read_data="{}")
    def test_load_transactions_invalid_content(self, mock_file: MagicMock) -> None:
        result = load_transactions("fake_path.json")
        self.assertEqual(result, [])
        mock_file.assert_called_once_with("fake_path.json", "r", encoding="Windows-1251")

    @patch("builtins.open", new_callable=mock_open, read_data="")
    def test_load_transactions_empty_file(self, mock_file: MagicMock) -> None:
        result = load_transactions("fake_path.json")
        self.assertEqual(result, [])
        mock_file.assert_called_once_with("fake_path.json", "r", encoding="Windows-1251")

    @patch("builtins.open", side_effect=FileNotFoundError)
    def test_load_transactions_file_not_found(self, mock_file: MagicMock) -> None:
        result = load_transactions("fake_path.json")
        self.assertEqual(result, [])
        mock_file.assert_called_once_with("fake_path.json", "r", encoding="Windows-1251")

    @patch("builtins.open", new_callable=mock_open, read_data='{"transaction": "data"}')
    @patch("json.load", side_effect=json.JSONDecodeError("Expecting value", "", 0))
    def test_load_transactions_json_decode_error(self, mock_json_load: MagicMock, mock_file: MagicMock) -> None:
        result = load_transactions("fake_path.json")
        self.assertEqual(result, [])
        mock_file.assert_called_once_with("fake_path.json", "r", encoding="Windows-1251")
        mock_json_load.assert_called_once()
