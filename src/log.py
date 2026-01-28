import logging
import os
from typing import Any

PATH_TO_ROOT = os.path.dirname(os.path.dirname(__file__))

if not os.path.exists(os.path.join(PATH_TO_ROOT, "logs")):
    os.makedirs(os.path.join(PATH_TO_ROOT, "logs"))


def create_logger_masks() -> Any:
    """Создание логгера для функции masks"""
    logger_masks = logging.getLogger("masks")
    logger_masks.setLevel(logging.DEBUG)

    file_handler_masks = logging.FileHandler(
        os.path.join(PATH_TO_ROOT, "logs/logger_masks.log"), encoding="utf-8", mode="w"
    )
    file_formatter_masks = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
    file_handler_masks.setFormatter(file_formatter_masks)
    logger_masks.addHandler(file_handler_masks)
    return logger_masks


def create_logger_utils() -> Any:
    """Создание логгера для функции utils"""
    logger_utils = logging.getLogger("utils")
    logger_utils.setLevel(logging.DEBUG)

    file_handler_utils = logging.FileHandler(
        os.path.join(PATH_TO_ROOT, "logs/logger_utils.log"), encoding="utf-8", mode="w"
    )
    file_formatter_utils = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
    file_handler_utils.setFormatter(file_formatter_utils)
    logger_utils.addHandler(file_handler_utils)
    return logger_utils
