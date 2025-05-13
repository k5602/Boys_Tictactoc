import math

  
scores = {  
            'X':10 ,
            'O': -10 ,
            'tie': 0 
         } 

def check_result(board):
      """ 
       if winner is 'X' return 1
       if winner is 'O' return -1
       if tie return 0
       if no winner return None
       """
      pass

def minimax(board , depth , isMaximizing):
        result = check_result(board)
        if result != None:
                return scores[result]
        if isMaximizing:
                best_score = -(math.inf)
                for i in range(3):
                    for j in range(3):
                        if board[i][j] == ' ':
                            board[i][j] = 'X' 
                            score = minimax(board , depth + 1 , False) 
                            board[i][j] = ' '
                            best_score = max(score , best_score)
                return best_score

        elif not isMaximizing:
                best_score = (math.inf)
                for i in range(3):
                    for j in range(3):
                        if board[i][j] == ' ':
                            board[i][j] = 'O' 
                            score = minimax(board , depth + 1 , True) 
                            board[i][j] = ' '
                            best_score = min(score , best_score)
                return best_score
        

def best_move(board):
    ai_move = ''
    # if player == 'X':
    #     ai_move = 'O'
    # else:
    #     ai_move = 'X'
    best_score = -(math.inf)
    move = (0, 0) 
    for i in range(3):
        for j in range(3):
                if board[i][j] == ' ' :
                     board[i][j] = ai_move 
                     score = minimax(board , 0 , False) 
                     board[i][j] = ' '
                
                if score > best_score:
                    best_score = score
                    move = (i, j)
               
    return move

