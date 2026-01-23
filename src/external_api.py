import os

import requests
from dotenv import load_dotenv

load_dotenv()
headers = {"apikey": os.getenv("APIKEY")}


def get_amount_transactions(transaction: dict) -> str | float:
    """Функция, возвращающая сумму транзакции в рублях и обращающаяся к внешнему API для конвертации
    валюты USD и EUR в рубли"""
    if transaction != {} and type(transaction) is dict:
        code = transaction.get("operationAmount", {}).get("currency", {}).get("code", "")
        try:
            amount = float(transaction.get("operationAmount", {}).get("amount"))
        except TypeError:
            print("Отсутствует сумма транзакции")
            return False
        except ValueError:
            print("Неправильный тип данных суммы транзакции")
            return False
        if code == "RUB":
            return amount
        elif code in ["USD", "EUR"]:
            from_ = code
            to = "RUB"
            response = requests.get(
                f"https://api.apilayer.com/exchangerates_data/convert?to={to}&from={from_}&amount={amount}",
                headers=headers,
            )
            if response.status_code == 200:
                amount = float(response.json().get("result"))
                return amount
            else:
                print(f"При конвертации валюты произошла ошибка {response.status_code}")
                return False
        print("В транзакции не указан или указан неверно тип валюты")
        return False
    print("Отсутствуют корректные данные по транзакции")
    return False


if __name__ == "__main__":  # pragma: no cover
    print(
        get_amount_transactions(
            {
                "id": 441945886,
                "state": "EXECUTED",
                "date": "2019-08-26T10:50:58.294041",
                "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
                "description": "Перевод организации",
                "from": "Maestro 1596837868705199",
                "to": "Счет 64686473678894779589",
            }
        )
    )
