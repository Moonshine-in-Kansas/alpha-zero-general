from Arena import Arena
from MCTS import MCTS
from connectfour.ConnectfourGame import ConnectfourGame, display
from connectfour.ConnectfourPlayers import *
from connectfour.tensorflow.NNet import NNetWrapper as nn

import numpy as np
from utils import *


from Coach import Coach
"""
use this script to play any two agents against each other, or play manually with
any agent.
"""


g = ConnectfourGame(7)

# all players
rp = RandomPlayer(g).play
hp = HumanConnectfourPlayer(g).play

#nnet players

nnet = nn(g)
nnet.load_checkpoint('./pretrained_models/connectfour/tensorflow/','best.pth.tar')
print("loaded trained neurual net")
args = dotdict({'numMCTSSims': 100, 'cpuct':1.0})
mcts = MCTS(g, nnet, args)
nnp = lambda x: np.argmax(mcts.getActionProb(x, temp=1))


n2 = nn(g)
n2.load_checkpoint('./temp/','checkpoint_0.pth.tar')
print("loaded trained neurual net")
args2 = dotdict({'numMCTSSims': 100, 'cpuct':1.0})
mcts2 = MCTS(g, n2, args2)
n2p = lambda x: np.argmax(mcts2.getActionProb(x, temp=1))


arena = Arena(nnp, rp, g, display=display)
print(arena.playGames(100, verbose=True))

