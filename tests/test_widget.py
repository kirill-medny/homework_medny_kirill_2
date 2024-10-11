import pytest

from src.widget import get_new_data, mask_account_card


@pytest.mark.parametrize(
    "number_str, result",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Счет 35383033474447895560", "Счет **5560"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
        ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
        ("Счет 73654108430135874305", "Счет **4305"),
    ],
)
def test_mask_account_card(number_str: str, result: str) -> None:
    """Функция передает строку с номером карты или счета"""
    assert mask_account_card(number_str) == result


@pytest.mark.parametrize(
    "old_data, result",
    [
        ("2018-07-11T02:26:18.671407", "11.07.2018"),
        ("2019-07-03T18:35:29.512364", "03.07.2019"),
        ("2018-06-30T02:08:58.4255722", "30.06.2018"),
    ],
)
def test_get_new_data(old_data: str, result: str) -> None:
    """Функция передает строку с датой"""
    assert get_new_data(old_data) == result
