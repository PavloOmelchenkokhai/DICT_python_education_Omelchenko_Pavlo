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
        print(''.join(str(x) for x in snake[:3]) + '...' + ''.join(str(x) for x in snake[-3:]))
    else:
        print(''.join(str(x) for x in snake))
    print("\nYour pieces:")
    for i, piece in enumerate(player, 1):
        print(f"{i}:{piece}")
    print()
    if status == "player":
        print("Status: It's your turn to make a move. Enter your command.")
    else:
        print("Status: Computer is about to make a move. Press Enter to continue...")

def check_draw(snake):
    if len(snake) < 8: return False
    left, right = snake[0][0], snake[-1][1]
    if left != right: return False
    count = sum([piece.count(left) for piece in snake])
    return count >= 8

def is_move_legal(piece, direction, snake):
    left_val = snake[0][0]
    right_val = snake[-1][1]
    if direction == 'left':
        return piece[0] == left_val or piece[1] == left_val
    else:
        return piece[0] == right_val or piece[1] == right_val

def apply_piece(piece, direction, snake):
    if direction == 'left':
        if piece[1] == snake[0][0]:
            snake.insert(0, piece)
        else:
            snake.insert(0, piece[::-1])
    else:
        if piece[0] == snake[-1][1]:
            snake.append(piece)
        else:
            snake.append(piece[::-1])

def get_valid_input(player, snake):
    while True:
        try:
            move = int(input("> "))
            if abs(move) > len(player):
                print("Invalid input. Please try again.")
                continue
            if move == 0:
                return move
            piece = player[abs(move)-1]
            direction = 'right' if move > 0 else 'left'
            if is_move_legal(piece, direction, snake):
                return move
            else:
                print("Illegal move. Please try again.")
        except ValueError:
            print("Invalid input. Please try again.")

def make_player_move(player, snake, stock):
    move = get_valid_input(player, snake)
    if move == 0:
        if stock:
            player.append(stock.pop())
    else:
        index = abs(move) - 1
        piece = player.pop(index)
        direction = 'right' if move > 0 else 'left'
        apply_piece(piece, direction, snake)

def make_computer_move(computer, snake, stock):
    possible_moves = list(range(-len(computer), len(computer)+1))
    random.shuffle(possible_moves)

    for move in possible_moves:
        if move == 0:
            continue
        index = abs(move) - 1
        piece = computer[index]
        direction = 'right' if move > 0 else 'left'
        if is_move_legal(piece, direction, snake):
            piece = computer.pop(index)
            apply_piece(piece, direction, snake)
            return

    if stock:
        computer.append(stock.pop())

while True:
    full_set = create_domino_set()
    stock, computer, player = split_pieces(full_set)
    player_double = find_highest_double(player)
    computer_double = find_highest_double(computer)
    if not player_double and not computer_double:
        continue
    if player_double and (not computer_double or player_double > computer_double):
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
        make_player_move(player, snake, stock)
        status = "computer"
    else:
        input()
        make_computer_move(computer, snake, stock)
        status = "player"
