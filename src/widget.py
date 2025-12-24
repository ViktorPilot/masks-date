from src import masks


def mask_account_card(data_card: str) -> str:
    """Функция, маскирующая номер карты и счета"""
    list_data_card = data_card.split()
    if len(list_data_card) <= 1 or not isinstance(int(list_data_card[-1]), int):
        raise ValueError("Неправильный формат или введено пустое значение номера/счета карты")

    if "Счет" not in list_data_card:
        if len(list_data_card[-1]) != 16:
            raise ValueError("Неправильное количество символов номера карты")

        masks_number_card = masks.get_mask_card_number(list_data_card[-1])
        list_data_card[-1] = masks_number_card
        return " ".join(list_data_card)
    else:
        if len(list_data_card[-1]) != 20:
            raise ValueError("Неправильное количество символов счета карты")

        masks_count_card = masks.get_mask_account(list_data_card[-1])
        return f"{list_data_card[0]} {masks_count_card}"


def get_date(card_date: str) -> str:
    """Функция, изменяющая формат вывода даты"""
    if len(card_date) != 26 or not isinstance(int(card_date[:4] + card_date[5:7] + card_date[8:10]), int):
        raise ValueError("Неправильный формат ввода даты")
    if int(card_date[:4]) > 0 and 0 < int(card_date[5:7]) <= 12 and 0 < int(card_date[8:10]) <= 31:
        return f"{card_date[8:10]}.{card_date[5:7]}.{card_date[:4]}"
    else:
        raise ValueError("Неправильный ввод значений даты")


if __name__ == "__main__":
    print(mask_account_card("Счет 64686473678894779589"))
    print(get_date("2024-03-12T02:26:18.671407"))
