from enum import Enum


class Mark(Enum):
    """
    Class is used as data structure for a mark on the board.
    Can only take the values XX, OO, and EMPTY
    """

    EMPTY = 0
    XX = 1
    OO = 2

    def opposite(self):
        """Give the opposite mark"""
        if self.mark == Mark.XX:
            return Mark.OO
        elif self.mark == Mark.OO:
            return Mark.XX
        else:
            return Mark.EMPTY
