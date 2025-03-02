import random


def generate_task():
    num1 = random.randint(2, 9)
    num2 = random.randint(2, 9)
    operator = random.choice(['+', '-', '*'])

    print(f"{num1} {operator} {num2}")
    return num1, num2, operator


def get_correct_answer(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2


def main():
    num1, num2, operator = generate_task()

    try:
        user_answer = int(input())
        correct_answer = get_correct_answer(num1, num2, operator)

        if user_answer == correct_answer:
            print("Right!")
        else:
            print("Wrong!")
    except ValueError:
        print("Invalid input. Please enter a number.")


if __name__ == "__main__":
    main()