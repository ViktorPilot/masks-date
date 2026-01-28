import json
import os

from src.log import create_logger_utils

logger_utils = create_logger_utils()


def get_dict_transactions(path_to_operations: str) -> list[None | dict]:
    """Функция, преобразующая json-файл с транзакциями в список"""
    logger_utils.info("Начало работы программы...")
    try:
        with open(path_to_operations, "r", encoding="utf-8") as file:
            list_operations = json.load(file)
            logger_utils.info(f"Данные успешно загружены из файла {os.path.basename(path_to_operations)}.")
            if type(list_operations) is not list:
                logger_utils.info("Тип данных не является списком транзакций")
                list_operations = []
    except (json.JSONDecodeError, FileNotFoundError):
        list_operations = []
        logger_utils.error(f"Файл не найден или ошибка чтения файла {os.path.basename(path_to_operations)}.")
    logger_utils.info("Завершение работы программы.")
    return list_operations


if __name__ == "__main__":  # pragma: no cover
    print(get_dict_transactions(os.path.abspath(os.path.join(os.path.dirname(__file__), "../data/operations.json"))))
