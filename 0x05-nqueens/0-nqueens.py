#!/usr/bin/python3
"""
    0-nqueens mod
"""
import sys


def checkSafe(row, col, board, N):
    """
        checks if a point (row and col) is safe to put a queen
        and returns true if so else returns false
    """
    r = row
    c = col

    # check horizontally upwards
    while r >= 0:
        if board[r][c] == "Queen":
            return False

        r -= 1

    # check left diagonally upwards
    r, c = row, col
    while r >= 0 and c >= 0:
        if board[r][c] == "Queen":
            return False

        r -= 1
        c -= 1

    # check right diagonally upwards
    r, c = row, col
    while r >= 0 and c < N:
        if board[r][c] == "Queen":
            return False

        r -= 1
        c += 1

    return True


def printQueens(board, N):
    """
        prints the points the Queen can stay without
        being attacked
    """
    print([
        [i, j] for i in range(N) for j in range(N) if board[i][j] == "Queen"
        ])


def solveQueens(board, row, N):
    """
        solves the prints the available points a queen
        can be placed without attacking each other
    """
    if row == N:
        printQueens(board, N)
        return

    # loop through columns
    for col in range(N):
        if checkSafe(row, col, board, N):
            board[row][col] = "Queen"
            solveQueens(board, row + 1, N)
            board[row][col] = "empty"


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        num = int(sys.argv[1])
    except Exception:
        print("N must be a number")
        sys.exit(1)
    if num < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [["empty" for i in range(num)] for j in range(num)]
    solveQueens(board, 0, num)
