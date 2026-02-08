import logging
import os
from logging import getLogger

from src.finance_operations import (get_operation_csv, get_operation_excel, path_to_transactions_csv,
                                    path_to_transactions_excel)
from src.process_bank_transactions import process_bank_search
from src.processing import filter_by_state, sort_by_date
from src.utils import get_dict_transactions, path_to_operation
from src.widget import get_date, mask_account_card

if not os.path.exists("logs"):
    os.makedirs("logs")

logger_main = getLogger("main")

logger_main.setLevel("INFO")
handler_main = logging.FileHandler("logs/logger_main.log", encoding="utf-8", mode="w")
formatter_main = logging.Formatter("%(asctime)s - %(name)s (функция: %(funcName)s) - %(levelname)s: %(message)s")
handler_main.setFormatter(formatter_main)
logger_main.addHandler(handler_main)


def main() -> list[dict]:
    """Функция, связывающая функциональность всех модулей продукта"""
    logger_main.info("Начало работы программы...")
    print("Программа: Привет! Добро пожаловать в программу работы с банковскими транзакциями.")

    # Выбор типа файла
    while True:
        try:
            choose_type_file = int(
                input(
                    """Выберите необходимый пункт меню:
        1. Получить информацию о транзакциях из JSON-файла.
        2. Получить информацию о транзакциях из CSV-файла.
        3. Получить информацию о транзакциях из XLSX-файла.
        Пользователь: """
                ).strip()
            )
        except ValueError:
            print("Программа: Введено не целое число. Введите значение от 1 до 3.")
            logger_main.error("Введено не целое число.")
        else:
            if choose_type_file not in [1, 2, 3]:
                print("Программа: Выбран неверный пункт. Введите значение от 1 до 3.")
                logger_main.error("Выбран неверный пункт.")
            else:
                break
    if choose_type_file == 1:
        print("Программа: Для обработки выбран JSON-файл.")
        type_file = get_dict_transactions(path_to_operation)
        logger_main.info("Для обработки выбран JSON-файл.")
    elif choose_type_file == 2:
        print("Программа: Для обработки выбран CSV-файл.")
        type_file = get_operation_csv(path_to_transactions_csv)
        logger_main.info("Для обработки выбран CSV-файл.")
    else:
        print("Программа: Для обработки выбран XLSX-файл.")
        type_file = get_operation_excel(path_to_transactions_excel)
        logger_main.info("Для обработки выбран XLSX-файл.")

    # Выбор статуса для фильтрации
    while True:
        print(
            """Программа: Введите статус, по которому необходимо выполнить фильтрацию.
        Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING."""
        )
        choose_type_status = input("Пользователь: ").upper().strip()
        if choose_type_status in ["EXECUTED", "CANCELED", "PENDING"]:
            type_status = filter_by_state(list_of_dict=type_file, state=choose_type_status)
            print(f"Программа: Операции отфильтрованы по статусу {choose_type_status}.")
            logger_main.info(f"Выбран статус для фильтрации транзакций: {choose_type_status}.")
            break
        else:
            print(f"Программа: Статус операции {choose_type_status} недоступен.")
            logger_main.error(f"Статус операции {choose_type_status} недоступен.")

    # Фильтрация транзакций по дате
    while True:
        print("Программа: Отсортировать операции по дате? Да/Нет")
        choose_sort_date = input("Пользователь: ").strip().lower()
        if choose_sort_date in ["да", "нет"]:
            break
        else:
            print("Программа: Введен неверный ответ.")
            logger_main.error("Введен неверный статус для фильтрации транзакций по дате.")

    # Фильтрация транзакций по возрастанию/убыванию даты
    while True:
        if choose_sort_date == "да":
            print("Программа: Отсортировать по возрастанию или по убыванию?")
            choose_sort_increase = input("Пользователь: ").strip().lower()
            if choose_sort_increase == "по возрастанию":
                sort_increase = sort_by_date(list_of_dict=type_status, type_sort=False)
                logger_main.info("Данные по транзакциям отсортированы по возрастанию даты проведения.")
                break
            elif choose_sort_increase == "по убыванию":
                sort_increase = sort_by_date(list_of_dict=type_status)
                logger_main.info("Данные по транзакциям отсортированы по убыванию даты проведения.")
                break
            else:
                print("Программа: Введен неверный ответ.")
                logger_main.error("Введен неверный статус для сортировки транзакций по возрастанию/убыванию даты.")
        else:
            sort_increase = type_status
            logger_main.info("Данные по транзакциям не отсортированы по возрастанию/убыванию даты.")
            break

    # Фильтрация транзакций по типу валюты
    while True:
        print("Выводить только рублевые транзакции? Да/Нет")
        choose_sort_currency = input("Пользователь: ").strip().lower()
        if choose_sort_currency == "да":
            logger_main.info("Для вывода выбраны только рублевые транзакции.")
            if choose_type_file == 1:
                sort_currency = [
                    x
                    for x in sort_increase
                    if x.get("operationAmount", {}).get("currency", {}).get("code", {}) == "RUB"
                ]
                break
            elif choose_type_file in [2, 3]:
                sort_currency = [x for x in sort_increase if x.get("currency_code") == "RUB"]
                break
        elif choose_sort_currency == "нет":
            sort_currency = sort_increase
            logger_main.info("Для вывода выбраны транзакции независимо от типа валюты.")
            break
        else:
            print("Программа: Введен неверный ответ.")
            logger_main.error("Введен неверный статус для фильтрации транзакций по типу валюты.")

    # Фильтрация транзакций по определенному слову в описании
    while True:
        print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
        choose_sort_word = input("Пользователь: ").strip().lower()
        if choose_sort_word == "да":
            print("Введите строку для поиска в описании.")
            user_words = input("Пользователь: ").strip().capitalize()
            sort_word = process_bank_search(data=sort_currency, search=user_words)
            logger_main.info(f"Данные по транзакциям отфильтрованы по слову в описании '{user_words}'.")
            break
        elif choose_sort_word == "нет":
            sort_word = sort_currency
            logger_main.info("Данные по транзакциям не отфильтрованы по определенному слову в описании.")
            break
        else:
            print("Программа: Введен неверный ответ.")
            logger_main.error("Введен неверный статус для фильтрации транзакций по определенному слову в описании.")

    print("Программа: Распечатываю итоговый список транзакций...")

    # Вывод результатов
    if not sort_word:
        print("Программа: Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        logger_main.info("Не найдено ни одной транзакции, подходящей под условия фильтрации.")
    else:
        print(f"Всего банковских операций в выборке: {len(sort_word)}\n")
        for transaction in sort_word:
            print(f"{get_date(transaction.get("date", ""))} {transaction.get('description', {})}")
            if choose_type_file == 1:
                if transaction.get("from") and transaction.get("to"):
                    print(
                        f"{mask_account_card(transaction.get("from", ""))} "
                        f"-> {mask_account_card(transaction.get("to", ""))}"
                    )
                elif transaction.get("from"):
                    print(f"{mask_account_card(transaction.get("from", ""))}")
                elif transaction.get("to"):
                    print(f"{mask_account_card(transaction.get("to", ""))}")
                print(
                    f"Сумма: {transaction.get('operationAmount', {}).get('amount', {})}"
                    f" {transaction.get('operationAmount', {}).get('currency', {}).get('name', "")}\n"
                )
            else:
                if transaction.get("from") and transaction.get("to"):
                    print(
                        f"{mask_account_card(transaction.get("from", ""))} "
                        f"-> {mask_account_card(transaction.get("to", ""))}"
                    )
                elif transaction.get("from"):
                    print(f"{mask_account_card(transaction.get("from", ""))}")
                elif transaction.get("to"):
                    print(f"{mask_account_card(transaction.get("to", ""))}")
                print(f"Сумма: {transaction.get('amount', "")} {transaction.get('currency_name', "")}\n")
        logger_main.info("Список транзакций по заданным статусам сформирован.")
    logger_main.info("Завершение работы программы.")
    return sort_word


if __name__ == "__main__":  # pragma: no cover
    print(main())
