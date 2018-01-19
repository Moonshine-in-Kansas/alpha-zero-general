import numpy as np

class RandomPlayer():
    def __init__(self, game):
        self.game = game

    def play(self, board):
        a = np.random.randint(self.game.getActionSize())
        valids = self.game.getValidMoves(board, 1)
        while valids[a]!=1:
            a = np.random.randint(self.game.getActionSize())
        return a


class HumanConnectfourPlayer():
    def __init__(self, game):
        self.game = game

    def play(self, board):
        # display(board)
        valid = self.game.getValidMoves(board, 1)
        for i in range(len(valid)):
            if valid[i]:
                print(int(i%self.game.n))
        while True:
            a = input()
            try:
                y = int(a)
            except:
                print('Could not parse input')
                continue
            if not(y in range(board.shape[0])):
                print('Out of bounds')
                continue
            a = y
            if valid[a]:
                break
            else:
                print('Invalid')
        return a
