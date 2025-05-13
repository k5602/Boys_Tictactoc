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

def initialize_game(game_mode):
    """ print empty board"""
    if game_mode == "1":
        print("You are Player 1 (" + PLAYER_SYMBOL + ")")
        print("The AI is (" + AI_SYMBOL + ")")
    else:
        print("Player 1 (" + PLAYER_SYMBOL + ")")
        print("Player 2 (" + PLAYER2_SYMBOL + ")")
    display_board()

def play_again(board, game_mode):
    for i in range(3):
        for j in range(3):
            board[i][j] = " "
    while True:
        choice = input("Do you want to play again? (yes/no): ")
        if choice == "y":
            initialize_game(game_mode)
            start_game(game_mode)
            continue
        elif choice == "n":
            exit()
        else:
            print("Invalid choice. Please enter 'yes' or 'no'.")

def start_game(game_mode):
    print("Welcome to Tic Tac Toe game")
    if game_mode == "1":
        while True:
            get_player_move()
            display_board()
            minimax_value = minimax(board, 0, False)
            if check_win(board) == PLAYER_SYMBOL:
                print("Player wins!")
                play_again(board, game_mode)

            elif board_full():
                print("Draw")
                play_again(board, game_mode)

            row, col = best_move(board)
            board[row][col] = AI_SYMBOL
            print(f"AI played at: {row} {col}")
            display_board()
            if check_win(board) == AI_SYMBOL:
                print("AI wins!")
                play_again(board, game_mode)
            elif board_full():
                print("Draw")
                play_again(board, game_mode)
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

# --- Main execution ---
while True:
    game_mode = input("Select game mode:\n1. Player vs AI\n2. Player vs Player\nEnter 1 or 2: ")
    if game_mode in ["1", "2"]:
        break
    print("Invalid choice. Please enter 1 or 2.")

initialize_game(game_mode)
start_game(game_mode)