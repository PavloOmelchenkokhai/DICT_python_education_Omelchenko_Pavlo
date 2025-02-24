def print_help():
    """Вивід форматів"""
    formatters = [
        "plain", "bold", "italic", "inline-code", "link",
        "header", "unordered-list", "ordered-list", "new-line"
    ]
    print("Available formatters: " + " ".join(formatters))
    print("Special commands: !help !done")


def get_text(prompt):
    """Отримати текст від користувача."""
    return input(prompt)


def apply_format(formatter):
    """Застосувати форматування."""
    if formatter == "plain":
        return get_text("Text: ")
    elif formatter == "bold":
        return f"**{get_text('Text: ')}**"
    elif formatter == "italic":
        return f"*{get_text('Text: ')}*"
    elif formatter == "inline-code":
        return f"`{get_text('Text: ')}`"
    elif formatter == "header":
        while True:
            try:
                level = int(input("Level: "))
                if 1 <= level <= 6:
                    break
                print("The level should be within the range of 1 to 6.")
            except ValueError:
                print("Invalid level input.")
        return f"{'#' * level} {get_text('')}\n"
    elif formatter == "link":
        label = get_text("Label: ")
        url = get_text("URL: ")
        return f"[{label}]({url})"
    elif formatter == "new-line":
        return "\n\n"
    elif formatter in ["ordered-list", "unordered-list"]:
        return get_list(formatter)
    return None


def get_list(formatter):
    """Отримати список."""
    while True:
        try:
            num_rows = int(input("Number of rows: "))
            if num_rows > 0:
                break
            print("The number of rows should be greater than zero.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    items = []
    for i in range(1, num_rows + 1):
        item = input(f"Row #{i}: ")
        prefix = f"{i}. " if formatter == "ordered-list" else "* "
        items.append(f"{prefix}{item}")

    return "\n" + "\n".join(items) + "\n"


def main():
    markdown = ""
    formatters = [
        "plain", "bold", "italic", "inline-code", "link",
        "header", "unordered-list", "ordered-list", "new-line"
    ]

    while True:
        command = input("Choose a formatter: ").strip()

        if command == "!help":
            print_help()
        elif command == "!done":
            with open("output.md", "w", encoding="utf-8") as file:
                file.write(markdown.strip())
            print(markdown)
            break
        elif command in formatters:
            formatted_text = apply_format(command)
            if formatted_text is not None:
                markdown += formatted_text
                print(markdown.strip())
        else:
            print("Unknown formatting type or command")


if __name__ == "__main__":
    main()