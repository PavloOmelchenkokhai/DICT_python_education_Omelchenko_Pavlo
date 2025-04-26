import sys

commands = {
    "config": "Get and set a username.",
    "add": "Add a file to the index.",
    "log": "Show commit logs.",
    "commit": "Save changes.",
    "checkout": "Switch between commits and restore a previous file state."
}

def show_help():
    print("These are VCS commands:")
    for cmd, desc in commands.items():
        print(f"{cmd} {desc}")

def main():
    if len(sys.argv) == 1 or sys.argv[1] == "--help":
        show_help()
    else:
        command = sys.argv[1]
        if command in commands:
            print(commands[command])
        else:
            print(f"'{command}' is not a VCS command.")

if __name__ == "__main__":
    main()
