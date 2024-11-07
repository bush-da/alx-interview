#!/usr/bin/env python3
"""N-Queens puzzle solution using backtracking."""

import sys

def print_usage_and_exit(msg):
    print(msg)
    sys.exit(1)

def is_safe(board, row, col, n):
    # Check column
    for i in range(row):
        if board[i] == col:
            return False
    # Check main diagonal
    for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
        if board[i] == j:
            return False
    # Check anti-diagonal
    for i, j in zip(range(row - 1, -1, -1), range(col + 1, n)):
        if board[i] == j:
            return False
    return True

def solve_nqueens(n):
    solutions = []
    board = [-1] * n

    def backtrack(row):
        if row == n:
            # Solution found
            solutions.append([[i, board[i]] for i in range(n)])
            return
        for col in range(n):
            if is_safe(board, row, col, n):
                board[row] = col
                backtrack(row + 1)
                board[row] = -1  # Reset position

    backtrack(0)
    return solutions

def main():
    if len(sys.argv) != 2:
        print_usage_and_exit("Usage: nqueens N")

    try:
        n = int(sys.argv[1])
    except ValueError:
        print_usage_and_exit("N must be a number")

    if n < 4:
        print_usage_and_exit("N must be at least 4")

    solutions = solve_nqueens(n)
    for solution in solutions:
        print(solution)

if __name__ == "__main__":
    main()
