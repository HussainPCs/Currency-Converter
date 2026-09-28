import requests
def converter(from_currency,to_currency,amount):
    url = f"https://api.frankfurter.dev/v1/latest?base={from_currency}&symbols={to_currency}"
    response = requests.get(url)
    data = response.json()
    rates = data["rates"][to_currency]
    final = float(amount)*rates
    return final
from_currency = input("What currency do you want to convert?\n")
to_currency = input("What currency do you want to convert?\n")
amount = float(input("How much do you want to convert?\n"))
print(f"{amount} {from_currency} would be {converter(from_currency,to_currency,amount):.2f} {to_currency}")


