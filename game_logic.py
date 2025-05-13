# import random
from minimax import minimax , best_move , check_win


board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

PLAYER_SYMBOL = "x"
AI_SYMBOL = "o"
PLAYER2_SYMBOL = "o"

def display_board():
    print("\nCurrent Board:")
    print("-----------")
    for i, row in enumerate(board):
        print("|", end=" ")
        for j, cell in enumerate(row):
            print(cell, end=" | ")
        print("\n-----------")

def initialize_game(game_mode):
    """Display welcome message and print empty board"""
    print("Welcome to Tic Tac Toe game")
    if game_mode == "1":
        print("You are Player 1 (" + PLAYER_SYMBOL + ")")
        print("The AI is (" + AI_SYMBOL + ")")
    else:
        print("Player 1 (" + PLAYER_SYMBOL + ")")
        print("Player 2 (" + PLAYER2_SYMBOL + ")")
    display_board()

# def check_win(board):
#     """
#     Check for a winner or tie on the board.
#     Returns 'x' if X wins, 'o' if O wins, 'tie' if draw, or None if game ongoing.
#     """
#     for i in range(3):
#         if board[i][0] == board[i][1] == board[i][2] != ' ':
#             return board[i][0]
        
#         if board[0][i] == board[1][i] == board[2][i] != ' ':
#             return board[0][i]
        
#     if board[0][0] == board[1][1] == board[2][2] != ' ':
#         return board[0][0]
    
#     if board[0][2] == board[1][1] == board[2][0] != ' ':
#         return board[0][2]
    
#     for row in board:
#         if ' ' in row:
#             return None
#     return 'tie'

def board_full():
    """check if each board empty or full"""
    for row in board:
        if " " in row:
            return False
    return True

def get_player_move(player_symbol="x", player_number=1):
    while True:
        try:
            prompt = f"Player {player_number} ({player_symbol}), enter your move (row then column): "
            place = input(prompt).split()
            if len(place) != 2:
                print("Please enter two numbers separated by a space.")
                continue
            
            row, col = int(place[0]), int(place[1])

            if 0 <= row <= 2 and 0 <= col <= 2:
                if board[row][col] == " ":
                    board[row][col] = player_symbol
                    return
                else:
                    print("That position is already taken. Please choose another.")
            else:
                print("Invalid input. Please enter numbers between 0 and 2.")
        except ValueError:
            print("Please enter valid numbers.")

# def make_ai_move():
#     empty_positions = []
#     for i in range(3):
#         for j in range(3):
#             if board[i][j] == " ":
#                 empty_positions.append((i, j))

#     if empty_positions:
#         row, col = random.choice(empty_positions)
#         board[row][col] = AI_SYMBOL
#         print(f"AI places {AI_SYMBOL} at position ({row}, {col})")
#     else:
#         print("No more moves available")


while True:
    game_mode = input("Select game mode:\n1. Player vs AI\n2. Player vs Player\nEnter 1 or 2: ")
    if game_mode in ["1", "2"]:
        break
    print("Invalid choice. Please enter 1 or 2.")

initialize_game(game_mode)

if game_mode == "1":
    while True:
        get_player_move()
        display_board()
        minimax_value = minimax(board, 0, False)
        if check_win(board) == PLAYER_SYMBOL:
            print("Player wins!")
            break
        elif board_full():
            print("Draw")
            break
        row, col = best_move(board)
        board[row][col] = AI_SYMBOL
        print(f"AI played at: {row} {col}")
        display_board()
        if check_win(board) == AI_SYMBOL:
            print("AI wins!")
            break
        elif board_full():
            print("Draw")
            break
else:

    current_player = 1
    while True:
        if current_player == 1:
            get_player_move(PLAYER_SYMBOL, 1)
            player_symbol = PLAYER_SYMBOL
        else:
            get_player_move(PLAYER2_SYMBOL, 2)
            player_symbol = PLAYER2_SYMBOL
        
        display_board()
        
        if check_win(player_symbol):
            print(f"Player {current_player} wins!")
            break
        elif board_full():
            print("Draw")
            break
        current_player = 2 if current_player == 1 else 1
def play_again():
    while True:
        choice = input("Do you want to play again? (yes/no): ")
        if choice == "yes":
            return True
        elif choice == "no":
            return False
        else:
            print("Invalid choice. Please enter 'yes' or 'no'.")