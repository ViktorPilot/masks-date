def get_mask_card_number(card_number_: int) -> str:
    """Функция, возвращающая зашифрованный номер карты"""
    first_part_number = str(card_number_)[:4]
    second_part_number = str(card_number_)[4:6]
    end_part_number = str(card_number_)[12:]
    return f"{first_part_number} {second_part_number}** **** {end_part_number}"


def get_mask_account(count_number_: int) -> str:
    """Функция, возвращающая зашифрованный номер счета"""
    return f"**{str(count_number_)[-4:]}"


if __name__ == "__main__":
    card_number = 7000792289606361
    count_number = 73654108430135874305
    get_mask_card_number(card_number)
    get_mask_account(count_number)
