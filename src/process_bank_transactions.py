import collections
import logging
import os
import re

PATH_TO_DIR = os.path.dirname(os.path.dirname(__file__))

PATH_TO_LOGGER = os.path.join(PATH_TO_DIR, "logs/logger_process.log")

logging.basicConfig(
    filename=PATH_TO_LOGGER,
    filemode="w",
    format="%(asctime)s - %(name)s (функция: %(funcName)s) - %(levelname)s: %(message)s",
    level=logging.INFO,
    encoding="utf-8",
)
logger = logging.getLogger("process_bank_transactions")


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    """Функция, фильтрующая список транзакций по описанию категории"""
    logger.info("Начало работы функции..")
    list_filtred = []
    logger.info("Создание списка отфильтрованных транзакций.")
    for operation in data:
        value_decription = operation.get("description", "")
        if type(value_decription) is str:
            result = re.search(search, value_decription)
            if result:
                list_filtred.append(operation)
        else:
            logger.error(f"Транзакция id: {operation.get('id', '')}. Тип данных 'description' отличается от строки.")
            continue
    logger.info("Список отфильтрованных транзакций создан. Завершение работы функции.")
    return list_filtred


def process_bank_operations(data: list[dict], categories: list) -> dict:
    """Функция, вычисляющая количество транзакций по заданным категориям"""
    logger.info("Начало работы функции..")
    list_filtred_cat = [
        operation.get("description", "") for operation in data if operation.get("description", "") in categories
    ]
    logger.info("Список с категориями всех проведенных транзакций создан.")
    counter = collections.Counter(list_filtred_cat)
    logger.info("Выполнен подсчет категорий транзакций. Завершение работы функции.")
    return dict(counter)


if __name__ == "__main__":  # pragma: no cover
    print(
        process_bank_search(
            [
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                    "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод организации",
                    "from": "Счет 75106830613657916952",
                    "to": "Счет 11776614605963066702",
                },
                {
                    "id": 142264268,
                    "state": "EXECUTED",
                    "date": "2019-04-04T23:20:05.206878",
                    "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод со счета на счет",
                    "from": "Счет 19708645243227258542",
                    "to": "Счет 75651667383060284188",
                },
                {
                    "id": 873106923,
                    "state": "EXECUTED",
                    "date": "2019-03-23T01:09:46.296404",
                    "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
                    "description": "Перевод со счета на счет",
                    "from": "Счет 44812258784861134719",
                    "to": "Счет 74489636417521191160",
                },
                {
                    "id": 895315941,
                    "state": "EXECUTED",
                    "date": "2018-08-19T04:27:37.904916",
                    "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод с карты на карту",
                    "from": "Visa Classic 6831982476737658",
                    "to": "Visa Platinum 8990922113665229",
                },
                {
                    "id": 594226727,
                    "state": "CANCELED",
                    "date": "2018-09-12T21:27:25.241689",
                    "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
                    "description": "Перевод организации",
                    "from": "Visa Platinum 1246377376343588",
                    "to": "Счет 14211924144426031657",
                },
            ],
            "Перевод организации",
        )
    )

    print(
        process_bank_operations(
            [
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                    "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод организации",
                    "from": "Счет 75106830613657916952",
                    "to": "Счет 11776614605963066702",
                },
                {
                    "id": 142264268,
                    "state": "EXECUTED",
                    "date": "2019-04-04T23:20:05.206878",
                    "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод со счета на счет",
                    "from": "Счет 19708645243227258542",
                    "to": "Счет 75651667383060284188",
                },
                {
                    "id": 873106923,
                    "state": "EXECUTED",
                    "date": "2019-03-23T01:09:46.296404",
                    "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
                    "description": "Перевод со счета на счет",
                    "from": "Счет 44812258784861134719",
                    "to": "Счет 74489636417521191160",
                },
                {
                    "id": 895315941,
                    "state": "EXECUTED",
                    "date": "2018-08-19T04:27:37.904916",
                    "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод с карты на карту",
                    "from": "Visa Classic 6831982476737658",
                    "to": "Visa Platinum 8990922113665229",
                },
                {
                    "id": 594226727,
                    "state": "CANCELED",
                    "date": "2018-09-12T21:27:25.241689",
                    "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
                    "description": "Перевод организации",
                    "from": "Visa Platinum 1246377376343588",
                    "to": "Счет 14211924144426031657",
                },
            ],
            ["Перевод организации", "Перевод с карты на карту", "Перевод со счета на счет"],
        )
    )
