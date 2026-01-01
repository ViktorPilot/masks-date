import pytest
from src import generators


@pytest.mark.parametrize("type_currency, result", [("USD", [
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {
            "amount": "79114.93",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188"
    }
]), ("RUB", [
    {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {
            "amount": "43318.34",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160"
    },
    {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {
            "amount": "67314.70",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657"
    }
])])
def test_filter_by_currency(usual_transactions, type_currency, result):
    assert list(generators.filter_by_currency(usual_transactions, type_currency)) == result


def test_filter_by_currency_not_need_code(not_need_code):
    assert list(generators.filter_by_currency(not_need_code, type_currency="RUB")) == []


def test_filter_by_currency_empty_list_rub():
    assert list(generators.filter_by_currency([], type_currency="RUB")) == []


def test_filter_by_currency_empty_list_usd():
    assert list(generators.filter_by_currency([], type_currency="USD")) == []


def test_filter_by_currency_not_operations_usd(not_operations_usd):
    assert list(generators.filter_by_currency(not_operations_usd, type_currency="USD")) == []


def test_transaction_descriptions_1(one_operation):
    i = (generators.transaction_descriptions(one_operation))
    assert next(i) == "Перевод организации"


def test_transaction_descriptions_2(not_operations_usd):
    i = (generators.transaction_descriptions(not_operations_usd))
    assert next(i) == "Перевод организации"
    assert next(i) == "Перевод со счета на счет"


def test_transaction_descriptions_3(usual_transactions):
    i = (generators.transaction_descriptions(usual_transactions))
    assert next(i) == "Перевод организации"
    assert next(i) == "Перевод со счета на счет"
    assert next(i) == "Перевод со счета на счет"
    assert next(i) == "Перевод с карты на карту"
    assert next(i) == "Перевод организации"


@pytest.mark.parametrize("result", [["Перевод организации",
                                     "Перевод со счета на счет",
                                     "Перевод со счета на счет",
                                     "Перевод с карты на карту",
                                     "Перевод организации"]])
def test_transaction_descriptions_4(usual_transactions, result):
    assert list(generators.transaction_descriptions(usual_transactions)) == result


def test_transaction_descriptions_5():
    assert list(generators.transaction_descriptions([])) == []
