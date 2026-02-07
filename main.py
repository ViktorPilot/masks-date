from src.finance_operations import get_operation_csv, path_to_transactions_csv, path_to_transactions_excel, \
    get_operation_excel
from src.process_bank_transactions import process_bank_search
from src.processing import filter_by_state, sort_by_date
from src.utils import get_dict_transactions, path_to_operation
from src.widget import get_date, mask_account_card


def main() -> None:
    """Функция, связывающая функциональность всех модулей продукта"""
    print("Программа: Привет! Добро пожаловать в программу работы с банковскими транзакциями.")

    # Выбор типа файла
    while True:
        try:
            choose_type_file = int(input("""Выберите необходимый пункт меню:
        1. Получить информацию о транзакциях из JSON-файла.
        2. Получить информацию о транзакциях из CSV-файла.
        3. Получить информацию о транзакциях из XLSX-файла.
        Пользователь: """).strip())
        except ValueError:
            print("Программа: Введено не целое число. Введите значение от 1 до 3.")
        else:
            if choose_type_file not in [1, 2, 3]:
                print("Программа: Выбран неверный пункт. Введите значение от 1 до 3.")
            else:
                break
    if choose_type_file == 1:
        print("Программа: Для обработки выбран JSON-файл.")
        type_file = get_dict_transactions(path_to_operation)
    elif choose_type_file == 2:
        print("Программа: Для обработки выбран CSV-файл.")
        type_file = get_operation_csv(path_to_transactions_csv)
    else:
        print("Программа: Для обработки выбран XLSX-файл.")
        type_file = get_operation_excel(path_to_transactions_excel)

    # Выбор статуса для фильтрации
    while True:
        print("""Программа: Введите статус, по которому необходимо выполнить фильтрацию.
        Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING.""")
        choose_type_status = input("Пользователь: ").upper().strip()
        if choose_type_status in ["EXECUTED", "CANCELED", "PENDING"]:
            type_status = filter_by_state(list_of_dict=type_file, state=choose_type_status)
            print(f"Программа: Операции отфильтрованы по статусу {choose_type_status}.")
            break
        else:
            print(f"Программа: Статус операции {choose_type_status} недоступен.")

    # Фильтрация данных по дате
    while True:
        print("Программа: Отсортировать операции по дате? Да/Нет")
        choose_sort_date = input("Пользователь: ").strip().lower()
        if choose_sort_date in ["да", "нет"]:
            break
        else:
            print("Программа: Введен неверный ответ.")

    # Фильтрация данных по возрастанию/убыванию
    while True:
        if choose_sort_date == "да":
            print("Программа: Отсортировать по возрастанию или по убыванию?")
            choose_sort_increase = input("Пользователь: ").strip().lower()
            if choose_sort_increase == "по возрастанию":
                sort_increase = sort_by_date(list_of_dict=type_status, type_sort=False)
                break
            elif choose_sort_increase == "по убыванию":
                sort_increase = sort_by_date(list_of_dict=type_status)
                break
            else:
                print("Программа: Введен неверный ответ.")
        else:
            sort_increase = type_status
            break

    # Фильтрация данных по типу валюты
    while True:
        print("Выводить только рублевые транзакции? Да/Нет")
        choose_sort_currency = input("Пользователь: ").strip().lower()
        if choose_sort_currency == "да":
            if choose_type_file == 1:
                sort_currency = [x for x in sort_increase if
                                 x.get('operationAmount', {}).get('currency', {}).get('code', {}) == 'RUB']
                break
            elif choose_type_file in [2, 3]:
                sort_currency = [x for x in sort_increase if x.get('currency_code') == 'RUB']
                break
        elif choose_sort_currency == "нет":
            sort_currency = sort_increase
            break
        else:
            print("Программа: Введен неверный ответ.")

    # Фильтрация данных по определенному слову в описании
    while True:
        print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
        choose_sort_word = input("Пользователь: ").strip().lower()
        if choose_sort_word == "да":
            print("Введите строку для поиска в описании.")
            user_words = input("Пользователь: ").strip().capitalize()
            sort_word = process_bank_search(data=sort_currency, search=user_words)
            break
        elif choose_sort_word == "нет":
            sort_word = sort_currency
            break
        else:
            print("Программа: Введен неверный ответ.")
    print(sort_word)

    print("Программа: Распечатываю итоговый список транзакций...")

    # Вывод результатов
    if not sort_word:
        print("Программа: Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    else:
        print(f"Всего банковских операций в выборке: {len(sort_word)}\n")
        for transaction in sort_word:
            print(f"{get_date(transaction.get("date", ""))} {transaction.get('description', {})}")
            if choose_type_file == 1:
                if transaction.get("from") and transaction.get("to"):
                    print(f"{mask_account_card(transaction.get("from"))} -> {mask_account_card(transaction.get("to"))}")
                elif transaction.get("from"):
                    print(f"{mask_account_card(transaction.get("from"))}")
                elif transaction.get("to"):
                    print(f"{mask_account_card(transaction.get("to"))}")
                print(
                    f"Сумма: {transaction.get('operationAmount', {}).get('amount', {})} {transaction.get('operationAmount', {}).get('currency', {}).get('name', "")}\n")
            else:
                if transaction.get("from") and transaction.get("to"):
                    print(f"{mask_account_card(transaction.get("from"))} -> {mask_account_card(transaction.get("to"))}")
                elif transaction.get("from"):
                    print(f"{mask_account_card(transaction.get("from"))}")
                elif transaction.get("to"):
                    print(f"{mask_account_card(transaction.get("to"))}")
                print(f"Сумма: {transaction.get('amount', "")} {transaction.get('currency_name', "")}\n")


if __name__ == "__main__":
    main()
