import os
from typing import Any

from src.setup_logger import setup_logger

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path_1 = os.path.join(current_dir, "../logs", "masks.log")
logger = setup_logger("masks", file_path_1)


def get_mask_card_number(card_number: str) -> str:
    """Функция принимает строку и возвращает маску карты"""
    logger.info(f"Задаем формат маски для номера банковской карты {card_number}")
    mask_number = f"{card_number[0:4]} {card_number[4:6]}** **** {card_number[12:]}"
    return mask_number


def get_mask_account(acc_number: str) -> Any:
    """Функция принимает строку и возвращает маску счета"""
    logger.info(f"Проверяем правильность написания {acc_number}")
    if len(str(acc_number)) != 20:
        logger.error("Ошибка. Проверьте длину счета. Он должен содержать 20 символов")
        raise ValueError("Проверьте номер счета. Он должен содержать 20 символов")
    else:
        logger.info(f"Задаем формат маски для номера счета {acc_number}")
        mask_bank_account = f"**{acc_number[-4::]}"
        return mask_bank_account
