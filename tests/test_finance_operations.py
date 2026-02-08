import os
from typing import Tuple
from unittest.mock import Mock, patch

from src.finance_operations import PATH_TO_DIR, get_operation_csv, get_operation_excel


@patch("csv.DictReader")
def test_get_operation_csv_valid(mock_dict: Mock, valid_get_operation_csv: Tuple) -> None:
    """Тестирование работы функции, конвертирующей файл с транзакциями .csv в список при стандартных значениях"""
    mock_dict.return_value = valid_get_operation_csv
    assert get_operation_csv(os.path.join(PATH_TO_DIR, "data/transactions.csv")) == [
        {
            "id": "650703",
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": "16210",
            "currency_name": "Sol",
            "currency_code": "PEN",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
            "description": "Перевод организации",
        },
        {
            "id": "3598919",
            "state": "EXECUTED",
            "date": "2020-12-06T23:00:58Z",
            "amount": "29740",
            "currency_name": "Peso",
            "currency_code": "COP",
            "from": "Discover 3172601889670065",
            "to": "Discover 0720428384694643",
            "description": "Перевод с карты на карту",
        },
    ]


@patch("csv.DictReader")
def test_get_operation_csv_empty_list(mock_dict: Mock) -> None:
    """Тестирование работы функции, конвертирующей файл с транзакциями .csv в список при отсутствии транзакций"""
    mock_dict.return_value = {}
    assert get_operation_csv(os.path.join(PATH_TO_DIR, "data/transactions.csv")) == []


@patch("csv.DictReader")
def test_get_operation_csv_not_found(mock_dict: Mock, valid_get_operation_csv: Tuple) -> None:
    """Тестирование работы функции, конвертирующей файл с транзакциями .csv в список
    при отсутствии файла с транзакциями"""
    mock_dict.return_value = valid_get_operation_csv
    assert get_operation_csv(os.path.join(PATH_TO_DIR, "data/trans.csv")) == []


@patch("pandas.read_csv")
def test_get_operation_csv_error(mock_df: Mock, valid_get_operation_csv: Tuple) -> None:
    """Тестирование работы функции, конвертирующей файл с транзакциями .csv в список при ошибке в чтении файла"""
    mock_df.return_value = valid_get_operation_csv
    assert get_operation_csv(os.path.join(PATH_TO_DIR, "data/transactions_excel.xlsx")) == []


@patch("pandas.read_excel")
def test_get_operation_excel_error(mock_df: Mock, valid_get_operation_excel: list[dict]) -> None:
    """Тестирование работы функции, конвертирующей файл с транзакциями .xlsx в список при ошибке в чтении файла"""
    mock_df.return_value = valid_get_operation_excel
    assert get_operation_excel(os.path.join(PATH_TO_DIR, "data/transactions_excel.xlsx")) == []


@patch("pandas.read_excel")
def test_get_operation_excel_not_found(mock_df: Mock, valid_get_operation_excel: list[dict]) -> None:
    """Тестирование работы функции, конвертирующей файл с транзакциями .xlsx в список
    при отсутствии файла с транзакциями"""
    mock_df.return_value = valid_get_operation_excel
    assert get_operation_excel(os.path.join(PATH_TO_DIR, "data/trans_excel.xlsx")) == []


@patch("pandas.read_excel")
def test_get_operation_excel_valid(mock_df: Mock, valid_get_operation_excel: list[dict]) -> None:
    """Тестирование работы функции, конвертирующей файл с транзакциями .xlsx в список при стандартных значениях"""
    mock_df.return_value.fillna.return_value.to_dict.return_value = valid_get_operation_excel
    assert get_operation_excel(os.path.join(PATH_TO_DIR, "data/transactions_excel.xlsx")) == [
        {
            "id": 650703.0,
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": 16210.0,
            "currency_name": "Sol",
            "currency_code": "PEN",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
            "description": "Перевод организации",
        },
        {
            "id": 3598919.0,
            "state": "EXECUTED",
            "date": "2020-12-06T23:00:58Z",
            "amount": 29740.0,
            "currency_name": "Peso",
            "currency_code": "COP",
            "from": "Discover 3172601889670065",
            "to": "Discover 0720428384694643",
            "description": "Перевод с карты на карту",
        },
    ]


@patch("pandas.read_excel")
def test_get_operation_excel_empty(mock_df: Mock) -> None:
    """Тестирование работы функции, конвертирующей файл с транзакциями .xlsx в список при отсутствии транзакций"""
    mock_df.return_value.fillna.return_value.to_dict.return_value = []
    assert get_operation_excel(os.path.join(PATH_TO_DIR, "data/transactions_excel.xlsx")) == []
