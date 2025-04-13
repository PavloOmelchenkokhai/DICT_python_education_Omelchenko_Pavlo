import random

def create_domino_set():
    """Генерує повний набір доміно (28 кісточок)"""
    return [[i, j] for i in range(7) for j in range(i, 7)]

def split_pieces(full_set):
    """Розділяє кісточки між гравцем, комп’ютером та резервом"""
    random.shuffle(full_set)
    return full_set[:14], full_set[14:21], full_set[21:]

def find_highest_double(pieces):
    """Повертає найбільший дубль, якщо є"""
    doubles = [piece for piece in pieces if piece[0] == piece[1]]
    return max(doubles) if doubles else None

while True:
    full_set = create_domino_set()
    stock, computer, player = split_pieces(full_set)

    player_double = find_highest_double(player)
    computer_double = find_highest_double(computer)

    if not player_double and not computer_double:
        continue

    # Визначити хто має більший дубль
    if (player_double and not computer_double) or (player_double and computer_double and player_double > computer_double):
        domino_snake = [player_double]
        player.remove(player_double)
        status = "computer"
    else:
        domino_snake = [computer_double]
        computer.remove(computer_double)
        status = "player"

    print("Stock pieces:", stock)
    print("Computer pieces:", computer)
    print("Player pieces:", player)
    print("Domino snake:", domino_snake)
    print("Status:", status)
    break
