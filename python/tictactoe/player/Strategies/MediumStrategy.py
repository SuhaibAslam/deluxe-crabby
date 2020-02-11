from random import random

from src.main.python.tictactoe.TicTacToeController import TicTacToeController
from src.main.python.tictactoe.player.Strategies.Strategy import Strategy
from src.main.python.tictactoe.shared.WinningConditions import WinningConditions


class MediumStrategy(Strategy):
    def get_name(self):
        return "Normal"

    def get_move(self, board, mark):

        win = WinningConditions()


        x = -1
        y = -1
        valid_move = False
        while not valid_move:
            x = int(random() * TicTacToeController.dim)
            y = int(random() * TicTacToeController.dim)
            valid_move = (board.valid_field(x, y) and board.is_empty_field(x, y))
        return [x, y]
