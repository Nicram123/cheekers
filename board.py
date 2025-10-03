import pygame

from piece import Piece
from constatnts import COLS, RED, BLACK, ROWS, GREEN, SQUARE_SIZE, WHITE
import math as m

class Board:
  PADDING = 10
  def __init__(self):
    self.board = [] # lista list reprezentujaca plansze gdzie wystepuja obiekty Piece lub 0 (gdzie brak pionka)
    self.possible_places_to_move = [] # lista przechowujaca mozliwe ruchy dla zaznaczonego pionka 
    self.selected_piece = None  
    self.red_count = 12
    self.white_count = 12
    self.number_of_kings_red = 0 
    self.number_of_kings_white = 0
    self.turn = RED
    self.king_piece = [] 
    self.create_board()
   
  # Funckja oceny dla algorytmu minimax uwzgledniajaca liczbe pionkow i damki 
  def evaluate(self): 
    return self.white_count - self.red_count  + (self.number_of_kings_white * 0.5 - self.number_of_kings_red * 0.5)
   
  # uzywana w imitate_action w minimax.py do usunicia zbitych pionkow przy symulacji ruchow
  def remove(self, objects):  
    for obj in objects:
        self.board[obj.row][obj.col] = 0
  
  # metoda do odswiezania liczby pionkow (uzywana w main.py po ruchu AI) 
  def refresh_counts(self):
    self.red_count = len(self.get_all_pieces(RED))
    self.white_count = len(self.get_all_pieces(WHITE)) 
            

  def move(self, piece, row, col):
    self.board[piece.row][piece.col], self.board[row][col] = 0, piece
    piece.row, piece.col = row, col 
    piece.center = (piece.row*SQUARE_SIZE + SQUARE_SIZE//2,piece.col * SQUARE_SIZE +SQUARE_SIZE//2) 
    piece.calc_pos()
    piece.ifKing()
    # ewentualnie obsługa damki

  # pobiera wszystkie pionki danego koloru z aktualnej planszy 
  def get_all_pieces(self, color):
    return [obj for row in self.board for obj in row if obj != 0 and obj.color == color]

  #def get_all_pieces(self, color):  # get_all_pieces 
  # objects = []
  # for row in self.board:
  #     for obj in row:
  #         if obj != 0 and obj.color == color:
  #             objects.append(obj)
  # return objects
  
  # wyswietla wszystkie pionki danego koloru na planszy 
  def display_all_pieces(self, color, WIN):
      for row in self.board:
         for obj in row:
               if obj != 0 and obj.color == color:
                  obj.draw(WIN)
      
  
  def if_win_the_game(self):
    if self.red_count <= 0:
        return WHITE
    elif self.white_count <= 0:
        return RED
    return None
  
  def draw_squares(self,win):
    win.fill(BLACK)
    for row in range(ROWS):
        for col in range(row % 2, ROWS, 2):
           pygame.draw.rect(win,GREEN,(row*SQUARE_SIZE,col*SQUARE_SIZE,SQUARE_SIZE,SQUARE_SIZE))

  def get_board(self):
    return self.board
   
  #def create_board(self):
  ##   for row in range(ROWS):
  #      self.board.append([ ])
  #      for col in range(COLS):
  #          if col % 2 == ((row + 1) % 2):
  #            if row < 3:    
  #3               obj = Piece(row, col, WHITE)
  #               self.board[row].append(obj)
  #            elif row > 4:
  #               obj = Piece(row, col, RED)
  #               self.board[row].append(obj)
  #
  #            else:
  #               
  #               self.board[row].append(0)
  #          else:
  #              self.board[row].append(0)
                
  # wypelnianie planszy board (listy list) pionkami lub 0 na poczatku gry
  def create_board(self):
    self.board = []
    for r in range(ROWS):
        row = []
        for c in range(COLS):
            if self.should_have_piece(r, c):
                color = WHITE if r < 3 else RED if r > 4 else None
                row.append(Piece(r, c, color) if color else 0)
            else:
                row.append(0)
        self.board.append(row)
  
   
  # sprawdza czy na danym polu powinnien byc pionek (czarne pola i odpowiednie rzędy)
  def should_have_piece(self, r: int, c: int) -> bool:
    # na czarnych polach postawione pionki 
    if (r + c) % 2 == 0:
        return False
    # białe pionki w pierwszych 3 rzędach
    if r < 3:
        return True
    # czerwone pionki w ostatnich 3 rzędach
    if r > ROWS - 4:  # np. przy ROWS = 8 => r > 4
        return True
    return False
              
                

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
  
  # Zmiana tury przy kazdym ruchu (na zmiane player - RED, AI - WHITE)
  def change_turn(self):
    self.turn = RED if self.turn == WHITE else WHITE
  
  
  
  
              
              