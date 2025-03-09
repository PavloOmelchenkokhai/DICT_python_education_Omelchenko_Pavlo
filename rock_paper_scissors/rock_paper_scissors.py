winning_moves = {
    "rock": "paper",
    "paper": "scissors",
    "scissors": "rock"
}

user_choice = input().strip().lower()
if user_choice in winning_moves:
    computer_choice = winning_moves[user_choice]
    print(f"Sorry, but the computer chose {computer_choice}")
else:
    print("Invalid input. Please choose rock, paper, or scissors.")