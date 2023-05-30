"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy

X = "X"
O = "O"
EMPTY = None

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x = 0
    o = 0
    for box in board:
        for let in box:
            if let == "X" or let == X or let == "x":
                x+=1
            if let == "O" or let == O or let == "o":
                o+=1
    if x > o:
        # O Players Turn
        return O
    # X Players Turn
    return X

    
def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possibleMoves = set()
    for x in range(len(board)):
        for y in range(len(board[x])):
            if board[x][y] == EMPTY:
                possibleMoves.add((x,y))
                
    return possibleMoves



def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    clone = deepcopy(board)
    currentPlayer = player(board)
    x = action[0]
    y = action[1]

    if clone[x][y] != EMPTY:
        # if board spot is taken error 
        raise KeyError
    else:
        # if the board spot is open
        clone[x][y] = currentPlayer
    return clone



def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Checking if rows have a winner
    for row in board:
        x = row.count(X)
        o = row.count(O)
        if x == 3:
            return X
        if o == 3:
            return O
  
    # Checking if columns have a winner
    if board[0][0] == X and board[1][0] == X and board [2][0] == X or board[0][1] == X and board[1][1] == X and board [2][1] == X or board[0][2] == X and board[1][2] == X and board [2][2] == X:
        return X
    elif board[0][0] == O and board[1][0] == O and board [2][0] == O or board[0][1] == O and board[1][1] == O and board [2][1] == O or board[0][2] == O and board[1][2] == O and board [2][2] == O:
        return O
    
    
    # Checking if diganoals have a winner
    elif board[0][0] == X and board[1][1] == X and board[2][2] == X or board[0][2] == X and board[1][1] == X and board[2][0] == X:
        return X
    elif board[0][0] == O and board[1][1] == O and board[2][2] == O or board[0][2] == O and board[1][1] == O and board[2][0] == O:
        return O
    else:
        return None
 

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # if the winnner is not None or every square on the board is filled up, the game is over (TRUE)
    # if the winner is None and not every square on the baord is filled up, return False (game not over)

    gameWinner = winner(board)
    boardFilled = False
    count  = 0
    for r in board:
        for c in r:
            if c == X or c == O:
                count +=1
                
    if count == 9:
        boardFilled = True

    if gameWinner != None or boardFilled:
        return True
    
    if gameWinner == None and boardFilled == False:
        return False


   
def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board):
        w = winner(board)
        if w == X:
            return 1
        elif w == O:
            return -1
        else:
            return 0


def maxPlayer(board):
    if terminal(board):
        return utility(board), None
    
    value = float('-inf')
    move = None

    for action in actions(board):
        
        res, act = minPlayer(result(board, action))

        if res > value:
            value = res
            move = action
            if value == 1:
                return value, move

    return value, move


def minPlayer(board):

    if terminal(board):
        return utility(board), None

    value = float('inf')
    move = None

    for action in actions(board):
       
        res, act = maxPlayer(result(board, action))

        if res < value:
            value = res
            move = action
            if value == -1:
                return value, move

    return value, move

    

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    
    currentPlayer = player(board)
        

    if currentPlayer == X:
        value, bestMove = maxPlayer(board)
        return bestMove

    if currentPlayer == O:
        value, bestMove = minPlayer(board)
        return bestMove


    

