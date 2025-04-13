import random

def create_domino_set():
    return [[i, j] for i in range(7) for j in range(i, 7)]

def split_pieces(full_set):
    random.shuffle(full_set)
    return full_set[:14], full_set[14:21], full_set[21:]

def find_highest_double(pieces):
    doubles = [piece for piece in pieces if piece[0] == piece[1]]
    return max(doubles) if doubles else None

while True:
    full_set = create_domino_set()
    stock, computer, player = split_pieces(full_set)

    player_double = find_highest_double(player)
    computer_double = find_highest_double(computer)

    if not player_double and not computer_double:
        continue

    if (player_double and not computer_double) or (player_double and computer_double and player_double > computer_double):
        domino_snake = [player_double]
        player.remove(player_double)
        status = "computer"
    else:
        domino_snake = [computer_double]
        computer.remove(computer_double)
        status = "player"
    break

print("=" * 70)
print(f"Stock size: {len(stock)}")
print(f"Computer pieces: {len(computer)}\n")

print("Domino snake:")
print(domino_snake)

print("\nYour pieces:\n")
for idx, piece in enumerate(player, start=1):
    print(f"{idx}:{piece}")

# Статус гри
print()

if status == "computer":
    print("Status: Computer is about to make a move. Press Enter to continue...")
    input()
else:
    print("Status: It's your turn to make a move. Enter your command.")
