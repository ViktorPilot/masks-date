import os.path
from functools import wraps
from typing import Callable, Any


def log(filename: str | None = None) -> Callable:
    """Функция-декоратор, записывающая log в файл или в консоль при вызове функции"""

    def wrapper(func: Callable) -> Callable:
        @wraps(func)
        def inner(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                if filename:
                    with open(filename, "a", encoding="UTF-8") as file:
                        file.write(f"{func.__name__} ok\n")
                        return result
                print(f"{func.__name__} ok\n")
                return result
            except Exception as e:
                if filename:
                    with open(filename, "a", encoding="UTF-8") as file:
                        file.write(f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}\n")
                else:
                    print(f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}\n")

        return inner

    return wrapper


if __name__ == "__main__":
    path_to_dir = os.path.dirname(__file__)
    path_to_mylog = os.path.join(os.path.dirname(path_to_dir), "mylog.txt")


    @log(filename=path_to_mylog)
    def my_function(x: int, y: int) -> int:
        """Функция, суммирующая два числа"""
        return x + y


    my_function(1, 2)
