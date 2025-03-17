import math

# Запитуємо суму кредиту
principal = int(input("Enter the loan principal:\n> "))

# Запитуємо, що користувач хоче обчислити
print("What do you want to calculate?")
print('type "m" – for number of monthly payments,')
print('type "p" – for the monthly payment:')
choice = input("> ").strip()

if choice == "m":
    # Якщо користувач хоче обчислити кількість місяців
    monthly_payment = int(input("Enter the monthly payment:\n> "))

    months = math.ceil(principal / monthly_payment)

    if months == 1:
        print("It will take 1 month to repay the loan")
    else:
        print(f"It will take {months} months to repay the loan")

elif choice == "p":
    # Якщо користувач хоче обчислити щомісячний платіж
    months = int(input("Enter the number of months:\n> "))

    payment = math.ceil(principal / months)
    last_payment = principal - (months - 1) * payment

    if payment == last_payment:
        print(f"Your monthly payment = {payment}")
    else:
        print(f"Your monthly payment = {payment} and the last payment = {last_payment}.")
else:
    print("Invalid choice")
