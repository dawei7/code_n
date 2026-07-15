"""Optimal app-local solution for LeetCode 950."""

from collections import deque


def solve(deck):
    positions = deque(range(len(deck)))
    answer = [0] * len(deck)
    for value in sorted(deck):
        answer[positions.popleft()] = value
        if positions:
            positions.append(positions.popleft())
    return answer
