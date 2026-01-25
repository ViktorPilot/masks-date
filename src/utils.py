import json
import os


def get_dict_transactions(path_to_operations: str) -> list[None | dict]:
    """Функция, преобразующая json-файл с транзакциями в список"""
    try:
        with open(path_to_operations, "r", encoding="utf-8") as file:
            list_operations = json.load(file)
            if type(list_operations) is not list:
                list_operations = []
    except (json.JSONDecodeError, FileNotFoundError):
        list_operations = []

    return list_operations


if __name__ == "__main__":  # pragma: no cover
    print(get_dict_transactions(os.path.abspath(os.path.join(os.path.dirname(__file__), "../data/operations.json"))))
