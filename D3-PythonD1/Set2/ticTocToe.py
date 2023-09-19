import itertools
import os
import copy

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_board(board):
    clear_screen()
    print("Tic-Tac-Toe Game\n")
    for row in board:
        print(" | ".join(row))
        print("-" * (4 * len(row) - 1))

def is_winner(board, player, win_pattern):
    for pattern in win_pattern:
        if all(board[row][col] == player for row, col in pattern):
            return True
    return False

def is_board_full(board):
    return all(cell != ' ' for row in board for cell in row)

def get_move(board_size):
    while True:
        try:
            move = input(f"Enter your move (e.g., 0 0 for top-left on a {board_size}x{board_size} board): ").strip()
            row, col = map(int, move.split())
            
            if 0 <= row < board_size and 0 <= col < board_size:
                return row, col
            else:
                print("Invalid input. Please enter valid row and column indices within the board size.")
        except ValueError:
            print("Invalid input. Please enter two integers separated by a space.")

def create_board(board_size):
    return [[' ' for _ in range(board_size)] for _ in range(board_size)]

def create_win_pattern(board_size):
    # Create winning patterns for rows, columns, and diagonals
    rows = [[(i, j) for j in range(board_size)] for i in range(board_size)]
    cols = [[(i, j) for i in range(board_size)] for j in range(board_size)]
    diagonals = [[(i, i) for i in range(board_size)], [(i, board_size - 1 - i) for i in range(board_size)]]
    return rows + cols + diagonals

def play_game():
    while True:
        board_size = int(input("Enter the board size (e.g., 3 for a 3x3 board): "))
        win_pattern = create_win_pattern(board_size)
        board = create_board(board_size)
        player_turn = itertools.cycle(['X', 'O'])
        current_player = next(player_turn)
        moves_history = []

        print_board(board)

        while True:
            print(f"Player {current_player}'s turn:")
            row, col = get_move(board_size)

            if board[row][col] == ' ':
                board[row][col] = current_player
                moves_history.append(copy.deepcopy(board))
            else:
                print("Invalid move. That cell is already occupied.")
                continue

            print_board(board)

            if is_winner(board, current_player, win_pattern):
                print(f"Player {current_player} wins!")
                break
            elif is_board_full(board):
                print("It's a tie!")
                break

            current_player = next(player_turn)

        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            break

if __name__ == "__main__":
    play_game()
