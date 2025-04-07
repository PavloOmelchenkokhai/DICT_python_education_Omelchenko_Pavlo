# Зчитування кількості монет
mycoins = float(input("Please, enter the number of mycoins you have: > "))

# Зчитування курсу обміну
exchange_rate = float(input("Please, enter the exchange rate: > "))

# Обчислення у доларах
dollars = mycoins * exchange_rate

# Виведення результату
print(f"The total amount of dollars: {dollars:.2f}")
