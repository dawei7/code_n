"""Optimal solution for LeetCode 358: Rearrange String k Distance Apart."""

from collections import Counter, deque
from heapq import heapify, heappop, heappush


def solve(s: str, k: int) -> str:
    if k <= 1:
        return s

    heap = [(-count, character) for character, count in Counter(s).items()]
    heapify(heap)
    cooldown: deque[tuple[int, int, str]] = deque()
    result: list[str] = []

    for index in range(len(s)):
        while cooldown and cooldown[0][0] <= index:
            _, count, character = cooldown.popleft()
            heappush(heap, (count, character))

        if not heap:
            return ""

        count, character = heappop(heap)
        result.append(character)
        count += 1
        if count < 0:
            cooldown.append((index + k, count, character))

    return "".join(result)

