import requests

# Отримання URL від користувача
url = input("Input the URL:\n> ").strip()

try:
    response = requests.get(url, timeout=5)  # Виконання запиту з таймаутом 5 секунд

    if response.status_code != 200:
        print("Invalid quote resource!")  # Якщо статус-код не 200
    else:
        try:
            data = response.json()  # Розбір JSON-відповіді
            quote = data.get("content")  # Отримання цитати

            if quote:
                print(quote)  # Вивід цитати
            else:
                print("Invalid quote resource!")  # Якщо в JSON немає цитати
        except ValueError:  # Якщо відповідь не JSON
            print("Invalid quote resource!")
except requests.exceptions.RequestException:
    print("Invalid quote resource!")  # Помилка підключення
