#!/usr/bin/python3
""" pascal_trianlge function that will output based on number of rows input
    return based on list
"""

def pascal_triangle(n):
    """
    Returns a list of lists representing Pascal's triangle of size n.
    If n <= 0, returns an empty list.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])

        row.append(1)
        triangle.append(row)

    return triangle
