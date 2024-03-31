import pygame

from .constatnts import BLACK, ROWS, COLS, RED, SQUARE_SIZE, WHITE
from .piece import Piece
import math as m

class Board:
  PADDING = 10
  def __init__(self):
    self.board = []
    self.boardOfBlue = []
    self.selected_piece = None
    self.red_left = self.white_left = 12
    self.red_kings = self.white_kings = 0
    self.create_board()
    
  
  def draw_squares(self,win):
    win.fill(BLACK)
    for row in range(ROWS):
        for col in range(row % 2, ROWS, 2):
           pygame.draw.rect(win,RED,(row*SQUARE_SIZE,col*SQUARE_SIZE,SQUARE_SIZE,SQUARE_SIZE))

  def create_board(self):
     for row in range(ROWS):
        self.board.append([ ])
        for col in range(COLS):
            if col % 2 == ((row + 1) % 2):
              if row < 3:
                 
                 obj = Piece(row, col, WHITE)
                 
                 self.board[row].append(obj)
              elif row > 4:
                 obj = Piece(row, col, RED)
                 self.board[row].append(obj)

              else:
                 
                 self.board[row].append(0)
            else:
                self.board[row].append(0)

  def draw(self,win):
     self.draw_squares(win)
     for row in range(ROWS):
        for col in range(COLS):
           piece = self.board[row][col]
           if piece != 0:
              piece.draw(win)

  def choose_a_pown(self,pos):
     for n in range(ROWS):
        for x in range(COLS):
           if ( n * SQUARE_SIZE <= pos[1] and pos[1] <= n * SQUARE_SIZE + SQUARE_SIZE ) and ( x * SQUARE_SIZE <= pos[0] and pos[0] <= x * SQUARE_SIZE + SQUARE_SIZE ):
              if self.board[n][x] != 0:
                 
                 middleX, middleY = self.board[n][x].center
                 radius = SQUARE_SIZE//2 - self.PADDING 
                 d = m.sqrt((pos[1] - middleX)**2 + (pos[0] - middleY)**2)
                 if radius >= d:
                    return self.board[n][x]
     return 0
  
  
  
  
              
              