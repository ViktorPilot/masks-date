import csv
import logging
import os.path

import pandas as pd

PATH_TO_DIR = os.path.dirname(os.path.dirname(__file__))
path_to_transactions_csv = os.path.join(PATH_TO_DIR, "data/transactions.csv")
path_to_transactions_excel = os.path.join(PATH_TO_DIR, "data/transactions_excel.xlsx")

logging.basicConfig(
    filename=os.path.join(PATH_TO_DIR, "logs/logger_finance_op.log"),
    filemode="w",
    level=logging.INFO,
    encoding="utf-8",
    format="%(asctime)s - %(name)s (функция: %(funcName)s) - %(levelname)s: %(message)s",
)

logger = logging.getLogger("finance_operations")


def get_operation_csv(path_to_csv: str) -> list[dict]:
    """Функция, считывающая с файла .csv данные по банковским операциям и возвращающая
    список словарей с транзакциями"""
    logger.info("Начало работы функции...")
    if os.path.exists(path_to_csv):
        try:
            with open(path_to_csv, "r", encoding="utf-8", newline="") as file:
                reader = csv.DictReader(file, delimiter=";")
                logger.info("Файл успешно прочитан.")
                logger.info("Файл успешно конвертирован в список транзакций. Завершение работы функции.")
                return list(reader)
        except Exception as e:
            logger.error(f"Ошибка при чтении файла: {e}. Завершение работы функции.")
            return []
    else:
        logger.error(f"Файл {os.path.basename(path_to_csv)} не найден. Завершение работы функции.")
        return []


def get_operation_excel(path_to_xlsx: str) -> list[dict]:
    """Функция, считывающая с файла .xlsx данные по банковским операциям и возвращающая
    список словарей с транзакциями"""
    logger.info("Начало работы функции...")
    if os.path.exists(path_to_xlsx):
        try:
            df = pd.read_excel(path_to_xlsx).to_dict(orient="records")
            logger.info("Файл успешно прочитан.")
            logger.info("Файл успешно конвертирован в список транзакций. Завершение работы функции.")
            return df
        except Exception as e:
            logger.error(f"Ошибка при чтении файла: {e}. Завершение работы функции.")
            return []
    else:
        logger.error(f"Файл {os.path.basename(path_to_xlsx)} не найден. Завершение работы функции.")
        return []


if __name__ == "__main__":  # pragma: no cover
    print(get_operation_csv(path_to_transactions_csv))
    print(get_operation_excel(path_to_transactions_excel))
