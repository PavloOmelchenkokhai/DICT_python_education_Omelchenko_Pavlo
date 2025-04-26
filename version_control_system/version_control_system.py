import sys
import os
import hashlib
import shutil

VCS_DIR = "vcs"
CONFIG_FILE = os.path.join(VCS_DIR, "config.txt")
INDEX_FILE = os.path.join(VCS_DIR, "index.txt")
LOG_FILE = os.path.join(VCS_DIR, "log.txt")
COMMITS_DIR = os.path.join(VCS_DIR, "commits")

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
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, 'w') as f:
            pass
    if not os.path.exists(COMMITS_DIR):
        os.makedirs(COMMITS_DIR)

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
            with open(INDEX_FILE, 'r') as f:
                tracked = f.read().splitlines()
            if filename not in tracked:
                with open(INDEX_FILE, 'a') as f:
                    f.write(filename + '\n')
            print(f"The file '{filename}' is tracked.")
        else:
            print(f"Can't find '{filename}'.")

def get_file_hash(filepath):
    with open(filepath, 'rb') as f:
        return hashlib.sha1(f.read()).hexdigest()

def get_latest_commit_hash():
    if not os.path.exists(LOG_FILE) or os.path.getsize(LOG_FILE) == 0:
        return None
    with open(LOG_FILE, 'r') as f:
        lines = f.read().split('\n')
        for line in lines:
            if line.startswith('commit'):
                return line.split()[1]
    return None

def commit(args):
    if len(args) == 0:
        print("Message was not passed.")
        return

    if os.path.getsize(INDEX_FILE) == 0:
        print("Nothing to commit.")
        return

    with open(INDEX_FILE, 'r') as f:
        tracked_files = f.read().splitlines()

    if not tracked_files:
        print("Nothing to commit.")
        return

    all_hash = hashlib.sha1()
    for file in tracked_files:
        if os.path.exists(file):
            with open(file, 'rb') as f:
                all_hash.update(f.read())

    new_commit_hash = all_hash.hexdigest()

    latest_commit_hash = get_latest_commit_hash()

    if new_commit_hash == latest_commit_hash:
        print("Nothing to commit.")
        return

    commit_path = os.path.join(COMMITS_DIR, new_commit_hash)
    os.makedirs(commit_path)

    for file in tracked_files:
        if os.path.exists(file):
            shutil.copy(file, commit_path)

    username = ""
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r') as f:
            username = f.read().strip()

    with open(LOG_FILE, 'r+') as log:
        old_logs = log.read()
        log.seek(0)
        log.write(f"commit {new_commit_hash}\n")
        log.write(f"Author: {username}\n")
        log.write(f"{args[0]}\n\n")
        log.write(old_logs)

    print("Changes are committed.")

def log_command():
    if os.path.getsize(LOG_FILE) == 0:
        print("No commits yet.")
    else:
        with open(LOG_FILE, 'r') as f:
            print(f.read().strip())

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
            elif command == "commit":
                commit(args)
            elif command == "log":
                log_command()
            else:
                print(commands[command])
        else:
            print(f"'{command}' is not a VCS command.")

if __name__ == "__main__":
    main()
