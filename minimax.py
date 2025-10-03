import pygame 
from copy import deepcopy 
from constatnts import RED, WHITE 

class MinimaxAlgorithm:
               
  def mini_max(self, dep, board, if_max): 
    if dep == 0 or board.if_win_the_game() is not None:
        return board.evaluate(), board
    if not if_max:
        return self._minimize(dep, board)
    return self._maximize(dep, board)

        
  def _maximize(self, dep, board):
    best_piece = None
    optimal_action = None
    highest_evaluation = -10**6
    for action, piece in self.all_action(board, WHITE):
        evaluation = self.mini_max(dep - 1, action, False)[0]
        if evaluation >= highest_evaluation:
            highest_evaluation = evaluation
            best_piece = piece
            optimal_action = action
    return highest_evaluation, optimal_action, best_piece


  def _minimize(self, dep, board):
    best_piece = None
    optimal_action = None
    lowest_evaluation = 10**6
    for action, piece in self.all_action(board, RED):
        evaluation = self.mini_max(dep - 1, action, True)[0]
        if evaluation <= lowest_evaluation:
            lowest_evaluation = evaluation
            best_piece = piece
            optimal_action = action
    return lowest_evaluation, optimal_action, best_piece



      
        
  def all_action(self, board, color):
      actions = []
      for obj in board.get_all_pieces(color):
          actual_actions = obj.get_valid_moves(board)
          for action, objects in actual_actions.items():
              temp_board = deepcopy(board)
              temp_obj = temp_board.board[obj.row][obj.col]
              if temp_obj != 0:
                new_board = self.imitate_action(action, temp_obj, objects, temp_board)
                actions.append((new_board, temp_obj))
      return actions


    
  def imitate_action(self, action, piece, objects, board):
      board.move(piece, action[0], action[1])
      if objects:
          board.remove(objects, piece.color)
      return board