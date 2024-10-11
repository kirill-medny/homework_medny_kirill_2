import pytest


@pytest.fixture
def number_str() -> list:
    """Функция передает строку с номером карты или счета для функции mask_account_card"""
    return [
        "Maestro 1596 83** **** 5199",
        "**9589",
        "MasterCard 7158 30** **** 6758",
        "**5560",
        "Visa Classic 6831 98** **** 7658",
        "Visa Platinum 8990 92** **** 5229",
        "Visa Gold 5999 41** **** 6353",
        "**4305",
    ]


@pytest.fixture
def old_data() -> list:
    """Функция передает строку с датой для функции get_new_data"""
    return [
        "11.07.2018",
        "03.07.2019",
        "30.06.2018",
    ]


@pytest.fixture
def card_number() -> list:
    """Функция передает строку с номером карты для функции test_mask_card_number"""
    return [
        "7000 79** **** 6361",
        "7158 30** **** 6758",
        "6831 98** **** 7658",
        "8990 92** **** 5229",
        "5999 41** **** 6353",
    ]


@pytest.fixture
def acc_number() -> list:
    """Функция передает строку с номером счета для функции get_mask_account"""
    return ["**4305", "**9589", "**5560", "**4305"]


@pytest.fixture
def list_dict() -> list:
    """
    Функция которая передает список словарей для функций filter_by_state, sort_by_date
    """
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


@pytest.fixture
def transactions() -> list[dict]:
    """
    Функция которая передает список словарей для функции test_filter_by_currency
    """
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]
