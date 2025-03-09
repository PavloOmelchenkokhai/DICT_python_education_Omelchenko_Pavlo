import random

winning_moves = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper"
}

options = list(winning_moves.keys())

user_choice = input().strip().lower()
computer_choice = random.choice(options)

if user_choice in winning_moves:
    if user_choice == computer_choice:
        print(f"There is a draw ({computer_choice})")
    elif winning_moves[user_choice] == computer_choice:
        print(f"Well done. The computer chose {computer_choice} and failed")
    else:
        print(f"Sorry, but the computer chose {computer_choice}")
else:
    print("Invalid input. Please choose rock, paper, or scissors.")