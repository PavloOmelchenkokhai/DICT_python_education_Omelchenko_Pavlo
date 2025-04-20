import random
import sqlite3

conn = sqlite3.connect('card.s3db')
cur = conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS card (
    id INTEGER PRIMARY KEY,
    number TEXT,
    pin TEXT,
    balance INTEGER DEFAULT 0
)
''')
conn.commit()

def luhn_checksum(number):
    digits = [int(d) for d in number]
    for i in range(0, len(digits), 2):
        digits[i] *= 2
        if digits[i] > 9:
            digits[i] -= 9
    return (10 - sum(digits) % 10) % 10

def generate_card_number():
    iin = "400000"
    acc_id = str(random.randint(0, 999999999)).zfill(9)
    partial_number = iin + acc_id
    checksum = luhn_checksum(partial_number)
    return partial_number + str(checksum)

def generate_pin():
    return str(random.randint(0, 9999)).zfill(4)

def create_account():
    while True:
        card_number = generate_card_number()
        cur.execute("SELECT number FROM card WHERE number = ?", (card_number,))
        if not cur.fetchone():
            pin = generate_pin()
            cur.execute("INSERT INTO card (number, pin) VALUES (?, ?)", (card_number, pin))
            conn.commit()
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

    cur.execute("SELECT * FROM card WHERE number = ? AND pin = ?", (card_number, pin))
    account = cur.fetchone()

    if account:
        print("\nYou have successfully logged in!")
        while True:
            print("\n1. Balance")
            print("2. Log out")
            print("0. Exit")
            choice = input("> ")
            if choice == "1":
                print(f"\nBalance: {account[3]}")
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
