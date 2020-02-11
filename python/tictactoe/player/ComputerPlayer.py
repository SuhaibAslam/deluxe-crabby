from src.main.python.tictactoe.player.Player import Player
from src.main.python.tictactoe.player.Strategies.EasyStrategy import EasyStrategy
from src.main.python.tictactoe.player.Strategies.HardStrategy import HardStrategy
from src.main.python.tictactoe.player.Strategies.MediumStrategy import MediumStrategy
from src.main.python.tictactoe.shared.Mark import Mark


class ComputerPlayer(Player):

    # noinspection PyMissingConstructor
    def __init__(self, difficulty):
        self.mark = Mark.OO
        difficulty.toUpperCase()
        if difficulty.equals("EASY"):
            self.strategy = EasyStrategy()
        elif difficulty.equals("NORMAL"):
            self.strategy = MediumStrategy()
        elif difficulty.equals("HARD"):
            self.strategy = HardStrategy()
        else:
            self.strategy = EasyStrategy()

    def do_turn(self, board):
        return self.strategy.get_move(board, self.mark)
