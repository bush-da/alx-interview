#!/usr/bin/python3
from collections import deque

def canUnlockAll(boxes):
    """Determine if all boxes can be unlocked."""
    n = len(boxes)  # Get the total number of boxes
    visited = [False] * n  # Track visited boxes, initialized to False
    visited[0] = True  # The first box is unlocked
    queue = deque([0])  # Initialize BFS with the first box

    while queue:
        current_box = queue.popleft()  # Get the current box to process
        # Check each key in the current box
        for key in boxes[current_box]:
            # If the key corresponds to a valid box that hasn't been visited
            if key < n and not visited[key]:
                visited[key] = True  # Mark the box as visited
                queue.append(key)  # Add the box to the queue for further exploration

    return all(visited)  # Return True if all boxes are visited
