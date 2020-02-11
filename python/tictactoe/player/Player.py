class Player:
    """General player class that should not be instantiated.
       Use HumanPlayer and ComputerPlayer instead."""

    def __init__(self):
        self.mark = None

    def get_mark(self):
        return self.mark

    def make_move(self, x, y, board):
        board.set_value(x, y, self.get_mark())
