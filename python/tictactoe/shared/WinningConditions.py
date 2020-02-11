from src.main.python.tictactoe.shared.Mark import Mark


class WinningConditions:
    def __init__(self, fields, dim):
        self.board = fields
        self.dim = dim

    def has_winner(self):
        return self.is_winner(Mark.XX) or self.is_winner(Mark.OO)

    def update_board(self, old_board):
        self.board = old_board

    def is_winner(self, mark):
        return (self.has_row(mark) or self.has_column(mark) or self.has_diagonal(mark)) and mark.not_equals(Mark.EMPTY)

    def has_row(self, mark):
        for y in self.dim:
            row = self.board.fields[y]
            if row[0].equals(row[1]).equals(row[2]).equals(mark):
                return True
        return False

    def has_column(self, mark):
        col = []
        for x in self.dim:
            for y in self.dim:
                col.append(self.board.fields[x][y])
            if col[0].equals(col[1]).equals(col[2]).equals(mark):
                return True
        return False

    def has_diagonal(self, mark):
        return self.has_diagonal_left(mark) or self.has_diagonal_right(mark)

    def has_diagonal_left(self, mark):
        pass

    def has_diagonal_right(self, mark):
        pass
