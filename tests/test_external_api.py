import unittest
from unittest.mock import patch

from src.external_api import get_amount_transactions


def test_get_amount_transactions_get_rub(get_amount_transactions_rub: dict) -> None:
    """Тестирование функции при транзакции в рублях"""
    assert get_amount_transactions(get_amount_transactions_rub) == 31957.58


def test_get_amount_transactions_not_amount(not_amount: dict) -> None:
    """Тестирование функции при отсутствии суммы транзакции"""
    assert not get_amount_transactions(not_amount)


def test_get_amount_transactions_invalid_type_amount(invalid_type_amount: dict) -> None:
    """Тестирование функции с неправильным типом данных суммы транзакции"""
    assert not get_amount_transactions(invalid_type_amount)


def test_get_amount_transactions_invalid_code_currency(invalid_code_currency: dict) -> None:
    """Тестирование функции с кодом валюты, отличным от USD, EUR, RUB"""
    assert not get_amount_transactions(invalid_code_currency)


def test_get_amount_transactions_not_list_and_empty_dict() -> None:
    """Тестирование функции с пустым словарем"""
    assert not get_amount_transactions({})


@patch("requests.get")
def test_get_amount_transactions_usd(mock_requests: unittest.mock.Mock, get_amount_transactions_usd: dict) -> None:
    """Тестирование функции при транзакции в USD"""
    mock_requests.return_value.status_code = 200
    mock_requests.return_value.json.return_value.get.return_value = 100.58
    assert get_amount_transactions(get_amount_transactions_usd) == 100.58


@patch("requests.get")
def test_get_amount_transactions_stat_code_not_200(
    mock_requests: unittest.mock.Mock, get_amount_transactions_usd: dict
) -> None:
    """Тестирование функции при ошибках, связанных с запросом на сервер"""
    mock_requests.return_value.status_code = 300
    assert not get_amount_transactions(get_amount_transactions_usd)
