import random

accounts = {}

def generate_card_number():
    iin = "400000"
    account_identifier = str(random.randint(0, 999999999)).zfill(9)
    checksum = str(random.randint(0, 9))  # Поки що випадкова цифра (алгоритм Луна – на наступних етапах)
    return iin + account_identifier + checksum

def generate_pin():
    return str(random.randint(0, 9999)).zfill(4)

def create_account():
    while True:
        card_number = generate_card_number()
        if card_number not in accounts:
            pin = generate_pin()
            accounts[card_number] = {"pin": pin, "balance": 0}
            print("\nYour card has been created")
            print("Your card number:")
            print(card_number)
            print("Your card PIN:")
            print(pin)
            break

def log_in():
    print("\nEnter your card number:")
    card_number = input("> ")
    print("Enter your PIN:")
    pin = input("> ")

    if card_number in accounts and accounts[card_number]["pin"] == pin:
        print("\nYou have successfully logged in!")
        while True:
            print("\n1. Balance")
            print("2. Log out")
            print("0. Exit")
            choice = input("> ")
            if choice == "1":
                print(f"\nBalance: {accounts[card_number]['balance']}")
            elif choice == "2":
                print("\nYou have successfully logged out!")
                break
            elif choice == "0":
                print("\nBye!")
                exit()
            else:
                print("\nInvalid option.")
    else:
        print("\nWrong card number or PIN!")

def main():
    while True:
        print("\n1. Create an account")
        print("2. Log into account")
        print("0. Exit")
        choice = input("> ")
        if choice == "1":
            create_account()
        elif choice == "2":
            log_in()
        elif choice == "0":
            print("\nBye!")
            break
        else:
            print("\nInvalid option.")

if __name__ == "__main__":
    main()
