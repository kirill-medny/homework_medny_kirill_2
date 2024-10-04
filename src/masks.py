def get_mask_card_number(number: str) -> str:
    """Функция принимает строку и возвращает маску карты"""
    new_string = f"{number[0:4]} {number[4:6]}** **** {number[12:]}"
    return new_string


def get_mask_account(number: str) -> str:
    """Функция принимает строку и возвращает маску счета"""
    new_string = f"**{number[-4::]}"
    return new_string
