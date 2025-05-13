import random

matrix = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
player1 = "x"
AI = "o"

def tic_tac_toe():
    print("Welcome to Tic Tac Toe game")
    print("You are Player 1 (x)")
    print("The AI is (o)")
    
    for row in matrix:
        print(row)

def print_board():
    for row in matrix:
        print(row)

def check_win(player):
    for i in range(3):
        if matrix[i][0] == matrix[i][1] == matrix[i][2] == player:
            return True
        if matrix[0][i] == matrix[1][i] == matrix[2][i] == player:
            return True
    if matrix[0][0] == matrix[1][1] == matrix[2][2] == player:
        return True
    if matrix[0][2] == matrix[1][1] == matrix[2][0] == player:
        return True
    return False

def board_full():
    for row in matrix:
        if " " in row:
            return False
    return True

def check_player():
    while True:
        col = int(input("Enter your column index (0-2): "))
        row = int(input("Enter your row index (0-2): "))
        if 0 <= row <= 2 and 0 <= col <= 2:
            if matrix[row][col] == " ":
                matrix[row][col] = player1
                break
            else:
                print("please choose another place: ")
        else:
            print("invalid place,please choose number between (0-2): ")


def check_ai():
    list = []
    for i in range(3):
        for j in range(3):
            if matrix[i][j] == " ":
                list.append((i , j))
    if list:
        row , col = random.choice(list)

tic_tac_toe()

while True:
    check_player()
    print_board()

    if check_win(player1):
        print("player 1 is win")
        break
    elif board_full():
        print("Draw")
        break

    check_ai()
    print_board()

    if check_win(AI):
        print("AI is win")
        break
    elif board_full():
        print("Draw")
        break