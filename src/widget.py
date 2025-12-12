import masks


def mask_account_card(data_card: str) -> str:
    """Функция, маскирующая номер карты и счета"""
    if "Счет" not in data_card:
        list_number_card = data_card.split()
        masks_number_card = masks.get_mask_card_number(int(list_number_card[-1]))
        list_number_card[-1] = masks_number_card
        return " ".join(list_number_card)
    else:
        list_count_card = data_card.split()
        masks_count_card = masks.get_mask_account(int(list_count_card[-1]))
        return f"{list_count_card[0]} {masks_count_card}"


def get_date(card_date: str) -> str:
    """Функция, изменяющая формат вывода даты"""
    return f"{card_date[8:10]}.{card_date[5:7]}.{card_date[:4]}"


card_info = "Счет 64686473678894779589"
date = "2024-03-11T02:26:18.671407"

if __name__ == "__main__":
    print(mask_account_card(card_info))
    get_date(date)
