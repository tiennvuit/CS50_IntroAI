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
    X_count = 0
    O_count = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'X':
                X_count += 1
            elif board[i][j] == 'O':
                O_count += 1
    if X_count <= O_count:
        return 'X'
    return 'O'

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
    new_board = copy_board(board)
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
    if board[0][0] == board[1][0] and board[1][0] == board[2][0] and board[0][0] != None:
        return board[0][0] 
    if board[0][1] == board[1][1] and board[1][1] == board[2][1] and board[0][1] != None:
        return board[0][1]
    if board[0][2] == board[1][2] and board[1][2] == board[2][2] and board[0][2] != None:
        return board[0][2]
    
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
    

def copy_board(board):
    new_board = [[None]*3, [None]*3, [None]*3]
    for i in range(3):
        for j in range(3):
            new_board[i][j] = board[i][j]
    return new_board


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    legal_actions = actions(board)
    for action in legal_actions:   
        # Check whether the computer have win chance or not 
        newboard = result(board, action)
        if winner(newboard) == 'X' or winner(newboard) == 'O':
            return action
    # Check whether the user have win change
    for action in legal_actions:
        newboard = copy_board(board)
        newboard[action[0]][action[1]] = 'O'
        if winner(newboard) == 'O':
            return action
    
    return random.choice(legal_actions)
