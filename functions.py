from variables import *
from forex_python.converter import CurrencyRates

c = CurrencyRates()

def Convert():
    global from_result, to_result, amount_result
    result.delete(0, END)
    
    amount_result = amount.get()
    amount_result = int(amount_result)

    from_result = from_currency.get().upper()

    to_result = to_currency.get().upper()
    result1 = c.convert(from_result, to_result, amount_result)

    return result.insert(END, f'{result1} {to_result}')