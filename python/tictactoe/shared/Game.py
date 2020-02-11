from src.main.python.tictactoe.shared.Board import Board
from src.main.python.tictactoe.shared.Mark import Mark


class Game:
    def __init__(self, player1, player2):
        self.human_player = player1
        self.cpu_player = player2
        self.board = Board()
        self.winner = ""

    def get_board(self):
        return self.board

    def get_winner(self):
        win = self.board.get_win()
        if win.has_winner():
            xx_is_winner = win.is_winner(Mark.XX)
            human_is_xx = self.human_player.get_mark()
            if (human_is_xx and xx_is_winner) or (not human_is_xx and not xx_is_winner):
                self.winner = "You"
            else:
                self.winner = "The computer"
            return self.winner
        return ""

    def get_human_player(self):
        return self.human_player

    def get_cpu_player(self):
        return self.cpu_player
