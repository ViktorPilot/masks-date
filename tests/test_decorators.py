from typing import Any

import pytest

from src.decorators import log


@log()
def my_function(x: Any, y: Any) -> Any:
    """Функция, суммирующая два числа"""
    return x + y


@pytest.mark.parametrize("x, y, result", [(1, 2, "my_function ok\n"), (1.2, 2.3, "my_function ok\n")])
def test_log_positive(capsys, x, y, result):
    """Тестирование работы декоратора при вводе целых чисел и чисел с плавающей запятой"""
    my_function(x, y)
    captured = capsys.readouterr()
    assert captured.out == result


@pytest.mark.parametrize("x, y, result", [("1", 2, "my_function error: TypeError. Inputs: ('1', 2), {}\n"),
                                          (1, "2", "my_function error: TypeError. Inputs: (1, '2'), {}\n"),
                                          ([1, 2], (2, 1),
                                           "my_function error: TypeError. Inputs: ([1, 2], (2, 1)), {}\n")])
def test_log_negative(capsys, x, y, result):
    """Тестирование работы декоратора при вводе аргументов, отличных от целых чисел и чисел с плавающей запятой"""
    my_function(x, y)
    captured = capsys.readouterr()
    assert captured.out == result
