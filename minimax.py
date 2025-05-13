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
    # Check rows and columns
    for i in range(3):
        # Check rows
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return board[i][0]
        # Check columns
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return board[0][i]
    
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]
    
    # Check for tie/ongoing game
    if any(' ' in row for row in board):
        return None  # Game still ongoing
    return 'tie'

def minimax(board, depth, alpha, beta, is_maximizing):
    """
    Minimax algorithm with alpha-beta pruning for Tic-Tac-Toe.
    Returns the best score for the current board state.
    """
    # Check if game is over
    result = check_win(board)
    if result is not None:
        return scores[result]
    
    # Get available moves
    available_moves = [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']
    
    if is_maximizing:
        max_score = -math.inf
        for i, j in available_moves:
            board[i][j] = 'o'  # AI's move
            score = minimax(board, depth + 1, alpha, beta, False)
            board[i][j] = ' '  # Undo move
            max_score = max(score, max_score)
            alpha = max(alpha, max_score)
            if beta <= alpha:
                break  # Beta cutoff
        return max_score
    else:
        min_score = math.inf
        for i, j in available_moves:
            board[i][j] = 'x'  # Player's move
            score = minimax(board, depth + 1, alpha, beta, True)
            board[i][j] = ' '  # Undo move
            min_score = min(score, min_score)
            beta = min(beta, min_score)
            if beta <= alpha:
                break  # Alpha cutoff
        return min_score

def best_move(board):
    """
    Finds the best move for the AI using the minimax algorithm.
    Returns a tuple (row, col) representing the best move.
    """
    best_score = -math.inf
    move = None
    
    # Try each available move
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'o'  # AI's move
                score = minimax(board, 0, -math.inf, math.inf, False)
                board[i][j] = ' '  # Undo move
                
                if score > best_score:
                    best_score = score
                    move = (i, j)
    
    return move or (0, 0)  # Default to (0,0) if no moves available