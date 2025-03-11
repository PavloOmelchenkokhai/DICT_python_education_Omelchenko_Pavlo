import random


def load_ratings(filename="rating.txt"):
    """Завантаження рейтингу гравців"""
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
    """Формує правила перемог та програшів для кожного варіанту"""
    rules = {}
    n = len(options)
    for i, option in enumerate(options):
        losing = options[i + 1:i + 1 + (n // 2)] + options[:max(0, (i + 1 + (n // 2)) - n)]
        rules[option] = set(losing)
    return rules


def get_player_name():
    """Запит імені гравця"""
    name = input("Enter your name: ")
    print(f"Hello, {name}")
    return name


def get_game_options():
    """Отримує варіанти гри від користувача та перевіряє їх коректність"""
    while True:
        options_input = input(
            "Enter game options (comma-separated) or press Enter for default [rock, paper, scissors]: ")
        options = options_input.split(",") if options_input else ["rock", "paper", "scissors"]
        options = [opt.strip() for opt in options if opt.strip()]

        if len(options) < 3:
            print("Error: You need at least 3 different options to play!")
        else:
            return options


def play_game(name, ratings, options, rules):
    """Основний цикл гри"""
    score = ratings.get(name, 0)
    print("Type !exit to quit or !rating to see your score.")
    print("Okay, let's start.")

    while True:
        user_choice = input("> ").strip()

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
            elif (user_choice == "rock" and computer_choice == "scissors") or \
                 (user_choice != "rock" and computer_choice != "scissors" and computer_choice in rules[user_choice]):
                print(f"Well done. The computer chose {computer_choice} and failed")
                score += 100
            else:
                print(f"Sorry, but the computer chose {computer_choice}")
        else:
            print("Invalid input")


def main():
    ratings = load_ratings()
    name = get_player_name()
    options = get_game_options()
    rules = determine_winners(options)
    play_game(name, ratings, options, rules)


if __name__ == "__main__":
    main()