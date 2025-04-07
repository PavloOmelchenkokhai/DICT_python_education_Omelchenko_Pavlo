import requests

# Крок 1: Отримати базову валюту (валюта, яку користувач має)
base_currency = input(">").lower()

# Крок 2: Завантажити дані з FloatRates
url = f"http://www.floatrates.com/daily/{base_currency}.json"
response = requests.get(url)
data = response.json()

# Крок 3: Створити кеш
cache = {}

# Зберігаємо у кеші курси до USD і EUR (якщо вони є)
for code in ['usd', 'eur']:
    if code in data:
        cache[code] = data[code]['rate']

# Кроки 4–10: Обробка запитів конвертації
while True:
    target_currency = input(">").lower()
    if not target_currency:
        break
    amount = float(input(">"))

    print("Checking the cache...")

    if target_currency in cache:
        print("It is in the cache!")
    else:
        print("Sorry, but it is not in the cache!")
        # Завантажити і додати в кеш
        if target_currency in data:
            cache[target_currency] = data[target_currency]['rate']
        else:
            print("Currency not found.")
            continue

    rate = cache[target_currency]
    result = round(amount * rate, 2)
    print(f"You received {result} {target_currency.upper()}.")
