import random

def create_domino_set():
    return [[i, j] for i in range(7) for j in range(i, 7)]

def split_pieces(full_set):
    random.shuffle(full_set)
    return full_set[:14], full_set[14:21], full_set[21:]

def find_highest_double(pieces):
    doubles = [piece for piece in pieces if piece[0] == piece[1]]
    return max(doubles, default=None)

def display_state(stock, computer, player, snake, status):
    print("=" * 70)
    print(f"Stock size: {len(stock)}")
    print(f"Computer pieces: {len(computer)}")

    if len(snake) > 6:
        print(f"{snake[:3]}...{snake[-3:]}")
    else:
        print(''.join(str(s) for s in snake))

    print("\nYour pieces:")
    for i, piece in enumerate(player, 1):
        print(f"{i}:{piece}")

    print()
    if status == "player":
        print("Status: It's your turn to make a move. Enter your command.")
    elif status == "computer":
        print("Status: Computer is about to make a move. Press Enter to continue...")

def check_draw(snake):
    if len(snake) < 8:
        return False
    ends = snake[0][0], snake[-1][1]
    if ends[0] != ends[1]:
        return False
    count = sum(s.count(ends[0]) for s in snake)
    return count >= 8

def make_move(pieces, snake, stock, move):
    if move == 0:
        if stock:
            pieces.append(stock.pop())
    else:
        index = abs(move) - 1
        if 0 <= index < len(pieces):
            piece = pieces.pop(index)
            if move > 0:
                snake.append(piece)
            else:
                snake.insert(0, piece)

def get_valid_input(player):
    while True:
        try:
            move = int(input("> "))
            if abs(move) <= len(player):
                return move
            else:
                print("Invalid input. Please try again.")
        except ValueError:
            print("Invalid input. Please try again.")

while True:
    full_set = create_domino_set()
    stock, computer, player = split_pieces(full_set)

    player_double = find_highest_double(player)
    computer_double = find_highest_double(computer)

    if not player_double and not computer_double:
        continue

    if (player_double and not computer_double) or (player_double and computer_double and player_double > computer_double):
        snake = [player_double]
        player.remove(player_double)
        status = "computer"
    else:
        snake = [computer_double]
        computer.remove(computer_double)
        status = "player"
    break

while True:
    display_state(stock, computer, player, snake, status)

    if not player:
        print("Status: The game is over. You won!")
        break
    elif not computer:
        print("Status: The game is over. The computer won!")
        break
    elif check_draw(snake):
        print("Status: The game is over. It's a draw!")
        break

    if status == "player":
        move = get_valid_input(player)
        make_move(player, snake, stock, move)
        status = "computer"
    else:
        input()
        move = random.randint(-len(computer), len(computer))
        make_move(computer, snake, stock, move)
        status = "player"
