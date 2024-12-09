from src.processing import filter_by_rub_cvs_xlsx, filter_by_rub_json, filter_by_state, find_transactions, sort_by_date
from src.utils import read_file
from src.widget import get_new_data, mask_account_card


def main() -> None:
    """Отвечает за основную логику проекта и связывает функции между собой"""
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    choice = input("Пользователь: ")
    transactions_data = []
    match choice:
        case "1":
            print("Для обработки выбран JSON-файл.")
            transactions_data = read_file("data/operations.json")
        case "2":
            print("Для обработки выбран CSV-файл.")
            transactions_data = read_file("data/transactions.csv")
        case "3":
            print("Для обработки выбран XLSX-файл.")
            transactions_data = read_file("data/transactions_excel.xlsx")

    while True:
        status = input(
            "Введите статус, по которому необходимо выполнить фильтрацию. "
            "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\nПользователь: "
        )
        if status.upper() in ["EXECUTED", "CANCELED", "PENDING"]:
            print(f'Операции отфильтрованы по статусу "{status.upper()}"')
            filtered_transactions = filter_by_state(transactions_data, status)
            break
        else:
            print(f'Статус операции "{status}" недоступен.')

    if not filtered_transactions:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")
        return

        # Сортировка списка транзакций по дате, если пользователь выбрал этот критерий.
    do_sort_by_date = 0
    user_input = input("Отсортировать операции по дате? Да/Нет\n>>>$: ")
    if user_input.lower() == "да":
        do_sort_by_date = 1
        user_input = input("Отсортировать по возрастанию (нажмите 0) или по убыванию (нажмите 1)?\n>>>$: ")
        if user_input.lower() == "по возрастанию":
            sorting_order = 0
        else:
            sorting_order = 1
        if do_sort_by_date:
            transactions_data = sort_by_date(transactions_data, sorting_order)

    user_input = input("Выводить только рублевые транзакции? Да/Нет\n>>>$: ")
    if user_input.lower() == "да":
        if choice == "1":
            transactions_data = filter_by_rub_json(transactions_data)
        else:
            transactions_data = filter_by_rub_cvs_xlsx(transactions_data)

    do_filter_by_description = 0
    user_input = input("Отфильтровать список транзакций по описанию? Да/Нет\n>>>$: ")
    if user_input.lower() == "да":
        do_filter_by_description = 1

    if do_filter_by_description:
        user_input = input(
            "Какие именно операции отразить в списке транзакций?"
            "(доступно: Перевод с карты на карту, Перевод организации, Открытие вклада\n>>>$:  "
        )
        transactions_data = find_transactions(transactions_data, user_input)

    if not transactions_data:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")

    print("Распечатываю итоговый список транзакций...")
    print(f"Всего банковских операций в выборке: {len(filtered_transactions)}")

    for transaction in transactions_data:
        if isinstance(transaction, dict):  # Проверка, является ли элемент словарем
            date = transaction.get("date")
            description = transaction.get("description")
            from_account = transaction.get("from")
            to_account = transaction.get("to")
            operation_amount = transaction.get("operationAmount")
            amount = transaction.get("amount")
            currency_name = transaction.get("currency_name")

            if date and description and to_account and from_account:  # Проверка на наличие необходимых ключей
                print(f"{get_new_data(date)} {description}")
                print(f"{mask_account_card(from_account)} -> {mask_account_card(to_account)}")
                if choice == "1":
                    if (
                        operation_amount
                        and isinstance(operation_amount, dict)
                        and "amount" in operation_amount
                        and "currency" in operation_amount
                        and isinstance(operation_amount["currency"], dict)
                        and "name" in operation_amount["currency"]
                    ):  # Многоуровневая проверка
                        print(f"{operation_amount['amount']} {operation_amount['currency']['name']}\n")
                    else:
                        print("Ошибка: Отсутствуют данные о сумме операции.")
                else:
                    if amount and currency_name:
                        print(f"Сумма: {amount} {currency_name}\n")
                    else:
                        print("Ошибка: Отсутствуют данные о сумме.")
            else:
                print("Ошибка: В транзакции отсутствуют необходимые данные (date, description, to).")
        else:
            print("Ошибка: Элемент transactions_data не является словарем.")


if __name__ == "__main__":
    main()
