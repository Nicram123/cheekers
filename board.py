import pygame

from constatnts import BLACK, ROWS, COLS, RED, SQUARE_SIZE, WHITE
from piece import Piece
import math as m

class Board:
  PADDING = 10
  def __init__(self):
    self.board = []
    self.boardOfBlue = []
    self.selected_piece = None  
    self.red_left = self.white_left = 12
    self.red_kings = self.white_kings = 0
    self.turn = RED
    self.king_piece = [] 
    self.create_board()
   
  # Min imax evaluation function
  def evaluate(self): 
    return self.white_left - self.red_left  + (self.white_kings * 0.5 - self.red_kings * 0.5)
   
  def remove(self, pieces, color):
    for piece in pieces:
        self.board[piece.row][piece.col] = 0
        if piece.color == RED:
            self.red_left -= 1
        else:
            self.white_left -= 1

  def move(self, piece, row, col, win):
    self.board[piece.row][piece.col], self.board[row][col] = 0, piece
    piece.row, piece.col = row, col 
    piece.center = (piece.row*SQUARE_SIZE + SQUARE_SIZE//2,piece.col * SQUARE_SIZE +SQUARE_SIZE//2) 
    piece.calc_pos()
    piece.ifKing()
    # ewentualnie obsługa damki

  def get_all_pieces(self, color):
    pieces = []
    for row in self.board:
        for piece in row:
            if piece != 0 and piece.color == color:
                pieces.append(piece)
    return pieces
 
  def display_all_pieces(self, color, WIN):
      pieces = []
      for row in self.board:
         for piece in row:
               if piece != 0 and piece.color == color:
                  piece.draw(WIN)
      
  
  def winner(self):
    if self.red_left <= 0:
        return WHITE
    elif self.white_left <= 0:
        return RED
    return None
  
  def draw_squares(self,win):
    win.fill(BLACK)
    for row in range(ROWS):
        for col in range(row % 2, ROWS, 2):
           pygame.draw.rect(win,RED,(row*SQUARE_SIZE,col*SQUARE_SIZE,SQUARE_SIZE,SQUARE_SIZE))

  def get_board(self):
    return self.board
   
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

  def draw(self,win, piece_=None):
     self.draw_squares(win)
     for row in range(ROWS):
        for col in range(COLS):
           piece = self.board[row][col]
           if piece != 0:
              piece.draw(win)
     if piece_ is not None:
         piece_.setPicture(win, self)

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
  
  def change_turn(self):
    self.turn = RED if self.turn == WHITE else WHITE
  
  
  
  
              
              