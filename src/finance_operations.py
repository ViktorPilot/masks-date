import csv
import logging
import os.path

import pandas as pd

PATH_TO_DIR = os.path.dirname(os.path.dirname(__file__))

logging.basicConfig(filename=os.path.join(PATH_TO_DIR, "logs/logger_finance_op.log"), filemode="w",
                    level=logging.INFO, encoding="utf-8",
                    format="%(asctime)s - %(name)s (функция: %(funcName)s) - %(levelname)s: %(message)s")

logger_csv = logging.getLogger("finance_operations_csv")


def get_operation_csv(path_to_csv: str) -> list[dict]:
    """Функция, считывающая с файла .csv данные по банковским операциям и возвращающая
    список словарей с транзакциями"""
    logger_csv.info("Начало работы функции...")
    if os.path.exists(path_to_csv):
        try:
            with open(path_to_csv, "r", encoding="utf-8", newline="") as file:
                reader = csv.DictReader(file, delimiter=";")
                return list(reader)
        except Exception as e:
            print(f"Ошибка при чтении файла: {e}")
            return []
    else:
        print(f"Файл {os.path.basename(path_to_csv)} не найден")
        return []


def get_operation_excel(path_to_xlsx: str) -> list[dict]:
    """Функция, считывающая с файла .xlsx данные по банковским операциям и возвращающая
    список словарей с транзакциями"""
    if os.path.exists(path_to_xlsx):
        try:
            df = pd.read_excel(path_to_xlsx).to_dict(orient="records")
            return df
        except Exception as e:
            print(f"Ошибка при чтении файла: {e}")
            return []
    else:
        print(f"Файл {os.path.basename(path_to_xlsx)} не найден")
        return []


if __name__ == "__main__":  # pragma: no cover
    print(get_operation_csv(os.path.join(PATH_TO_DIR, "data/transactions.csv")))
    print(get_operation_excel(os.path.join(PATH_TO_DIR, "data/transactions_excel.xlsx")))
