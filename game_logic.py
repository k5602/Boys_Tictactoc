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

def check_win(player):
    """"check all rows , column and main diagonal """
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True
        if board[0][i] == board[1][i] == board[2][i] == player:
            return True
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

def board_full():
    """check if each board empty or full"""
    for row in board:
        if " " in row:
            return False
    return True

def get_player_move():
    while True:
        try:
            place = input("Enter your index (row then column): ").split()
            if len(place) != 2:
                print("Please enter two numbers separated by a space.")
                continue
            
            row , col = int(place[0]) , int(place[1])

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

initialize_game()

while True:
    get_player_move()
    display_board()
    
    if check_win(PLAYER_SYMBOL):
        print("PLAYER_SYMBOL Win!")
        break
    elif board_full():
        print("Draw")
        break

    make_ai_move()
    display_board()

    if check_win(AI_SYMBOL):
        print("AI_SYMBOL Win!")
        break
    elif board_full():
        print("Draw")
        break