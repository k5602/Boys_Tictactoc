import math
scores = {  
    'x': -10,   # Player (minimizing)
    'o': 10,    # AI (maximizing)
    'tie': 0 
} 

def check_win(board):
    """
    Check for a winner or tie on the board.
    Returns 'x' if X wins, 'o' if O wins, 'tie' if draw, or None if game ongoing.
    """
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]
    for row in board:
        if ' ' in row:
            return None
    return 'tie'

def minimax(board, depth, isMaximizing):
    result = check_win(board)
    if result is not None:
        return scores[result]
    if isMaximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'o'  # AI's move (maximizing)
                    score = minimax(board, depth + 1, False)
                    board[i][j] = ' '
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'x'  # Player's move (minimizing)
                    score = minimax(board, depth + 1, True)
                    board[i][j] = ' '
                    best_score = min(score, best_score)
        return best_score

def best_move(board):
    best_score = -math.inf
    move = (0, 0)
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'o'
                score = minimax(board, 0, False)
                board[i][j] = ' '
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

