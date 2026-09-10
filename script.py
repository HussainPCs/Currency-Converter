import requests

def convert(from_currency, to_currency, amount):
    url = f"https://api.frankfurter.dev/v1/latest?base={from_currency}&symbols={to_currency}"
    response = requests.get(url)
    data = response.json()
    rate = data["rates"][to_currency]
    final = float(amount) * rate
    return final