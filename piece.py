import pygame 
from .constatnts import RED, WHITE, SQUARE_SIZE, GREY, BLUE, ROWS, COLS, BLACK , CROWN
import math as m

class Piece:
  PADDING = 10
  OUTLINE = 2
  captured_pieces = []
  def __init__(self,row,col,color):
    self.row = row
    self.col = col
    self.color = color
    self.king = False
    if self.color == RED:
      self.direction = -1
    else:
      self.direction = 1
    self.x = 0
    self.y = 0
    self.center = (self.row*SQUARE_SIZE + SQUARE_SIZE//2,self.col * SQUARE_SIZE +SQUARE_SIZE//2) 
    self.calc_pos()
  
  def IfCollision(self,obj,row,col):
    if ( obj.board[row][col] == 0):
      return True
    else:
      return False
    
  def returnTrue(self,board,mouse_position):
    for x in range(len(board.boardOfBlue)):
      if ( board.boardOfBlue[x].row * SQUARE_SIZE <= mouse_position[1] <=  board.boardOfBlue[x].row * SQUARE_SIZE + SQUARE_SIZE and
      board.boardOfBlue[x].col * SQUARE_SIZE <= mouse_position[0] <=  board.boardOfBlue[x].col * SQUARE_SIZE + SQUARE_SIZE ):
        return True
      
    return False
  
  def upgrate(self,board,win,ix):
      pygame.draw.rect(win,BLACK,(self.col*SQUARE_SIZE,self.row*SQUARE_SIZE,SQUARE_SIZE,SQUARE_SIZE))
      vi = board.board[self.row][self.col]
      board.board[self.row][self.col] = 0  
      self.row = board.boardOfBlue[ix].row 
      self.col = board.boardOfBlue[ix].col
      self.center = (self.row*SQUARE_SIZE + SQUARE_SIZE//2,self.col * SQUARE_SIZE + SQUARE_SIZE//2)
      board.board[self.row][self.col] = vi
      self.drawBlackSquare(win,board)
      board.boardOfBlue.clear()
      
      
      self.calc_pos()
      self.draw(win)

  def move(self,board,win,mouse_position):

    for x in range(len(board.boardOfBlue)):
      if ( board.boardOfBlue[x].row * SQUARE_SIZE <= mouse_position[1] <=  board.boardOfBlue[x].row * SQUARE_SIZE + SQUARE_SIZE and
      board.boardOfBlue[x].col * SQUARE_SIZE <= mouse_position[0] <=  board.boardOfBlue[x].col * SQUARE_SIZE + SQUARE_SIZE ):
        self.upgrate(board,win,x)
        self.remove(mouse_position[1],mouse_position[0],win,board)
        self.ifKing()
        self.setPicture(win)
        break

  def calc_pos(self):
    self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
    self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

  def make_king(self):
    self.king = True


  def draw(self, win):
    radius = SQUARE_SIZE//2 - self.PADDING 
    pygame.draw.circle(win, GREY, (self.x,self.y), radius + self.OUTLINE)
    pygame.draw.circle(win, self.color, (self.x,self.y), radius)

  
  def check_capture_recursive(self, board, win, captured_pieces_list=None, flag = False, max_depth=20):
    if captured_pieces_list is None:
        captured_pieces_list = []
        
    directions = []
    directions = [(1, -1), (-1, -1), (1, 1), (-1, 1)] if self.king or flag else [(-1, -1), (-1, 1)] if self.color == RED else [(1, -1), (1, 1)]
    flag = True if self.king or flag else False

    for dr, dc in directions:
        r, c = self.row + dr, self.col + dc
        if 0 <= r < len(board.board) and 0 <= c < len(board.board[0]) and board.board[r][c] != 0 and self.color != board.board[r][c].color:
            r, c = r + dr, c + dc
            if 0 <= r < len(board.board) and 0 <= c < len(board.board[0]) and board.board[r][c] == 0:
                if 0 <= r < len(board.board) and 0 <= c < len(board.board[0]) and board.board[r][c] == 0:
                    if board.board[r-dr][c-dc] not in captured_pieces_list:
                        captured_pieces_list.append(board.board[r-dr][c-dc])
                    else:
                        break
                obj = Piece(r, c, self.color)
                obj.row, obj.col = r, c
                board.boardOfBlue.append(obj)
                obj.calc_pos()
                obj.drawBlueCircle(win)
                if max_depth > 0:
                    obj.check_capture_recursive(board, win, captured_pieces_list, flag, max_depth - 1)

    self.captured_pieces.append(captured_pieces_list[:])
    if len(captured_pieces_list) != 0:
      captured_pieces_list.pop()

  def remove(self, finalX, finalY, win, board):
    piece_list = []
    for x in range(len(self.captured_pieces)):
        for y in range(len(self.captured_pieces[x])):
            if self.color == RED or self.king == True:
                if ((self.captured_pieces[x][y].row - 1) * SQUARE_SIZE <= finalX <= (self.captured_pieces[x][y].row - 1) * SQUARE_SIZE + SQUARE_SIZE and 
                    (self.captured_pieces[x][y].col - 1) * SQUARE_SIZE <= finalY <= (self.captured_pieces[x][y].col - 1) * SQUARE_SIZE + SQUARE_SIZE or 
                    (self.captured_pieces[x][y].row - 1) * SQUARE_SIZE <= finalX <= (self.captured_pieces[x][y].row - 1) * SQUARE_SIZE + SQUARE_SIZE and 
                    (self.captured_pieces[x][y].col + 1) * SQUARE_SIZE <= finalY <= (self.captured_pieces[x][y].col + 1) * SQUARE_SIZE + SQUARE_SIZE):
                    piece_list = self.captured_pieces[x]
                    
            if self.color == WHITE or self.king == True:
                if ((self.captured_pieces[x][y].row + 1) * SQUARE_SIZE <= finalX <= (self.captured_pieces[x][y].row + 1) * SQUARE_SIZE + SQUARE_SIZE and 
                    (self.captured_pieces[x][y].col - 1) * SQUARE_SIZE <= finalY <= (self.captured_pieces[x][y].col - 1) * SQUARE_SIZE + SQUARE_SIZE or 
                    (self.captured_pieces[x][y].row + 1) * SQUARE_SIZE <= finalX <= (self.captured_pieces[x][y].row + 1) * SQUARE_SIZE + SQUARE_SIZE and 
                    (self.captured_pieces[x][y].col + 1) * SQUARE_SIZE <= finalY <= (self.captured_pieces[x][y].col + 1) * SQUARE_SIZE + SQUARE_SIZE):
                    piece_list = self.captured_pieces[x]
                    
    for x in range(len(piece_list)):
        pygame.draw.rect(win, BLACK, (piece_list[x].col * SQUARE_SIZE, piece_list[x].row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
        board.board[piece_list[x].row][piece_list[x].col] = 0
        if not self.ClumpingLimit(finalX, finalY, piece_list[x]):
            continue
        else:
            break

    self.captured_pieces.clear()

        
      
  def ClumpingLimit(self, finalX, finalY, obj):
    if self.color == RED or self.king:
        return ((obj.row - 1) * SQUARE_SIZE <= finalX <= (obj.row - 1) * SQUARE_SIZE + SQUARE_SIZE and
                ((obj.col - 1) * SQUARE_SIZE <= finalY <= (obj.col - 1) * SQUARE_SIZE + SQUARE_SIZE or
                 (obj.col + 1) * SQUARE_SIZE <= finalY <= (obj.col + 1) * SQUARE_SIZE + SQUARE_SIZE))
    if self.color == WHITE or self.king:
        return ((obj.row + 1) * SQUARE_SIZE <= finalX <= (obj.row + 1) * SQUARE_SIZE + SQUARE_SIZE and
                ((obj.col - 1) * SQUARE_SIZE <= finalY <= (obj.col - 1) * SQUARE_SIZE + SQUARE_SIZE or
                 (obj.col + 1) * SQUARE_SIZE <= finalY <= (obj.col + 1) * SQUARE_SIZE + SQUARE_SIZE))
    return False


  def drawBlueCircle(self, win):
    radius = SQUARE_SIZE//2 - self.PADDING * 4
    pygame.draw.circle(win, BLUE, (self.x,self.y), radius)
    
  
  def drawBlackSquare(self,win,board):
    for x in range(len(board.boardOfBlue)):
      pygame.draw.rect(win,BLACK,(board.boardOfBlue[x].col*SQUARE_SIZE,board.boardOfBlue[x].row*SQUARE_SIZE,SQUARE_SIZE,SQUARE_SIZE))
  
  def BlueField(self, win, board):
    self.drawBlackSquare(win, board)
    board.boardOfBlue.clear()
    
    newX1 = self.col - 1
    newX2 = self.col + 1
    
    if self.king:
        newY1 = self.row - 1
        newY2 = self.row + 1
           
        for newX, newY in [(newX1, newY2), (newX2, newY2), (newX1, newY1), (newX2, newY1)]:
            if 0 <= newX < COLS and 0 <= newY < ROWS and self.IfCollision(board, newY, newX):
                obj = Piece(newY, newX, self.color)
                board.boardOfBlue.append(obj)
                obj.drawBlueCircle(win)
    
    elif self.color == WHITE:
        newY = self.row + 1
        
        for newX in [newX1, newX2]:
            if 0 <= newX < COLS and 0 <= newY < ROWS and self.IfCollision(board, newY, newX):
                obj = Piece(newY, newX, self.color)
                board.boardOfBlue.append(obj)
                obj.drawBlueCircle(win)
                
    elif self.color == RED:
        newY = self.row - 1
        
        for newX in [newX1, newX2]:
            if 0 <= newX < COLS and 0 <= newY < ROWS and self.IfCollision(board, newY, newX):
                obj = Piece(newY, newX, self.color)
                board.boardOfBlue.append(obj)
                obj.drawBlueCircle(win)

  def ifKing(self):
    if self.color == RED:
      if self.row == 0:
        self.king = True
    else:
      if self.row == ROWS - 1:
        self.king = True
        
        
  def setPicture(self,win):
    if self.king == True:
      win.blit(CROWN, (self.x - CROWN.get_width()//2, self.y - CROWN.get_height()//2))





  