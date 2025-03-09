import random


def load_ratings(filename="rating.txt"):
    ratings = {}
    try:
        with open(filename, "r") as file:
            for line in file:
                name, score = line.strip().split()
                ratings[name] = int(score)
    except FileNotFoundError:
        pass
    return ratings


def determine_winners(options):
    rules = {}
    n = len(options)
    for i, option in enumerate(options):
        losing = options[i + 1:i + 1 + (n // 2)]
        winning = options[i - (n // 2):i] if i - (n // 2) >= 0 else options[:i] + options[i + 1:]
        rules[option] = set(losing)
    return rules


def main():
    ratings = load_ratings()
    name = input("Enter your name: ")
    print(f"Hello, {name}")
    score = ratings.get(name, 0)

    options_input = input()
    options = options_input.split(",") if options_input else ["rock", "paper", "scissors"]
    rules = determine_winners(options)

    print("Okay, let's start.")

    while True:
        user_choice = input()
        if user_choice == "!exit":
            print("Bye!")
            break
        elif user_choice == "!rating":
            print(f"Your rating: {score}")
        elif user_choice in options:
            computer_choice = random.choice(options)
            if user_choice == computer_choice:
                print(f"There is a draw ({computer_choice})")
                score += 50
            elif computer_choice in rules[user_choice]:
                print(f"Well done. The computer chose {computer_choice} and failed")
                score += 100
            else:
                print(f"Sorry, but the computer chose {computer_choice}")
        else:
            print("Invalid input")


if __name__ == "__main__":
    main()
