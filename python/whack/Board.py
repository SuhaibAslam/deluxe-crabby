from random import randint
from time import sleep, time

from src.main.python.tictactoe.shared.Mark import Mark


class Board:
    grid_size = 3

    def __init__(self, difficulty, duration):
        self.finished = False
        self.grid = []
        self.difficulty = difficulty
        self.duration = duration

        for i in range(self.grid_size):
            self.grid.append([Mark()] * self.grid_size)

    def valid_field(self, x, y):
        if 0 <= x < self.grid_size and 0 <= y < self.grid_size:
            return True
        else:
            return False

    def set_field(self, x, y, val):
        if self.valid_field(x, y):
            self.grid[x][y] = val
        else:
            raise ValueError('Index out of range. ')

    def get_field(self, x, y):
        if self.valid_field(x, y):
            return self.grid[x][y]
        else:
            raise ValueError('Index out of range. ')

    def copy(self):
        n = self.grid_size
        copy = Board(self.difficulty, self.duration)

        for i in range(n):
            for j in range(n):
                copy.set_field(i, j, self.get_field(i, j))

    def touch(self, x, y):
        if self.finished:
            return 'FINISHED'
        elif self.get_field(x, y) == Mark.MOLE:
            self.set_field(x, y, Mark.HIT)
            self.finished = True
            return 'HIT'
        else:
            self.set_field(x, y, Mark.TOUCH)
            return 'MISS'

    def mole(self):
        start = time()

        if self.difficulty == 'EASY':
            rtime = 1500
        elif self.difficulty == 'HARD':
            rtime = 500
        elif self.difficulty == 'IMPOSSIBLE':
            rtime = 200
        else:
            rtime = 1500

        x = randint(0, self.grid_size)
        y = randint(0, self.grid_size)

        while time() - start < self.duration:
            self.set_field(x, y, Mark.MOLE)
            sleep(rtime)

            if self.get_field(x, y) != Mark.HIT:
                self.set_field(x, y, Mark.EMPTY)
            else:
                break

            x = randint(0, self.grid_size)
            y = randint(0, self.grid_size)
