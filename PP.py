
def currency_converter(from_currency, to_currency, amount ):
    rate = float(input(f"What is the rate of {from_currency} to {to_currency}?"))
    calculation = amount * rate
    return calculation
from_currency = input("What currency do you want to convert from?")
to_currency = input("What currency do you want to convert to?")
amount = float(input("What is the amount?"))
print(f"The new value is: {currency_converter(from_currency, to_currency, amount)} {to_currency}")
