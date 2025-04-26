import sys
import os

VCS_DIR = "vcs"
CONFIG_FILE = os.path.join(VCS_DIR, "config.txt")
INDEX_FILE = os.path.join(VCS_DIR, "index.txt")

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

def setup_directories():
    if not os.path.exists(VCS_DIR):
        os.makedirs(VCS_DIR)
    if not os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'w') as f:
            pass
    if not os.path.exists(INDEX_FILE):
        with open(INDEX_FILE, 'w') as f:
            pass

def config(args):
    if len(args) == 0:
        if os.path.getsize(CONFIG_FILE) == 0:
            print("Please, tell me who you are.")
        else:
            with open(CONFIG_FILE, 'r') as f:
                username = f.read().strip()
            print(f"The username is {username}.")
    else:
        username = args[0]
        with open(CONFIG_FILE, 'w') as f:
            f.write(username)
        print(f"The username is {username}.")

def add(args):
    if len(args) == 0:
        if os.path.getsize(INDEX_FILE) == 0:
            print("Add a file to the index.")
        else:
            print("Tracked files:")
            with open(INDEX_FILE, 'r') as f:
                files = f.read().strip()
                print(files)
    else:
        filename = args[0]
        if os.path.exists(filename):
            with open(INDEX_FILE, 'a') as f:
                f.write(filename + '\n')
            print(f"The file '{filename}' is tracked.")
        else:
            print(f"Can't find '{filename}'.")

def main():
    setup_directories()

    if len(sys.argv) == 1 or sys.argv[1] == "--help":
        show_help()
    else:
        command = sys.argv[1]
        args = sys.argv[2:]
        if command in commands:
            if command == "config":
                config(args)
            elif command == "add":
                add(args)
            else:
                print(commands[command])
        else:
            print(f"'{command}' is not a VCS command.")

if __name__ == "__main__":
    main()
