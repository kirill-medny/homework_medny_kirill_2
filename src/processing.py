def filter_by_state(list_dict: list, state: str = "EXECUTED") -> list:
    """Функция которая принимает список словарей по ключу state
    и возвращает список словарей, содержащих данный ключ"""
    filter_list = []
    for i in list_dict:
        if i.get("state") == state:
            filter_list.append(i)
    return filter_list


def sort_by_date(list_dict: list, direction: bool = True) -> list:
    """Функция сортирует словари по дате"""
    sorted_list_by_date = sorted(list_dict, key=lambda x: x["date"], reverse=direction)
    return sorted_list_by_date
