from copy import deepcopy 
import pygame 

RED = (255, 0, 0) 
WHITE = (255, 255, 255) 

def minimax(position, depth, max_player, game, win):
    if depth == 0 or position.winner() != None:
         return position.evaluate(), position
    if max_player:
        maxEval = float('-inf')
        best_move = None
        best_piece = None
        for move, piece in get_all_moves(position, WHITE, game, win):
            evaluation = minimax(move, depth - 1, False, game, win)[0]
            maxEval = max(maxEval, evaluation)
            if maxEval == evaluation:
                best_move = move
                best_piece = piece
        return maxEval, best_move, best_piece 
      
    else:
        minEval = float('inf')
        best_move = None
        best_piece = None
        for move, piece in get_all_moves(position, RED, game, win):
            evaluation = minimax(move, depth - 1, True, game, win)[0]
            minEval = min(minEval, evaluation)
            if minEval == evaluation:
                best_move = move 
                best_piece = piece 
        return minEval, best_move, best_piece
      
def get_all_moves(position, color, game, win):
    moves = []
    for piece in position.get_all_pieces(color):
        valid_moves = piece.get_valid_moves(position)
        #print(f'Piece {piece.row},{piece.col} color={piece.color} valid_moves={valid_moves}')
        for move, skip in valid_moves.items():
            temp_board = deepcopy(position)
            temp_piece = temp_board.board[piece.row][piece.col]
            if temp_piece != 0:
              new_board = simulate_move(temp_piece, move, temp_board, game, skip, win)
              moves.append((new_board, temp_piece))
    #print(f'All moves for color {color}: {len(moves)}')
    return moves
  
def simulate_move(piece, move, board, game, skip, win):
    board.move(piece, move[0], move[1], win)
    if skip:
        board.remove(skip, piece.color)
    return board