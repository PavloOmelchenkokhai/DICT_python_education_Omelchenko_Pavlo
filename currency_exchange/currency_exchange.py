import requests

# Зчитування кількості mycoin
mycoins = float(input("> "))

# Курси валют
rates = {
    "ARS": 0.82,      # Аргентинське песо
    "HNL": 0.17,      # Гондураська лемпіра
    "AUD": 1.9622,    # Австралійський долар
    "MAD": 0.208      # Марокканський дирхам
}

# Прорахунок і вивід результатів
for currency, rate in rates.items():
    amount = round(mycoins * rate, 2)
    print(f"I will get {amount} {currency} from the sale of {mycoins} mycoins.")

# Запит на введення коду валюти
currency_code = input("\nEnter your base currency code (e.g. USD, EUR, AUD): ").lower()

# Формування URL
url = f"http://www.floatrates.com/daily/{currency_code}.json"

try:
    # Запит до сайту
    response = requests.get(url)
    data = response.json()

    # Отримання курсів до USD і EUR
    usd_rate = data.get('usd', {}).get('rate')
    eur_rate = data.get('eur', {}).get('rate')

    if usd_rate:
        print(f"\nExchange rate {currency_code.upper()} → USD: {round(usd_rate, 4)}")
    else:
        print("USD exchange rate not found.")

    if eur_rate:
        print(f"Exchange rate {currency_code.upper()} → EUR: {round(eur_rate, 4)}")
    else:
        print("EUR exchange rate not found.")

except Exception as e:
    print("Error while fetching exchange rates:", e)