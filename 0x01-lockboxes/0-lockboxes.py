#!/usr/bin/python3
"""Function that check if all boxes can be opened"""


def canUnlockAll(boxes):
    # Initialize a list to keep track of which boxes can be opened
    opened = [False] * len(boxes)
    opened[0] = True  # The first box is already unlocked

    # Initialize a stack (or queue) for DFS/BFS and add the first box
    stack = [0]

    # Iterate until there are no more boxes to explore
    while stack:
        box_index = stack.pop()  # Get the next box to explore
        for key in boxes[box_index]:  # Check the keys in the current box
            if key < len(boxes) and not opened[key]:
                opened[key] = True  # Mark the box as opened
                stack.append(key)  # Add the newly opened box to the stack

    # Check if all boxes are opened
    return all(opened)
