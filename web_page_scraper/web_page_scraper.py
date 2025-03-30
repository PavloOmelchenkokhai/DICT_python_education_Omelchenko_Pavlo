import requests

# Отримуємо URL від користувача
url = input("Input the URL:\n> ").strip()

try:
    # Виконуємо HTTP-запит
    response = requests.get(url, timeout=5)

    # Перевіряємо статус код
    if response.status_code == 200:
        # Записуємо контент сторінки у файл
        with open("source.html", "wb") as file:
            file.write(response.content)
        print("Content saved.")
    else:
        print(f"The URL returned {response.status_code}!")
except requests.exceptions.RequestException:
    print("The URL returned an error!")
