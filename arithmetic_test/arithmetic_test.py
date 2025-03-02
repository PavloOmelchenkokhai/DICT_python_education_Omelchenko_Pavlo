import random


def generate_problem(level):
    """Генерує завдання залежно від рівня складності."""
    if level == 1:
        num1 = random.randint(2, 9)
        num2 = random.randint(2, 9)
        operation = random.choice(['+', '-', '*'])
        expression = f"{num1} {operation} {num2}"
        answer = eval(expression)
    elif level == 2:
        num1 = random.randint(11, 29)
        expression = f"{num1}"
        answer = num1 ** 2
    else:
        return None, None
    return expression, answer


def get_valid_input(prompt):
    """Запитує введення користувача та перевіряє, чи є воно числом."""
    while True:
        user_input = input(prompt)
        if user_input.lstrip('-').isdigit():
            return int(user_input)
        print("Incorrect format.")


def main():
    while True:
        try:
            level = int(input(
                "Which level do you want? Enter a number:\n1 - simple operations with numbers 2-9\n2 - integral squares of 11-29\n> "))
            if level in [1, 2]:
                break
            else:
                print("Incorrect format.")
        except ValueError:
            print("Incorrect format.")

    correct_answers = 0
    for _ in range(5):
        expression, correct_answer = generate_problem(level)
        print(expression)
        user_answer = get_valid_input("> ")
        if user_answer == correct_answer:
            print("Right!")
            correct_answers += 1
        else:
            print("Wrong!")

    print(f"Your mark is {correct_answers}/5.")
    save_result = input("Would you like to save your result to the file? Enter yes or no.\n> ").strip().lower()

    if save_result in ["yes", "y"]:
        name = input("What is your name?\n> ").strip()
        level_description = "simple operations with numbers 2-9" if level == 1 else "integral squares of 11-29"
        with open("results.txt", "a", encoding="utf-8") as file:
            file.write(f"{name}: {correct_answers}/5 in level {level} ({level_description}).\n")
        print("The results are saved in \"results.txt\".")


if __name__ == "__main__":
    main()
