import random


def load_rating(filename):
    ratings = {}
    try:
        with open(filename, "r") as file:
            for line in file:
                name, score = line.strip().split()
                ratings[name] = int(score)
    except FileNotFoundError:
        pass
    return ratings


def get_game_result(user_choice, computer_choice, winning_moves):
    if user_choice == computer_choice:
        return "draw"
    elif winning_moves[user_choice] == computer_choice:
        return "win"
    else:
        return "lose"


def main():
    winning_moves = {"rock": "scissors", "paper": "rock", "scissors": "paper"}
    options = list(winning_moves.keys())

    user_name = input("Enter your name: ").strip()
    print(f"Hello, {user_name}")

    ratings = load_rating("rating.txt")
    score = ratings.get(user_name, 0)

    while True:
        user_choice = input().strip().lower()

        if user_choice == "!exit":
            print("Bye!")
            break

        if user_choice == "!rating":
            print(f"Your rating: {score}")
            continue

        if user_choice in winning_moves:
            computer_choice = random.choice(options)
            result = get_game_result(user_choice, computer_choice, winning_moves)

            if result == "draw":
                score += 50
                print(f"There is a draw ({computer_choice})")
            elif result == "win":
                score += 100
                print(f"Well done. The computer chose {computer_choice} and failed")
            else:
                print(f"Sorry, but the computer chose {computer_choice}")
        else:
            print("Invalid input.")


if __name__ == "__main__":
    main()
