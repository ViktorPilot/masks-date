import os
from typing import Any

import pytest

from src.decorators import log

path_to_dir = os.path.dirname(__file__)
path_to_mylog = os.path.join(os.path.dirname(path_to_dir), "mylog.txt")


@log()
def my_function(x: Any, y: Any) -> Any:
    """Функция, суммирующая два числа"""
    return x + y


@pytest.mark.parametrize("x, y, result", [(1, 2, "my_function ok\n"), (1.2, 2.3, "my_function ok\n")])
def test_log_positive(capsys, x, y, result):
    """Тестирование работы декоратора при вводе целых чисел и чисел с плавающей запятой с выводом лога в консоль"""
    my_function(x, y)
    captured = capsys.readouterr()
    assert captured.out == result


@pytest.mark.parametrize("x, y, result", [("1", 2, "my_function error: TypeError. Inputs: ('1', 2), {}\n"),
                                          (1, "2", "my_function error: TypeError. Inputs: (1, '2'), {}\n"),
                                          ([1, 2], (2, 1),
                                           "my_function error: TypeError. Inputs: ([1, 2], (2, 1)), {}\n")])
def test_log_negative(capsys, x, y, result):
    """Тестирование работы декоратора при вводе аргументов, отличных от целых чисел и чисел с плавающей запятой с выводом лога в консоль"""
    my_function(x, y)
    captured = capsys.readouterr()
    assert captured.out == result


@log(filename=path_to_mylog)
def my_function_2(x: Any, y: Any) -> Any:
    """Функция, суммирующая два числа"""
    return x + y


@pytest.mark.parametrize("x, y, result", [(1, 2, "my_function_2 ok\n"), (1.2, 2.3, "my_function_2 ok\n")])
def test_log_positive_to_mylog(x, y, result):
    """Тестирование работы декоратора при вводе целых чисел и чисел с плавающей запятой с выводом лога в файл mylog.txt"""
    my_function_2(x, y)
    with open(path_to_mylog, "r", encoding="UTF-8") as file:
        log_in_mylog = file.readlines()
        last_str = log_in_mylog[-1]
    assert last_str == result

    log_in_mylog.pop()
    with open(path_to_mylog, "w", encoding="UTF-8") as file:
        file.writelines(log_in_mylog)
