"""Optimal app-local solution for LeetCode 1298."""

from collections import deque


def solve(status, candies, keys, containedBoxes, initialBoxes):
    n = len(status)
    owned = [False] * n
    openable = [value == 1 for value in status]
    opened = [False] * n
    queue = deque()

    for box in initialBoxes:
        owned[box] = True
        if openable[box]:
            queue.append(box)

    total = 0
    while queue:
        box = queue.popleft()
        if opened[box] or not owned[box] or not openable[box]:
            continue

        opened[box] = True
        total += candies[box]

        for key in keys[box]:
            openable[key] = True
            if owned[key] and not opened[key]:
                queue.append(key)

        for child in containedBoxes[box]:
            owned[child] = True
            if openable[child] and not opened[child]:
                queue.append(child)

    return total
