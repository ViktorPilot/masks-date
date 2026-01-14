import os.path
from functools import wraps
from typing import Any, Callable


def log(filename: str | None = None) -> Callable:
    """Функция-декоратор, передающая в функцию inner параметр, определяющий
    логирование в консоль или в файл mylog.txt"""

    def wrapper(func: Callable) -> Callable:
        """Функция-обертка передающая логируемую оригинальную функцию в функцию inner"""

        @wraps(func)
        def inner(*args: Any, **kwargs: Any) -> Any:
            """Функция, выводящая в консоль или записывающая в файл mylog.txt лог работы оригинальной функции"""
            try:
                result = func(*args, **kwargs)
                if filename:
                    with open(filename, "a", encoding="UTF-8") as file:
                        file.write(f"{func.__name__} ok\n")
                        return result
                print(f"{func.__name__} ok")
                return result
            except Exception as e:
                if filename:
                    with open(filename, "a", encoding="UTF-8") as file:
                        file.write(f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}\n")
                else:
                    print(f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}")

        return inner

    return wrapper


if __name__ == "__main__":  # pragma: no cover
    path_to_dir = os.path.dirname(__file__)
    path_to_mylog = os.path.join(os.path.dirname(path_to_dir), "mylog.txt")


    @log(filename=path_to_mylog)
    def my_function(x: int | float, y: int | float) -> int | float:
        """Функция, суммирующая два числа"""
        return x + y


    my_function(1, 2)
