#!/usr/bin/python3
"""N queens solution finder module.
"""
import sys


def is_safe(board, row, col, N):
    """ Check if there is a queen in the same column"""
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True


def nqueens_util(board, row, N, solutions):
    """ queebs util"""
    if row == N:
        solutions.append(board[:])
        return

    for col in range(N):
        if is_safe(board, row, col, N):
            board[row] = col
            nqueens_util(board, row + 1, N, solutions)


def nqueens(N):
    """ queeens """
    try:
        N = int(N)
        if N < 4:
            raise ValueError
    except ValueError:
        print('N must be an integer greater or equal to 4')
        sys.exit(1)

    board = [-1] * N
    solutions = []
    nqueens_util(board, 0, N, solutions)

    return solutions


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: nqueens N')
        sys.exit(1)

    N = sys.argv[1]
    solutions = nqueens(N)

    for solution in solutions:
        print('[' + ', '
              .join(
                f'[{row}, {col}]' for row, col in enumerate(solution)) + ']')
