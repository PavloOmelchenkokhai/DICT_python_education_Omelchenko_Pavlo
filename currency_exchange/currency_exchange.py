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
