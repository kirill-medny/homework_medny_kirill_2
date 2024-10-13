def get_mask_card_number(card_number: str) -> str:
    """Функция принимает строку и возвращает маску карты"""
    mask_number = f"{card_number[0:4]} {card_number[4:6]}** **** {card_number[12:]}"
    return mask_number


def get_mask_account(acc_number: str) -> str:
    """Функция принимает строку и возвращает маску счета"""
    mask_bank_account = f"**{acc_number[-4::]}"
    return mask_bank_account
