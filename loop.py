#!/usr/bin/env python

from __future__ import print_function

from board import Board

def main():
    board = Board()
    board.lastmove = 'x'
    turn = 'o'
    while not board.check_win(board.lastmove):
        board.display()
        got_move = False
        print("It's " + turn + "'s turn.")
        while not got_move:
            movex = raw_input("     Enter row number (0-2): ")
            movey = raw_input("  Enter column number (0-2): ")
            try:
                movex = int(movex)
                movey = int(movey)
                got_move = True
            except ValueError:
                got_move = False
        board.move(movex, movey, turn)
        if board.lastmove == 'o':
            turn = 'x'
        elif board.lastmove == 'x':
            turn = 'o'
        print('')
    # For posterity.
    board.display()

if __name__ == '__main__':
    main()
