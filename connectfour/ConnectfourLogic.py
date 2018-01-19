'''
Board class for the game of ConnectFour.
Default board size is 7x6.
Board data:
  1=white(O), -1=black(X), 0=empty
  first dim is column , 2nd is row:
     pieces[0][0] is the top left square,
     pieces[2][0] is the bottom left square,
Squares are stored and manipulated as (x,y) tuples.

by Gerald and Philipp Hoehn

Based on the board for the game of Othello by Eric P. Nichols.

'''

class Board():

    # list of all 8 directions on the board, as (x,y) offsets
    #__directions = [(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1),(0,1)]

    def __init__(self, n=7):
        "Set up initial board configuration."

        self.n = n
        # Create the empty board array.
        self.pieces = [None]*(self.n)
        for i in range(self.n):
            self.pieces[i] = [0]*(self.n)

    # add [][] indexer syntax to the Board
    def __getitem__(self, index): 
        return self.pieces[index]

    def get_legal_moves(self, color):
        """Returns all the legal moves for the given color.
        (1 for white, -1 for black)
        @param color not used and came from previous version.        
        """
        moves = set()  # stores the legal moves.

        # Get all the empty columns (color==0)
        for y in range(self.n):
            if self[0][y]==0:
                newmove = (y)
                moves.add(newmove)
        return list(moves)

    def has_legal_moves(self):
        for y in range(self.n):
            if self[0][y]==0:
                return True
        return False
    
    def is_win(self, color):
        """Check whether the given player has collected a line of length 4 in any direction; 
        @param color (1=white,-1=black)
        """
        # check columns
        for y in range(self.n):
            for x in range(self.n-4):
                if self[x][y]==color and self[x+1][y]==color and self[x+2][y]==color and self[x+3][y]==color:
                    return True
        # check rows
        for y in range(self.n-3):
            for x in range(self.n-1):
                if self[x][y]==color and self[x][y+1]==color and self[x][y+2]==color and self[x][y+3]==color:
                    return True 
        # check two diagonal strips
        for y in range(self.n-3):
            for x in range(self.n-4):
                if self[x][y]==color and self[x+1][y+1]==color and self[x+2][y+2]==color and self[x+3][y+3]==color:
                    return True
        for y in range(self.n-3):
            for x in range(3,self.n-1):
                if self[x][y]==color and self[x-1][y+1]==color and self[x-2][y+2]==color and self[x-3][y+3]==color:
                    return True    
        return False

    def execute_move(self, move, color):
        """Perform the given move on the board; 
        color gives the color pf the piece to play (1=white,-1=black)
        """
        (x,y) = move
        # Add the piece to the lowest empty square of that column
        assert self[0][y] == 0
        low=0
        for x in range((self.n)-1):
            if self[x][y]== 0:
                low=x
        self[low][y] = color

