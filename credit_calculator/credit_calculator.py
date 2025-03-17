import math


def calculate_diff_payments(principal, periods, interest_rate):
    """Обчислення диференційованих платежів"""
    i = (interest_rate / 100) / 12  # Щомісячна процентна ставка
    total_payment = 0

    for m in range(1, periods + 1):
        Dm = (principal / periods) + i * (principal - (principal * (m - 1) / periods))
        total_payment += math.ceil(Dm)
        print(f"Month {m}: payment is {math.ceil(Dm)}")

    overpayment = total_payment - principal
    print(f"Overpayment = {overpayment}")


def calculate_months(principal, monthly_payment, interest_rate):
    """Обчислення кількості місяців для ануїтетних платежів"""
    i = (interest_rate / 100) / 12  # Щомісячна процентна ставка

    months = math.ceil(math.log(monthly_payment / (monthly_payment - i * principal), 1 + i))

    years = months // 12
    remaining_months = months % 12

    if years > 0 and remaining_months > 0:
        print(f"It will take {years} years and {remaining_months} months to repay the loan")
    elif years > 0:
        print(f"It will take {years} years to repay the loan")
    else:
        print(f"It will take {months} months to repay the loan")

    overpayment = (months * monthly_payment) - principal
    print(f"Overpayment = {overpayment}")


def calculate_annuity_payment(principal, periods, interest_rate):
    """Обчислення ануїтетного платежу"""
    i = (interest_rate / 100) / 12  # Щомісячна процентна ставка
    annuity_payment = principal * (i * (1 + i) ** periods) / ((1 + i) ** periods - 1)
    annuity_payment = math.ceil(annuity_payment)

    print(f"Your annuity payment = {annuity_payment}")

    overpayment = (annuity_payment * periods) - principal
    print(f"Overpayment = {overpayment}")


def calculate_principal(monthly_payment, periods, interest_rate):
    """Обчислення основної суми кредиту"""
    i = (interest_rate / 100) / 12  # Щомісячна процентна ставка

    principal = monthly_payment / ((i * (1 + i) ** periods) / ((1 + i) ** periods - 1))
    principal = round(principal)

    print(f"Your loan principal = {principal}")

    overpayment = (monthly_payment * periods) - principal
    print(f"Overpayment = {overpayment}")


def main():
    print("Welcome to Credit Calculator!")
    loan_type = input("Enter loan type (annuity/diff): ").strip()

    if loan_type not in ["annuity", "diff"]:
        print("Incorrect loan type")
        return

    principal = float(input("Enter loan principal: "))
    periods = int(input("Enter number of months: "))
    interest_rate = float(input("Enter loan interest (without %): "))

    if loan_type == "diff":
        calculate_diff_payments(principal, periods, interest_rate)
    else:
        calc_type = input("Calculate (annuity payment / principal / months)? (a/p/m): ").strip()
        if calc_type == "a":
            calculate_annuity_payment(principal, periods, interest_rate)
        elif calc_type == "p":
            payment = float(input("Enter monthly payment: "))
            calculate_principal(payment, periods, interest_rate)
        elif calc_type == "m":
            payment = float(input("Enter monthly payment: "))
            calculate_months(principal, payment, interest_rate)
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
