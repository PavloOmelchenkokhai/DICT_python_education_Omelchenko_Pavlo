import random
import os

rating_file = "rating.txt"


def load_ratings():
    """Завантажує рейтинг із файлу"""
    if not os.path.exists(rating_file):
        return {}

    with open(rating_file, "r") as file:
        return {line.split()[0]: int(line.split()[1]) for line in file if len(line.split()) == 2}


def save_ratings(ratings):
    """Зберігає рейтинг у файл"""
    with open(rating_file, "w") as file:
        file.writelines(f"{name} {score}\n" for name, score in ratings.items())


def get_username():
    """Отримує ім'я гравця"""
    name = input("Enter your name: ").strip()
    print(f"Hello, {name}")
    return name


def get_options():
    """Запитує у гравця набір символів для гри"""
    default = ["rock", "paper", "scissors"]
    extended = [
        "rock", "gun", "lightning", "devil", "dragon", "water", "air", "paper",
        "sponge", "wolf", "tree", "human", "snake", "scissors", "fire"
    ]

    user_input = input("Enter options separated by commas (or press Enter for default Rock, Paper, Scissors): ").strip()
    return default if not user_input else [opt.strip().lower() for opt in user_input.split(",")]


def generate_rules(options):
    """Створює список переможців для кожного символу"""
    rules = {}
    n = len(options)

    for i, option in enumerate(options):
        rules[option] = [options[(i - j) % n] for j in range(1, (n // 2) + 1)]

    return rules


def determine_result(player, computer, rules):
    """Визначає результат раунду"""
    if player == computer:
        return f"There is a draw ({computer})", 50
    if computer in rules[player]:
        return f"Well done. The computer chose {computer} and failed", 100
    return f"Sorry, but the computer chose {computer}", 0


def play_game(username, score, options, rules, ratings):
    """Основний ігровий цикл"""
    while True:
        choice = input("Enter your choice (!rating, !exit, or one of the options): ").strip().lower()

        if choice == "!exit":
            ratings[username] = score
            save_ratings(ratings)
            print("Bye!")
            break

        if choice == "!rating":
            print(f"Your rating: {score}")
            continue

        if choice in options:
            computer_choice = random.choice(options)
            message, points = determine_result(choice, computer_choice, rules)
            print(message)
            score += points
        else:
            print("Invalid input.")


# Запуск гри
ratings = load_ratings()
username = get_username()
score = ratings.get(username, 0)
options = get_options()
rules = generate_rules(options)

play_game(username, score, options, rules, ratings)
