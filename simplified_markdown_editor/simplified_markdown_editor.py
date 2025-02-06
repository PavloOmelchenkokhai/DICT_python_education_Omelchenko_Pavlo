def print_help():
    """Вивід форматів"""
formatters = [
    "plain","bold","italic","inline-code","link",
    "header","unordered-list","ordered-list","new-line"
]

print("Available formatters: ".join(formatters))

while True:
    command = input("Choose a formatter:").strip()
    if command == "!help":
        print(formatters)
    elif command == "!done":
        break
    else:
        print("Unknown formatting type or command")

