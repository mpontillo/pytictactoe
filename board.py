#!/usr/bin/env python

from __future__ import print_function


class Board(object):
    def __init__(self):
        self.lastmove = ' '
        self.board = [[' ', ' ', ' '],
                      [' ', ' ', ' '],
                      [' ', ' ', ' ']]

    def display(self):
        print("""\
 %s | %s | %s
---+---+---
 %s | %s | %s
---+---+---
 %s | %s | %s
""" % (
            self.board[0][0], self.board[0][1], self.board[0][2],
            self.board[1][0], self.board[1][1], self.board[1][2],
            self.board[2][0], self.board[2][1], self.board[2][2]))

    def check_win(self, move):
        if ((move == self.board[0][0] == self.board[0][1] == self.board[0][2]) or
            (move == self.board[1][0] == self.board[1][1] == self.board[1][2]) or
            (move == self.board[2][0] == self.board[2][1] == self.board[2][2]) or
            (move == self.board[0][0] == self.board[1][0] == self.board[2][0]) or
            (move == self.board[0][1] == self.board[1][1] == self.board[2][1]) or
            (move == self.board[0][2] == self.board[1][2] == self.board[2][2]) or
            (move == self.board[0][0] == self.board[1][1] == self.board[2][2]) or
            (move == self.board[2][0] == self.board[1][1] == self.board[0][2])):
            print("%s wins!" % (move))
            return True
        elif (self.board[0][0] != ' ' and 
              self.board[0][1] != ' ' and 
              self.board[0][2] != ' ' and
              self.board[1][0] != ' ' and
              self.board[1][1] != ' ' and 
              self.board[1][2] != ' ' and
              self.board[2][0] != ' ' and
              self.board[2][1] != ' ' and
              self.board[2][2] != ' '):
            print("Tie game. Too bad!")
            return True
        else:
            return False

    def move(self, x, y, move):
        move = move.lower()
        if (move != 'x') and (move != 'o'):
            print("Move must be an 'x' or 'o'.")
            return False
        elif (x > 2) or (y > 2) or (x < 0) or (y < 0):
            print("Row and column must be between 0 and 2 (inclusive).")
            return False
        elif self.board[x][y] != ' ':
            print("Illegal move! (move must be made on an empty spot.)")
            return False
        elif self.lastmove == move:
            print("It's not %s's turn." % (move))
            return False
        else:
            self.board[x][y] = move
            if self.check_win(move):
                print("Game over.")
            self.lastmove = move
            return True
