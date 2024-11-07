#!/usr/bin/env python3
"""N-Queens puzzle solution using backtracking."""

import sys

def print_usage_and_exit(message):
    """Prints an error message and exits the program."""
    print(message)
    sys.exit(1)

def is_safe(queens, row, col):
    """Checks if placing a queen at (row, col) is safe."""
    for r, c in enumerate(queens):
        # Check same column and diagonals
        if c == col or abs(c - col) == abs(r - row):
            return False
    return True

def solve_nqueens(n, row, queens, solutions):
    """Backtracks to find all solutions to the N-Queens problem."""
    if row == n:
        # Convert solution to format: [[row, col], [row, col], ...]
        solutions.append([[i, queens[i]] for i in range(n)])
        return

    for col in range(n):
        if is_safe(queens, row, col):
            queens[row] = col
            solve_nqueens(n, row + 1, queens, solutions)
            queens[row] = -1  # Reset position

def main():
    # Check for proper usage
    if len(sys.argv) != 2:
        print_usage_and_exit("Usage: nqueens N")
    
    # Check if N is an integer
    try:
        n = int(sys.argv[1])
    except ValueError:
        print_usage_and_exit("N must be a number")
    
    # Ensure N is at least 4
    if n < 4:
        print_usage_and_exit("N must be at least 4")

    # Initialize variables and find solutions
    solutions = []
    queens = [-1] * n  # -1 indicates no queen is placed in that row
    solve_nqueens(n, 0, queens, solutions)

    # Print each solution
    for solution in solutions:
        print(solution)

if __name__ == "__main__":
    main()
