def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if all(cell == player for cell in board[i]) or all(row[i] == player for row in board):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    return all(cell != ' ' for row in board for cell in row)

def is_valid_move(move, board):
    row, col = move
    return 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' '

def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    players = ['X', 'O']
    current_player = players[0]

    while True:
        print_board(board)

        # Get the player's move
        try:
            row = int(input(f"Player {current_player}, enter row (0, 1, or 2): "))
            col = int(input(f"Player {current_player}, enter column (0, 1, or 2): "))
            move = (row, col)

            if not is_valid_move(move, board):
                print("Invalid move. Try again.")
                continue

            board[row][col] = current_player

            if check_winner(board, current_player):
                print_board(board)
                print(f"Player {current_player} wins!")
                break

            if is_board_full(board):
                print_board(board)
                print("It's a draw!")
                break

            # Switch to the other player
            current_player = players[1] if current_player == players[0] else players[0]

        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    tic_tac_toe()
