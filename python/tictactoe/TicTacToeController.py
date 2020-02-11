from src.main.python import SPI
from src.main.python.SPI import SPIhandler
from src.main.python.tictactoe.player.ComputerPlayer import ComputerPlayer
from src.main.python.tictactoe.shared.Board import Board
from src.main.python.tictactoe.shared.Mark import Mark


class TicTacToeController:
    dim = 3
    game_over = False
    your_turn = True  # Human player always begins the game
    winner = "ONGOING"

    def play_game(self, difficulty):
        board = Board()

        spi = SPIhandler()

        while not self.game_over:
            if self.your_turn:
                input_given = False
                receive = ""

                while not input_given:
                    receive = spi.xfer()

                    if not receive.equals(SPI.EMPTY_LIST):
                        input_given = True

                move = self.data_to_move(receive)
                board.set_move(move, Mark.XX)
                leds = board.to_led_array()
                spi.xfer(leds)
                self.your_turn = False
            else:
                ai = ComputerPlayer(difficulty)
                board.set_move(ai.do_turn(board), ai.get_mark())
                self.your_turn = True

            self.game_over = board.game_over()

        if board.is_full():
            self.winner = "TIE"
        elif board.get_win().is_winner(Mark.XX):
            self.winner = "WIN"
        elif board.get_win().is_winner(Mark.OO):
            self.winner = "LOST"

    @staticmethod
    def data_to_move(recv):
        x = -1
        y = -1
        i = 0
        while i < len(recv):
            if recv[i] == 1:
                x = i % 3
                if i < 3:
                    y = 0
                elif 2 < i < 6:
                    y = 1
                elif i > 5:
                    y = 2
                break
            i += 1

        return [x, y]

    def get_game_over(self):
        return self.game_over

    def is_your_turn(self):
        return self.your_turn

    def get_winner(self):
        return self.winner
