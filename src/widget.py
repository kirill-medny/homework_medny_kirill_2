from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(number_str: str) -> str:
    """Функция принимает строку и маскирует номер карты или счета"""
    if len(number_str.split()[-1]) == 16:
        new_number = get_mask_card_number(number_str.split()[-1])
        result = f"{number_str[:-16]}{new_number}"
    elif len(number_str.split()[-1]) == 20:
        new_number = get_mask_account(number_str.split()[-1])
        result = f"{number_str[:-20]}{new_number}"
    return result


def get_new_data(old_data: str) -> str:
    """Функция принимает строку с датой и форматирует ее"""
    data_slise = old_data[0:10].split("-")
    result = ".".join(data_slise[::-1])
    return result
