import random


def generate_question():
    """Генерує просте арифметичне завдання."""
    num1 = random.randint(2, 9)
    num2 = random.randint(2, 9)
    operation = random.choice(['+', '-', '*'])
    question = f"{num1} {operation} {num2}"
    correct_answer = eval(question)
    return question, correct_answer


def get_valid_input():
    """Отримує коректне числове введення користувача."""
    while True:
        user_input = input(">")
        if user_input.lstrip('-').isdigit():
            return int(user_input)
        print("Incorrect format.")


def main():
    score = 0
    total_questions = 5

    for _ in range(total_questions):
        question, correct_answer = generate_question()
        print(question)
        user_answer = get_valid_input()

        if user_answer == correct_answer:
            print("Right!")
            score += 1
        else:
            print("Wrong!")

    print(f"Your mark is {score}/{total_questions}.")


if __name__ == "__main__":
    main()