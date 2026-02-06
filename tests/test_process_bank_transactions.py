from src.process_bank_transactions import process_bank_search, process_bank_operations


def test_process_bank_search_valid(pbs_valid: tuple[list[dict], str], result_pbs_valid: list[dict]) -> None:
    """Проверка фильтрации транзакций по заданной категории при стандартных значениях"""
    assert process_bank_search(*pbs_valid) == result_pbs_valid


def test_process_bank_search_empty() -> None:
    """Проверка работы функции, фильтрующей транзакции по заданной категории при пустом списке транзакций"""
    assert process_bank_search([], "Перевод организации") == []


def test_process_bank_search_not_description(pbs_not_description: tuple[list[dict], str]) -> None:
    """Проверка работы функции, фильтрующей транзакции по заданной категории
    при отсутствии описания транзакции 'description'"""
    assert process_bank_search(*pbs_not_description) == []


def test_process_bank_search_description_not_str(pbs_description_not_str: tuple[list[dict], str]) -> None:
    """Проверка работы функции, фильтрующей транзакции по заданной категории
    при типе данных 'description', отличным от str"""
    assert process_bank_search(*pbs_description_not_str) == []


def test_process_bank_operations_valid(pbo_valid: tuple[list[dict], list[str]]) -> None:
    """Проверка работы функции, вычисляющей количество транзакций по заданным категориям
        при стандартных значениях"""
    assert process_bank_operations(*pbo_valid) == {"Перевод организации": 2, "Перевод со счета на счет": 2,
                                                   "Перевод с карты на карту": 1}


def test_process_bank_operations_empty() -> None:
    """Проверка работы функции, вычисляющей количество транзакций по заданным категориям
        при пустом списке транзакций"""
    assert process_bank_operations([], ["Перевод организации", "Перевод с карты на карту"]) == {}


def test_process_bank_operations_not_description(pbo_not_description: tuple[list[dict], list[str]]) -> None:
    """Проверка работы функции, вычисляющей количество транзакций по заданным категориям
       при отсутствии описания транзакций 'description'"""
    assert process_bank_operations(*pbo_not_description) == {}


def test_process_bank_operations_not_operations(pbo_not_operations: tuple[list[dict], list[str]]) -> None:
    """Проверка работы функции, вычисляющей количество транзакций по заданным категориям
        при отсутствии в списке транзакций заданных категорий"""
    assert process_bank_operations(*pbo_not_operations) == {}
