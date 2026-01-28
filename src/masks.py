import logging
import os

PATH_TO_ROOT = os.path.dirname(os.path.dirname(__file__))

if not os.path.exists(os.path.join(PATH_TO_ROOT, "logs")):
    os.makedirs(os.path.join(PATH_TO_ROOT, "logs"))
logger_masks = logging.getLogger("masks")
logger_masks.setLevel(logging.DEBUG)

file_handler_masks = logging.FileHandler(
    os.path.join(PATH_TO_ROOT, "logs/logger_masks.log"), encoding="utf-8", mode="w"
)
file_formatter_masks = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler_masks.setFormatter(file_formatter_masks)
logger_masks.addHandler(file_handler_masks)


def get_mask_card_number(card_number_: str) -> str:
    """Функция, возвращающая зашифрованный номер карты"""
    logger_masks.info("Начало работы программы шифрования номера карты...")
    if len(card_number_) != 16:
        logger_masks.error("Ошибка: неправильное количество символов номера карты. Завершение работы программы.")
        raise ValueError("Неправильное количество символов номера карты")
    if not isinstance(int(card_number_), int):
        logger_masks.error("Ошибка: неправильный тип символов номера карты. Завершение работы программы.")
        raise ValueError("Неправильный тип символов номера карты")
    logger_masks.info("Получен зашифрованный номер карты. Завершение работы программы.")
    return f"{card_number_[:4]} {card_number_[4:6]}** **** {card_number_[12:]}"


def get_mask_account(count_number_: str) -> str:
    logger_masks.info("Начало работы программы шифрования номера счета...")
    """Функция, возвращающая зашифрованный номер счета"""
    if len(count_number_) != 20:
        logger_masks.error("Ошибка: неправильное количество символов номера счета. Завершение работы программы.")
        raise ValueError("Неправильное количество символов номера счета")
    if not isinstance(int(count_number_), int):
        logger_masks.error("Ошибка: неправильный тип символов номера счета. Завершение работы программы.")
        raise ValueError("Неправильный тип символов номера счета")
    logger_masks.info("Получен зашифрованный номер счета. Завершение работы программы.")
    return f"**{count_number_[-4:]}"


if __name__ == "__main__":  # pragma: no cover
    get_mask_card_number("1000792289606363")
    get_mask_account("73654108430135874305")
