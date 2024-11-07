#!/usr/bin/python3
"""N queens solution finder module.
"""
import sys

def get_input():
    """Retrieves and validates the program's argument.

    Returns:
        int: The size of the chessboard.
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    return n

def is_safe(queens, row, col):
    """Checks if placing a queen at (row, col) is safe.

    Args:
        queens (list): List where the index represents the row, and the value at each
                       index represents the column position of a queen.

    Returns:
        bool: True if no two queens attack each other.
    """
    for r, c in enumerate(queens):
        if c == col or abs(c - col) == abs(r - row):
            return False
    return True

def solve_nqueens(n):
    """Solves the N queens problem using backtracking and prints solutions.

    Args:
        n (int): The size of the chessboard.
    """
    def backtrack(row, queens):
        if row == n:
            solutions.append([[r, queens[r]] for r in range(n)])
            return
        for col in range(n):
            if is_safe(queens, row, col):
                queens[row] = col
                backtrack(row + 1, queens)
                queens[row] = -1  # Reset position

    solutions = []
    queens = [-1] * n  # Initialize queens' positions
    backtrack(0, queens)
    return solutions

if __name__ == "__main__":
    n = get_input()
    solutions = solve_nqueens(n)
    for solution in solutions:
        print(solution)
