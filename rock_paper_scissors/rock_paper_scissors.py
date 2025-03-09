import random

winning_moves = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper"
}

options = list(winning_moves.keys())

while True:
    user_choice = input().strip().lower()

    if user_choice == "!exit":
        print("Bye!")
        break

    if user_choice in winning_moves:
        computer_choice = random.choice(options)

        if user_choice == computer_choice:
            print(f"There is a draw ({computer_choice})")
        elif winning_moves[user_choice] == computer_choice:
            print(f"Well done. The computer chose {computer_choice} and failed")
        else:
            print(f"Sorry, but the computer chose {computer_choice}")
    else:
        print("Invalid input.")
