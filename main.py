import pygame
from constatnts import WIDTH, HEIGHT, SQUARE_SIZE, WHITE, RED, BLACK, GREEN 
from board import Board 
from piece import Piece 
from minimax import minimax

FPS = 60
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('checkers game AI')


def main():
  run = True
  clock = pygame.time.Clock()
  board = Board()
  board.draw(WIN)
  first_left_click = True
  obj = 0

  while run:
    clock.tick(FPS)
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False
      if event.type == pygame.MOUSEBUTTONDOWN:
        mouse_position = pygame.mouse.get_pos()
        if obj == 0 or len(board.boardOfBlue) == 0 or ( obj is not isinstance(obj, int) and not obj.returnTrue(board,mouse_position)) :
          obj = board.choose_a_pown(mouse_position)
        elif len(board.boardOfBlue) == 0:
          first_left_click = True
        else:
          first_left_click = False
        if event.button == 1:
          if first_left_click:
            first_left_click = True
            if obj != 0:
              obj.captured_pieces.clear()
              obj.BlueField(WIN,board) # drawing a blue fields
              obj.check_capture_recursive(board,WIN)
          elif not first_left_click and obj is not isinstance(obj, int):
            obj.move(board,WIN,mouse_position)
            first_left_click = True
            board.change_turn()
            if board.turn == WHITE:
                value, new_board, piece_ = minimax(board, 3, True, WIN, WIN)
                board = new_board
                board.draw(WIN, piece_)  # <--- to zamiast manualnego recta
                
                board.change_turn()
                print("AI made a move")
    pygame.display.update()

  pygame.quit()

main()