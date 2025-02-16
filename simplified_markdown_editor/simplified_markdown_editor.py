def print_help():
    """Вивід форматів"""
    formatters = [
        "plain", "bold", "italic", "inline-code", "link",
        "header", "unordered-list", "ordered-list", "new-line"
    ]
    print("Available formatters: " + " ".join(formatters))


def apply_format(formatter, text):
    if formatter == "plain":
        return text
    elif formatter == "bold":
        return f"**{text}**"
    elif formatter == "italic":
        return f"*{text}*"
    elif formatter == "inline-code":
        return f"`{text}`"
    elif formatter == "header":
        try:
            level = int(input("Level: "))
            if level < 1 or level > 6:
                print("The level should be within the range of 1 to 6.")
                return None
            text = input("Text: ")
            return f"{'#' * level} {text}\n"
        except ValueError:
            print("Invalid level input.")
            return None
    elif formatter == "link":
        label = input("Label: ")
        url = input("URL: ")
        return f"[{label}]({url})"
    elif formatter == "new-line":
        return "\n"
    elif formatter in ["ordered-list", "unordered-list"]:
        try:
            num_rows = int(input("Number of rows: "))
            if num_rows <= 0:
                print("The number of rows should be greater than zero.")
                return None

            items = []
            for i in range(1, num_rows + 1):
                item = input(f"Row #{i}: ")
                prefix = f"{i}. " if formatter == "ordered-list" else "* "
                items.append(f"{prefix}{item}")

            return "\n".join(items) + "\n"
        except ValueError:
            print("Invalid number of rows.")
            return None
    else:
        return None


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
            print(markdown)
            break
        elif command in formatters:
            if command == "new-line":
                formatted_text = apply_format(command, "")
            elif command in ["ordered-list", "unordered-list"]:
                formatted_text = apply_format(command, "")
            else:
                text = input("Text: ")
                formatted_text = apply_format(command, text)

            if formatted_text is not None:
                markdown += formatted_text + " "
                print(markdown.strip())
        else:
            print("Unknown formatting type or command")


if __name__ == "__main__":
    main()