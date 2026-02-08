import csv
import logging
import os

import pandas as pd

PATH_TO_DIR = os.path.dirname(os.path.dirname(__file__))
path_to_transactions_csv = os.path.join(PATH_TO_DIR, "data/transactions.csv")
path_to_transactions_excel = os.path.join(PATH_TO_DIR, "data/transactions_excel.xlsx")

logger_fo = logging.getLogger("finance_operations")
logger_fo.setLevel(logging.DEBUG)

file_handler_fo = logging.FileHandler(
    os.path.join(PATH_TO_DIR, "logs/logger_finance_op.log"), encoding="utf-8", mode="w"
)
file_formatter_fo = logging.Formatter("%(asctime)s - %(name)s (функция: %(funcName)s) - %(levelname)s: %(message)s")
file_handler_fo.setFormatter(file_formatter_fo)
logger_fo.addHandler(file_handler_fo)


def get_operation_csv(path_to_csv: str) -> list[dict | None]:
    """Функция, считывающая с файла .csv данные по банковским операциям и возвращающая
    список словарей с транзакциями"""
    logger_fo.info("Начало работы функции...")
    if os.path.exists(path_to_csv):
        try:
            with open(path_to_csv, "r", encoding="utf-8", newline="") as file:
                reader = csv.DictReader(file, delimiter=";")
                logger_fo.info("Файл успешно прочитан.")
                logger_fo.info("Файл успешно конвертирован в список транзакций. Завершение работы функции.")
                return list(reader)
        except Exception as e:
            logger_fo.error(f"Ошибка при чтении файла: {e}. Завершение работы функции.")
            return []
    else:
        logger_fo.error(f"Файл {os.path.basename(path_to_csv)} не найден. Завершение работы функции.")
        return []


def get_operation_excel(path_to_xlsx: str) -> list[dict | None]:
    """Функция, считывающая с файла .xlsx данные по банковским операциям и возвращающая
    список словарей с транзакциями"""
    logger_fo.info("Начало работы функции...")
    if os.path.exists(path_to_xlsx):
        try:
            df = pd.read_excel(path_to_xlsx).fillna("").to_dict(orient="records")
            logger_fo.info("Файл успешно прочитан.")
            logger_fo.info("Файл успешно конвертирован в список транзакций. Завершение работы функции.")
            return list(df)
        except Exception as e:
            logger_fo.error(f"Ошибка при чтении файла: {e}. Завершение работы функции.")
            return []
    else:
        logger_fo.error(f"Файл {os.path.basename(path_to_xlsx)} не найден. Завершение работы функции.")
        return []


if __name__ == "__main__":  # pragma: no cover
    print(get_operation_csv(path_to_transactions_csv))
    print(get_operation_excel(path_to_transactions_excel))
