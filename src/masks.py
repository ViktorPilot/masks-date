def get_mask_card_number(card_number: int) -> str:
    """Функция, возвращающая зашифрованный номер карты"""
    first_part_number = str(card_number)[:4]
    second_part_number = str(card_number)[4:6]
    end_part_number = str(card_number)[12:]
    return f"{first_part_number} {second_part_number}** **** {end_part_number}"


def get_mask_account(count_number: int) -> str:
    """Функция, возвращающая зашифрованный номер счета"""
    return f"**{str(count_number)[-4:]}"


card_number = 7000792289606361
count_number = 73654108430135874305

if __name__ == "__main__":
    print(get_mask_card_number(card_number))
    print(get_mask_account(count_number))
