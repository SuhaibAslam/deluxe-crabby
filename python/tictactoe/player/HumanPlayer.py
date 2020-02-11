from src.main.python.tictactoe.player.Player import Player
from src.main.python.tictactoe.shared.Mark import Mark


class HumanPlayer(Player):
    # noinspection PyMissingConstructor
    def __init__(self):
        self.mark = Mark.XX
