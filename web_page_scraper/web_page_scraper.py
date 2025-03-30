import requests
from bs4 import BeautifulSoup
import json

# Отримуємо URL від користувача
url = input("Input the URL:\n> ").strip()

# Перевіряємо, чи це сторінка фільму/серіалу IMDb
if "imdb.com/title/" not in url:
    print("Invalid movie page!")
    exit()

try:
    # Виконуємо HTTP-запит із заголовком для англійської версії сторінки
    headers = {
        "Accept-Language": "en-US,en;q=0.5",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(url, headers=headers, timeout=5)

    if response.status_code != 200:
        print("Invalid movie page!")
    else:
        # Використовуємо BeautifulSoup для аналізу HTML
        soup = BeautifulSoup(response.text, 'html.parser')

        # Отримуємо заголовок фільму
        title_tag = soup.find("h1")  # IMDb використовує <h1> для назв фільмів
        title = title_tag.text.strip() if title_tag else None

        # Отримуємо опис фільму
        description_tag = soup.find("span", {"data-testid": "plot-l"})
        description = description_tag.text.strip() if description_tag else None

        # Перевіряємо, чи отримані дані коректні
        if title and description:
            movie_data = {"title": title, "description": description}
            print(json.dumps(movie_data, indent=4))
        else:
            print("Invalid movie page!")
except requests.exceptions.RequestException:
    print("Invalid movie page!")  # Обробка помилок запиту
