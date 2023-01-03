#!/usr/bin/python3

import sys


def printBoard(board):
    if any(1 in x for x in board):
        print([[idx, board[idx].index(1)] for idx, val in enumerate(board)])
