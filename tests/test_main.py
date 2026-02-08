from unittest.mock import Mock, patch

from main import main


@patch("builtins.input")
def test_main_valid_xlsx(mock_input: Mock, main_valid_xlsx: list[dict]) -> None:
    """Тестирование работы функции при чтении транзакций из xlsx-файла при стандартных условиях"""
    mock_input.side_effect = ["3", "EXECUTED", "да", "по возрастанию", "да", "да", "перевод со счета на счет"]
    assert main() == main_valid_xlsx


@patch("builtins.input")
def test_main_valid_csv(mock_input_1: Mock, main_valid_csv: list[dict]) -> None:
    """Тестирование работы функции при чтении транзакций из csv-файла при стандартных условиях"""
    mock_input_1.side_effect = ["2", "CANCELED", "да", "по убыванию", "да", "да", "перевод организации"]
    assert main() == main_valid_csv


@patch("builtins.input")
def test_main_valid_json(mock_input_2: Mock, main_valid_json: list[dict]) -> None:
    """Тестирование работы функции при чтении транзакций из json-файла при стандартных условиях"""
    mock_input_2.side_effect = ["1", "CANCELED", "да", "по возрастанию", "да", "да", "перевод организации"]
    assert main() == main_valid_json


@patch("builtins.input")
def test_main_valid_empty_result(mock_input_3: Mock, main_valid_json: list[dict]) -> None:
    """Тестирование работы функции при отсутствии транзакций по выбранным статусам"""
    mock_input_3.side_effect = ["1", "PENDING", "да", "по возрастанию", "да", "да", "перевод организации"]
    assert main() == []


@patch("builtins.input")
def test_main_not_first_time(mock_input_1: Mock, main_valid_xlsx: list[dict]) -> None:
    """Тестирование работы функции при первом неверном вводе статусов"""
    mock_input_1.side_effect = [
        "one",
        "4",
        "3",
        "EXECUT",
        "EXECUTED",
        "yes",
        "да",
        "по нарастанию",
        "по возрастанию",
        "no",
        "да",
        "no",
        "да",
        "перевод со счета на счет",
    ]
    assert main() == main_valid_xlsx
