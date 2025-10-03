from copy import deepcopy 
import pygame 
from constatnts import RED, WHITE 

def mini_max(dep, board, if_max): # position, depth, max_player, game, win
    if dep == 0 or board.if_win_the_game() != None:
         return board.evaluate(), board 
    if if_max:
        best_piece = None
        optimal_action = None
        highest_evaluation = -1_000_000
        for action, piece in all_action(board, WHITE):
            evaluation = mini_max(dep - 1, action, False)[0]
            highest_evaluation = max(highest_evaluation, evaluation)
            if highest_evaluation == evaluation:
                optimal_action = action
                best_piece = piece
        return highest_evaluation, optimal_action, best_piece   
    else:
        best_piece = None
        optimal_action = None
        lowest_evaluation = 1_000_000
        for action, piece in all_action(board, RED):
            evaluation = mini_max(dep - 1, action, True)[0]
            lowest_evaluation = min(lowest_evaluation, evaluation)
            if lowest_evaluation == evaluation:
                optimal_action = action 
                best_piece = piece 
        return lowest_evaluation, optimal_action, best_piece

    
      
def all_action(board, color):
    actions = []
    for piece in board.get_all_pieces(color):
        actual_actions = piece.get_valid_moves(board)
        for action, objects in actual_actions.items():
            temp_board = deepcopy(board)
            temp_piece = temp_board.board[piece.row][piece.col]
            if temp_piece != 0:
              new_board = imitate_action(temp_piece, action, temp_board, objects)
              actions.append((new_board, temp_piece))
    return actions
  
def imitate_action(piece, action, board, objects):
    board.move(piece, action[0], action[1])
    if objects:
        board.remove(objects)
    return board