import math
import argparse


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
    parser = argparse.ArgumentParser(description="Credit Calculator")
    parser.add_argument("--type", choices=["annuity", "diff"], help="Type of payment: 'annuity' or 'diff'")
    parser.add_argument("--principal", type=float, help="Loan principal amount")
    parser.add_argument("--periods", type=int, help="Number of months")
    parser.add_argument("--interest", type=float, help="Loan interest rate (without %)")
    parser.add_argument("--payment", type=float, help="Monthly payment amount (only for annuity)")

    args = parser.parse_args()

    """Перевірка, чи всі параметри правильні"""
    if args.type not in ["annuity", "diff"]:
        print("Incorrect parameters")
        return

    if args.interest is None or args.interest <= 0:
        print("Incorrect parameters")
        return

    if args.type == "diff" and args.payment is not None:
        print("Incorrect parameters")
        return

    parameters = [args.principal, args.periods, args.interest, args.payment]
    if sum(p is not None for p in parameters) < 3:
        print("Incorrect parameters")
        return

    """Обчислення залежно від вибору користувача"""
    if args.type == "diff":
        if args.principal and args.periods:
            calculate_diff_payments(args.principal, args.periods, args.interest)
        else:
            print("Incorrect parameters")

    elif args.type == "annuity":
        if args.principal and args.periods:
            calculate_annuity_payment(args.principal, args.periods, args.interest)
        elif args.payment and args.periods:
            calculate_principal(args.payment, args.periods, args.interest)
        elif args.principal and args.payment:
            calculate_months(args.principal, args.payment, args.interest)
        else:
            print("Incorrect parameters")


if __name__ == "__main__":
    main()
