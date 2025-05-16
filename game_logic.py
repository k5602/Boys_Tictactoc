from minimax import best_move, check_win

# Initialize global variables
board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

PLAYER_SYMBOL = "x"
AI_SYMBOL = "o"
PLAYER2_SYMBOL = "o"


def display_board():
    """Display the current state of the board with formatting"""
    print("\nCurrent Board:")
    print("-----------")
    for row in board:
        print("|", end=" ")
        for cell in row:
            print(cell, end=" | ")
        print("\n-----------")


def reset_board():
    """Reset the board to empty state"""
    for i in range(3):
        for j in range(3):
            board[i][j] = " "


def initialize_game(game_mode):
    """Display welcome message, reset board and print empty board"""
    # Reset the board
    reset_board()

    if game_mode == "1":
        print("You are Player 1 (" + PLAYER_SYMBOL + ")")
        print("The AI is (" + AI_SYMBOL + ")")
    else:
        print("Player 1 (" + PLAYER_SYMBOL + ")")
        print("Player 2 (" + PLAYER2_SYMBOL + ")")
    display_board()


def board_full():
    """Check if the board is full (no empty spaces left)"""
    for row in board:
        if " " in row:
            return False
    return True


def get_player_move(player_symbol=PLAYER_SYMBOL, player_number=1):
    """Get and validate the player's move"""
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


def play_again():
    """Ask if the player wants to play again and handle the response"""
    while True:
        choice = input("Do you want to play again? (yes/no): ")
        choice = choice.lower()
        if choice in ["yes", "y"]:
            return main()
        elif choice in ["no", "n"]:
            return False
        else:
            print("Invalid choice. Please enter 'yes' or 'no'.")


def play_player_vs_ai():
    """Handle the Player vs AI game mode"""
    while True:
        # Player's turn
        get_player_move()
        display_board()

        result = check_win(board)
        if result == PLAYER_SYMBOL:
            print("Player wins!")
            if not play_again():
                break
            reset_board()
            display_board()
            continue
        elif board_full():
            print("It's a draw!")
            if not play_again():
                break
            reset_board()
            display_board()
            continue

        # AI's turn
        print("AI is thinking...")
        row, col = best_move(board)
        board[row][col] = AI_SYMBOL
        print(f"AI played at: {row} {col}")
        display_board()

        result = check_win(board)
        if result == AI_SYMBOL:
            print("AI wins!")
            if not play_again():
                break
            reset_board()
            display_board()
            continue
        elif board_full():
            print("It's a draw!")
            if not play_again():
                break
            reset_board()
            display_board()
            continue


def play_player_vs_player():
    """Handle the Player vs Player game mode"""
    current_player = 1
    while True:
        # Get current player's move
        if current_player == 1:
            get_player_move(PLAYER_SYMBOL, 1)
            player_symbol = PLAYER_SYMBOL
        else:
            get_player_move(PLAYER2_SYMBOL, 2)
            player_symbol = PLAYER2_SYMBOL

        display_board()

        result = check_win(board)
        if result == player_symbol:
            print(f"Player {current_player} wins!")
            if not play_again():
                break
            reset_board()
            display_board()
            current_player = 1
            continue
        elif board_full():
            print("It's a draw!")
            if not play_again():
                break
            reset_board()
            display_board()
            current_player = 1
            continue

        current_player = 2 if current_player == 1 else 1


def main():
    """Main game loop"""
    print("\n=== TIC TAC TOE ===")
    print("\nWelcome to Tic Tac Toe game")
    print("A classic game of Xs and Os\n")
    
    while True:
        game_mode = input("Select game mode:\n1. Player vs AI\n2. Player vs Player\nEnter 1 or 2: ")
        if game_mode in ["1", "2"]:
            break
        print("Invalid choice. Please enter 1 or 2.")

    print("\nBoard coordinates are from 0-2 for both row and column")
    print("Example: '1 2' refers to the middle-right position\n")
    
    # Initialize and start the game
    initialize_game(game_mode)

    # Run the appropriate game mode
    if game_mode == "1":
        play_player_vs_ai()
    else:
        play_player_vs_player()

    print("Thanks for playing!")


if __name__ == "__main__":
    main()