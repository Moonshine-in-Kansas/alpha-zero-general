from __future__ import print_function
import sys
sys.path.append('..')
from Game import Game
from .ConnectfourLogic import Board
import numpy as np


"""
Game class implementation for the game of Connect Four.
Based on the Othello and TicTacToe Game.

Author: Gerald and Philipp Hoehn, github.com/
Date: Jan 18, 2018.

Based on the OthelloGame by Surag Nair.
"""


class ConnectfourGame(Game):
    def __init__(self, n=7):
        self.n = n

    def getInitBoard(self):
        # return initial board (numpy board)
        b = Board(self.n)
        return np.array(b.pieces)

    def getBoardSize(self):
        # (a,b) tuple
        return (self.n, self.n)

    def getActionSize(self):
        # return number of actions
        return self.n + 1

    def getNextState(self, board, player, action):
        # if player takes action on board, return next (board,player)
        # action must be a valid move
        if action == self.n:
        	return (board, -player)
        b = Board(self.n)
        b.pieces = np.copy(board)
        move = (int(action/self.n), action%self.n)
        b.execute_move(move, player)
        return (b.pieces, -player)

    def getValidMoves(self, board, player):
        # return a fixed size binary vector
        valids = [0]*self.getActionSize()
        b = Board(self.n)
        b.pieces = np.copy(board)
        legalMoves =  b.get_legal_moves(player)
        if len(legalMoves)==0:
        	valids[-1]=1
        	return np.array(valids)
        for y in legalMoves:
        	valids[y]=1
        return np.array(valids)

    def getGameEnded(self, board, player):
        # return 0 if not ended, 1 if player 1 won, -1 if player 1 lost
        # player = 1
        b = Board(self.n)
        b.pieces = np.copy(board)
        if b.is_win(player):
        	return 1
        if b.is_win(-player):
            return -1
        if b.has_legal_moves():
            return 0
        # draw has a very little value 
        return 1e-4


    def getCanonicalForm(self, board, player):
        # return state if player==1, else return -state if player==-1
        return player*board

    def getSymmetries(self, board, pi):
        # mirror
        assert(len(pi) == self.n+1)  # 1 for pass
        l = [(board,pi)]
        pi_board = np.reshape(pi[:-1], self.n)
        newB = np.fliplr(board)
        newPi = pi_board[::-1]
        l += [(newB, list(newPi.ravel()) + [pi[-1]])]
        return l

    def stringRepresentation(self, board):
    	# 8x8 numpy array (canonical board)
    	return board.tostring()

    def getScore(self, board, player):
        b = Board(self.n)
        b.pieces = np.copy(board)
        return b.countDiff(player)

def display(board):
    n = board.shape[0]
    print("\n  ",end="")
    for y in range(n):
        print("\u001b[34;1m" + str(y), "", end="")
    print("\u001b[0m")
    print(" \u001b[0m\u001b[32m" + u"\u250C" + u"\u2500" * (n*2-1) + u"\u2510" + "\u001b[0m")
    for y in range(n-1):
        print(" \u001b[0m\u001b[32m" + 	u"\u2502",end="")    # print the row #
        for x in range(n):
            piece = board[y][x]    # get the piece to print
            if piece == 1: print("\u001b[0;1mX\u001b[0m",end="")
            elif piece == -1: print("\u001b[31;1mO\u001b[0m",end="")
            else:
                print("\u001b[32m" + u"\u00B7", end="")
            if x!=n-1: # if not last column print space after piece
                print("\u001b[32m ", end="")
        print("\u001b[32m" + u"\u2502")
    print(" \u001b[0m\u001b[32m" + u"\u2514" + u"\u2500" * (n*2-1) + u"\u2518" + "\u001b[0m\n")

