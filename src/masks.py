def get_mask_card_number(card_number_: str) -> str:
    """Функция, возвращающая зашифрованный номер карты"""
    if len(card_number_) != 16:
        raise ValueError("Неправильное количество символов номера карты")
    if not isinstance(int(card_number_), int):
        raise ValueError("Неправильный тип символов номера карты")
    first_part_number = card_number_[:4]
    second_part_number = card_number_[4:6]
    end_part_number = card_number_[12:]
    return f"{first_part_number} {second_part_number}** **** {end_part_number}"


def get_mask_account(count_number_: str) -> str:
    """Функция, возвращающая зашифрованный номер счета"""
    if len(count_number_) != 20:
        raise ValueError("Неправильное количество символов номера счета")
    if not isinstance(int(count_number_), int):
        raise ValueError("Неправильный тип символов номера счета")
    return f"**{count_number_[-4:]}"


if __name__ == "__main__":
    get_mask_card_number("1000792289606363")
    get_mask_account("73654108430135874305")
