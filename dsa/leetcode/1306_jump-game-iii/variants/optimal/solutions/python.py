"""Optimal app-local solution for LeetCode 1306."""

from collections import deque


def solve(arr, start):
    queue = deque([start])
    seen = bytearray(len(arr))
    seen[start] = 1

    while queue:
        index = queue.popleft()
        if arr[index] == 0:
            return True

        jump = arr[index]
        for destination in (index - jump, index + jump):
            if 0 <= destination < len(arr) and not seen[destination]:
                seen[destination] = 1
                queue.append(destination)

    return False
