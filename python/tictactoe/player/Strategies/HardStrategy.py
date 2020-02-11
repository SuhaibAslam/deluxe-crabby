from random import random

from src.main.python.tictactoe.TicTacToeController import TicTacToeController
from src.main.python.tictactoe.player.Strategies.Strategy import Strategy


class HardStrategy(Strategy):
    def get_name(self):
        return "Hard"

    def get_move(self, board, mark):
        x = -1
        y = -1
        valid_move = False
        while not valid_move:
            x = int(random() * TicTacToeController.dim)
            y = int(random() * TicTacToeController.dim)
            valid_move = (board.valid_field(x, y) and board.is_empty_field(x, y))
        return [x, y]
