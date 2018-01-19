# Connect Four implementation for Alpha Zero General

An implementation of Connect Four using tensorflow.  Neural network architecture for a 7x7 board was copy-pasted from the game of Othello, so possibly it can be simplified. 

To start training a model for Connect Four:
```bash
python main4.py
```
To start a tournament of 100 episodes with the model-based player against a random player:
```bash 
python pit4.py ```
You can play againt the model by switching to HumanPlayer in ```
python pit4.py```

### Experiments
I trained a tensor flow model for about 10 iterations, 100 episodes, 10 epochs per iteration and 100 MCTS simulations per turn. This took two days on a Ryzen 1700X processor. 
The pretrained model (tensorflow) can be found in ```pretrained_models/connectfour/tensorflow/```. You can play a game against it using ```pit4.py```. 

### Contributors and Credits
* [Gerald Hoehn](https://github.com/Moonshine-in-Kansas)

The implementation is based on the game of Othello and TicTacToe (https://github.com/suragnair/alpha-zero-general/tree/master/othello).