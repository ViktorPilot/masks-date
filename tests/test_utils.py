import os
from unittest.mock import patch

from src.utils import get_dict_transactions


def test_get_dict_transactions_valid(get_dict_transactions_valid: list[dict]) -> None:
    """Тестирование функции, преобразующей json-файл с транзакциями в список при стандартных значениях"""
    with patch("json.load") as mock_json:
        mock_json.return_value = get_dict_transactions_valid
        assert get_dict_transactions(
            os.path.abspath(os.path.join(os.path.dirname(__file__), "../data/operations.json"))
        ) == [
            {
                "id": 441945886,
                "state": "EXECUTED",
                "date": "2019-08-26T10:50:58.294041",
                "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
                "description": "Перевод организации",
                "from": "Maestro 1596837868705199",
                "to": "Счет 64686473678894779589",
            },
            {
                "id": 41428829,
                "state": "EXECUTED",
                "date": "2019-07-03T18:35:29.512364",
                "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
                "description": "Перевод организации",
                "from": "MasterCard 7158300734726758",
                "to": "Счет 35383033474447895560",
            },
        ]


def test_get_dict_transactions_data_not_list() -> None:
    """Тестирование функции, преобразующей json-файл с транзакциями в список при входных данных, отличными от списка"""
    with patch("json.load") as mock_json:
        mock_json.return_value = "not_dict"
        assert (
            get_dict_transactions(os.path.abspath(os.path.join(os.path.dirname(__file__), "../data/operations.json")))
            == []
        )


def test_get_dict_transactions_empty_file() -> None:
    """Тестирование функции, преобразующей json-файл с транзакциями в список при пустом json-файле"""
    with patch("json.load") as mock_json:
        mock_json.return_value = []
        assert (
            get_dict_transactions(os.path.abspath(os.path.join(os.path.dirname(__file__), "../data/operations.json")))
            == []
        )
