import math


def calculate_months(principal, monthly_payment, interest_rate):
    """Обчислення кількості місяців для погашення кредиту"""
    i = (interest_rate / 100) / 12  # Щомісячна процентна ставка

    # Обчислення кількості платежів
    months = math.ceil(math.log(monthly_payment / (monthly_payment - i * principal), 1 + i))

    # Перетворення у роки та місяці
    years = months // 12
    remaining_months = months % 12

    if years > 0 and remaining_months > 0:
        return f"It will take {years} years and {remaining_months} months to repay the loan"
    elif years > 0:
        return f"It will take {years} years to repay the loan"
    else:
        return f"It will take {months} months to repay the loan"


# Основний код
principal = int(input("Enter the loan principal:\n> "))

print("What do you want to calculate?")
print('type "m" – for number of monthly payments,')
print('type "p" – for the monthly payment,')
print('type "a" – for annuity monthly payment:')
choice = input("> ").strip()

if choice == "m":
    # Користувач хоче обчислити кількість місяців
    monthly_payment = float(input("Enter the monthly payment:\n> "))
    interest_rate = float(input("Enter the loan interest:\n> "))

    result = calculate_months(principal, monthly_payment, interest_rate)
    print(result)

elif choice == "p":
    # Користувач хоче обчислити щомісячний платіж
    months = int(input("Enter the number of months:\n> "))

    payment = math.ceil(principal / months)
    last_payment = principal - (months - 1) * payment

    if payment == last_payment:
        print(f"Your monthly payment = {payment}")
    else:
        print(f"Your monthly payment = {payment} and the last payment = {last_payment}.")

elif choice == "a":
    # Користувач хоче обчислити ануїтетний платіж
    interest_rate = float(input("Enter the loan interest:\n> "))
    months = int(input("Enter the number of months:\n> "))

    i = (interest_rate / 100) / 12  # Щомісячна процентна ставка
    annuity_payment = principal * (i * (1 + i) ** months) / ((1 + i) ** months - 1)

    print(f"Your annuity payment = {math.ceil(annuity_payment)}")

else:
    print("Invalid choice")
