import masks


def mask_account_card(data_card: str) -> str:
    if "Счет" not in data_card:
        list_number_card = data_card.split()
        masks_number_card = masks.get_mask_card_number(int(list_number_card[1]))
        return f"{list_number_card[0]} {masks_number_card}"
    else:
        list_count_card = data_card.split()
        masks_count_card = masks.get_mask_account(int(list_count_card[1]))
        return f"{list_count_card[0]} {masks_count_card}"


card_info = "Счет 64686473678894779589"
if __name__ == "__main__":
    print(mask_account_card(card_info))

# Maestro 1596837868705199
# Счет 64686473678894779589
# MasterCard 7158300734726758
# Счет 35383033474447895560
# Visa Classic 6831982476737658
# Visa Platinum 8990922113665229
# Visa Gold 5999414228426353
# Счет 73654108430135874305
