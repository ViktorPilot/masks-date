import pytest

from src import widget


@pytest.mark.parametrize(
    "data_card, result",
    [
        ("Счет 64686473678894779589", "Счет **9589"),
        ("Счет 00000000000000000000", "Счет **0000"),
        ("Visa Platinum 0000792289606361", "Visa Platinum 0000 79** **** 6361"),
        ("Maestro 7000792289606361", "Maestro 7000 79** **** 6361"),
    ],
)
def test_mask_account_card_positive(data_card: str, result: str) -> None:
    """Проверка работы функции, возвращающей зашифрованный номер карты или счета при стандартных значениях"""
    assert widget.mask_account_card(data_card) == result


@pytest.mark.parametrize(
    "data_card",
    ["Счет 6468647367889", "Счет 000000000000000000001111", "Visa Platinum 00007922", "Maestro 700079228960636111111"],
)
def test_mask_account_card_short_large_num(data_card: str) -> None:
    """Проверка работы функции, вызывающей исключение при вводе номера карты или счета
    с количеством символов отличным от заданных значений"""
    with pytest.raises(ValueError):
        widget.mask_account_card(data_card)


@pytest.fixture
def empty_num() -> str:
    return ""


def test_mask_account_card_empty_num(empty_num: str) -> None:
    """Проверка работы функции, вызывающей исключение при вводе пустой строки"""
    with pytest.raises(ValueError):
        widget.mask_account_card(empty_num)


@pytest.fixture
def only_num() -> str:
    return "64686473678894779589"


def test_mask_account_card_only_num(only_num: str) -> None:
    """Проверка работы функции, вызывающей исключение при вводе номера карты или счета
    без указания типа карты или счета"""
    with pytest.raises(ValueError):
        widget.mask_account_card(only_num)


@pytest.mark.parametrize(
    "data_card",
    [
        "abcdabcdabcdabcd",
        "9999999.99999999",
    ],
)
def test_mask_account_card_not_int(data_card: str) -> None:
    """Проверка работы функции, вызывающей исключение при вводе номера счета со значениями,
    отличными от целого числа"""
    with pytest.raises(ValueError):
        widget.mask_account_card(data_card)


@pytest.mark.parametrize(
    "card_date, result",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2025-01-01T00:00:00.000000", "01.01.2025"),
        ("2027-12-31T02:26:18.671407", "31.12.2027"),
    ],
)
def test_get_date_positive(card_date: str, result: str) -> None:
    """Проверка работы функции, изменяющей формат вывода даты при стандартных значениях"""
    assert widget.get_date(card_date) == result


@pytest.mark.parametrize(
    "card_date",
    [
        "2024-03-32T02:26:18.671407",
        "2024-13-11T02:26:18.671407",
    ],
)
def test_get_date_out_of_range(card_date: str) -> None:
    """Проверка работы функции, вызывающей исключение при вводе значений даты вне диапазона возможных значений"""
    with pytest.raises(ValueError):
        widget.get_date(card_date)


@pytest.mark.parametrize(
    "card_date",
    [
        "three-03-30T02:26:18.671407",
        "2024-aa-11T02:26:18.671407",
    ],
)
def test_get_date_not_int(card_date: str) -> None:
    """Проверка работы функции, вызывающей исключение при вводе даты, отличной от целого числа"""
    with pytest.raises(ValueError):
        widget.get_date(card_date)
