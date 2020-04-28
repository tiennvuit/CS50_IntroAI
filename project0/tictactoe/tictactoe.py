"""
Tic Tac Toe Player
"""

import math
import random

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
    X_count = board.count('X')
    Y_count = board.count('Y')
    if not(X_count + Y_count < 9):
        return None
    return 'X' if X_count < Y_count else 'O'


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    legal_moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == None:
                legal_moves.append((i, j))
    return legal_moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = [[0]*3, [0]*3, [0]*3]
    for i in range(3):
        for j in range(3):
            new_board[i][j] = board[i][j]
    new_board[action[0]][action[1]] = player(new_board)
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check vertical
    if board[0][0] == board[0][1] and board[0][1] == board[0][2] and board[0][0] != None:
        return board[0][0] 
    if board[1][0] == board[1][1] and board[1][1] == board[1][2] and board[1][0] != None:
        return board[1][0]
    if (board[2][0] == board[2][1] and board[2][1] == board[2][2]) and board[2][0] != None:
        return board[2][0]

    # Check horizontal
    if board[0][0] == board[0][1] and board[0][1] == board[0][2] and board[0][0] != None:
        return board[0][0] 
    if board[1][0] == board[1][1] and board[1][1] == board[1][2] and board[1][0] != None:
        return board[1][0]
    if board[2][0] == board[2][1] and board[2][1] == board[2][2] and board[2][0] != None:
        return board[2][0]
    
    # Check diagones
    if (board[0][0] == board[1][1] and board[1][1] == board[2][2]) or (board[0][2] == board[1][1] and board[1][1] == board[2][0]):
        if board[1][1] != None:
            return board[1][1]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    for i in range(0, 3):
        for j in range(0, 3):
            if board[i][j] == None:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)
    if win == 'X':
        return 1
    if win == 'O':
        return -1  
    return 0
    


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    legal_actions = actions(board)
    print(legal_actions)
    for action in legal_actions:
        new_board = result(board, action)
        print(new_board)
        if winner(new_board) is not None:
            return action
    return random.choice(legal_actions)
