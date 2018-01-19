from Coach import Coach
from connectfour.ConnectfourGame import ConnectfourGame
from connectfour.tensorflow.NNet import NNetWrapper as nn
from utils import *

args = dotdict({
    'numIters': 10000,
    'numEps': 500,
    'tempThreshold': 42,
    'updateThreshold': 0.60,
    'maxlenOfQueue': 100000,
    'numMCTSSims': 100,
    'arenaCompare': 200,
    'cpuct': 1,

    'checkpoint': './temp/',
    'load_model': True,
    'load_folder_file': ('./temp/','best.pth.tar'),
})

if __name__=="__main__":
    g = ConnectfourGame(7)
    nnet = nn(g)

    if args.load_model:
        nnet.load_checkpoint(args.load_folder_file[0], args.load_folder_file[1])
        print("loaded checkpoint")

    c = Coach(g, nnet, args)
    c.learn()
