import random

board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

PLAYER_SYMBOL = "x"
AI_SYMBOL = "o"

def display_board():
    print("\nCurrent Board:")
    print("-----------")
    for i, row in enumerate(board):
        print("|", end=" ")
        for j, cell in enumerate(row):
            print(cell, end=" | ")
        print("\n-----------")

def initialize_game():
    """Display welcome message and print empty board"""
    print("Welcome to Tic Tac Toe game")
    print("You are Player 1 (" + PLAYER_SYMBOL + ")")
    print("The AI is (" + AI_SYMBOL + ")")
    display_board()

def get_player_move():
    while True:
        try:
            col = int(input("Enter your column index (0-2): "))
            row = int(input("Enter your row index (0-2): "))

            if 0 <= row <= 2 and 0 <= col <= 2:
                if board[row][col] == " ":
                    board[row][col] = PLAYER_SYMBOL
                    return
                else:
                    print("That position is already taken. Please choose another.")
            else:
                print("Invalid input. Please enter numbers between 0 and 2.")
        except ValueError:
            print("Please enter valid numbers.")

def make_ai_move():
    empty_positions = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                empty_positions.append((i, j))

    if empty_positions:
        row, col = random.choice(empty_positions)
        board[row][col] = AI_SYMBOL
        print(f"AI places {AI_SYMBOL} at position ({row}, {col})")
    else:
        print("No more moves available")
