#!/usr/bin/env python3
"""implementation for island question"""


def island_perimeter(grid):
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:  # Found a land cell
                # Add 4 for the initial perimeter of the land cell
                perimeter += 4

                # Check for a neighbor above
                if r > 0 and grid[r-1][c] == 1:
                    perimeter -= 2

                # Check for a neighbor to the left
                if c > 0 and grid[r][c-1] == 1:
                    perimeter -= 2

    return perimeter
