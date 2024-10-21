import requests
from typing import Dict, Any


def get_exchange_rate(currency: str) -> float:
    """Получает текущий курс валюты к рублю."""
    api_key = 'YOUR_API_KEY'  # Замените на ваш API ключ url = f'https://api.apilayer.com/exchangerates_data/latest?base=RUB&symbols={currency}'

    headers = {
        'apikey': api_key
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data['rates'].get(currency, 0.0)
    else:
        print(f"Error fetching exchange rate: {response.status_code}")
        return 0.0


def calculate_transaction_amount(transaction: Dict[str, Any]) -> float:
    """Возвращает сумму транзакции в рублях."""
    amount = transaction.get('amount', 0.0)
    currency = transaction.get('currency', 'RUB').upper()  # По умолчанию считаем, что валюта - рубли

    if currency == 'RUB':
        return float(amount)
    elif currency in ['USD', 'EUR']:
        exchange_rate = get_exchange_rate(currency)
        return float(amount) * exchange_rate
    else:
        print(f"Unsupported currency: {currency}")
        return 0.0


# Пример использования
transaction_example = {
    'amount': 100,
    'currency': 'USD'
}

amount_in_rub = calculate_transaction_amount(transaction_example)
print(f"Сумма транзакции в рублях: {amount_in_rub:.2f}")
