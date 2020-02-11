from src.main.python.tictactoe.shared.Mark import Mark
from src.main.python.tictactoe.shared.WinningConditions import WinningConditions

dim = 3


class Board:
    def __init__(self):
        """Initialise the Board by filling it with empty marks"""

        self.fields = []
        for i in range(dim):
            self.fields.append([])
            for j in range(dim):
                self.fields[i].append(Mark.EMPTY)

        self.win = WinningConditions(self.fields, dim)

    @staticmethod
    def copy(board):
        """Copy an entire board and return the copy"""
        copy = Board()
        for x in range(dim):
            for y in range(dim):
                copy.set_value(x, y, board.get_value(x, y))

        return copy

    def set_value(self, x, y, mark):
        self.fields[x][y] = mark

    def set_move(self, move, mark):
        self.set_value(move[0], move[1], mark)

    def get_value(self, x, y):
        return self.fields[x][y]

    @staticmethod
    def valid_field(x, y):
        return x >= 0 & x < dim & y >= 0 & y < dim

    def is_empty_field(self, x, y):
        return self.get_value(x, y).equals(Mark.EMPTY)

    def is_full(self):
        for x in range(dim):
            for y in range(dim):
                if self.get_value(x, y).equals(Mark.EMPTY):
                    return False
        return True

    def game_over(self):
        return self.is_full() | self.win.has_winner()

    def get_win(self):
        return self.win

    def to_led_array(self):
        leds = 0b000000000000000000

        for rows in self.fields:
            for field in rows:
                if field.equals(Mark.EMPTY):
                    leds = leds << 2 | 0b00
                elif field.equals(Mark.XX):
                    leds = leds << 2 | 0b01
                elif field.equals(Mark.OO):
                    leds = leds << 2 | 0b10
        return leds
