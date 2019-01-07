# -*- encoding: utf-8 -*-
from . import board
import os

UNICODE_PIECES = {
  'r': '♜', 'n': '♞', 'b': '♝', 'q': '♛',
  'k': '♚', 'p': '♟', 'R': '♖', 'N': '♘',
  'B': '♗', 'Q': '♕', 'K': '♔', 'P': '♙',
  None: ' '
}

class BoardGuiConsole(object):
    '''
        Print a text-mode chessboard using the unicode chess pieces
    '''
    error = ''

    def __init__(self, chessboard):
        self.board = chessboard

    def move(self):
        os.system("clear")
        self.unicode_representation()
        print("\n", self.error)
        print("State a move in chess notation (e.g. A2A3). Type \"exit\" to leave:\n", ">>>", end=' ')
        self.error = ''
        coord = input()
        if coord == "exit":
            print("Bye.")
            exit(0)
        try:
            if len(coord) != 4: raise board.InvalidCoord
            self.board.move(coord[0:2], coord[2:4])
            os.system("clear")
        except board.ChessError as error:
            self.error = "Error: %s" % error.__class__.__name__

        self.move()

    def unicode_representation(self):
        print("\n", ("%s's turn\n" % self.board.player_turn.capitalize()).center(28))
        for number in self.board.axis_x[::-1]:
            print(" " + str(number) + " ", end=' ')
            for letter in self.board.axis_y:
                piece = self.board[letter+str(number)]
                if piece is not None:
                    print(UNICODE_PIECES[piece.abbriviation] + ' ', end=' ')
                else: print('  ', end=' ')
            print("\n")
        print("    " + "  ".join(self.board.axis_y))


def display(board):
    try:
        gui = BoardGuiConsole(board)
        gui.move()
    except (KeyboardInterrupt, EOFError):
        os.system("clear")
        exit(0)
