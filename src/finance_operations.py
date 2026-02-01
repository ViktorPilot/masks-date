import csv
import os.path

import pandas as pd


def get_operation_csv(path_to_csv: str) -> list[dict] | str:
    """Функция, считывающая с файла .csv данные по банковским операциям и возвращающая
    список словарей с транзакциями"""
    if os.path.exists(path_to_csv):
        try:
            with open(path_to_csv, "r", encoding="utf-8", newline="") as file:
                reader = csv.DictReader(file, delimiter=";")
                return list(reader)
        except Exception as e:
            return f"Ошибка при чтении файла: {e}"
    else:
        return f"Файл {os.path.basename(path_to_csv)} не найден"


def get_operation_excel(path_to_xlsx: str) -> list[dict] | str:
    """Функция, считывающая с файла .xlsx данные по банковским операциям и возвращающая
    список словарей с транзакциями"""
    if os.path.exists(path_to_xlsx):
        try:
            df = pd.read_excel(path_to_xlsx).to_dict(orient="records")
            return df
        except Exception as e:
            return f"Ошибка при чтении файла: {e}"
    else:
        return f"Файл {os.path.basename(path_to_xlsx)} не найден"


if __name__ == "__main__":
    print(get_operation_csv("../data/transactions.csv"))
    print(get_operation_excel("../data/transactions_excel.xlsx"))
