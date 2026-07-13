"""Dual heaps with lazy deletion for LeetCode 480."""

from collections import Counter
from heapq import heappop, heappush


def solve(nums: list[int], k: int) -> list[float]:
    small: list[int] = []
    large: list[int] = []
    delayed = Counter()
    small_size = 0
    large_size = 0

    def prune(heap: list[int], lower: bool) -> None:
        while heap:
            value = -heap[0] if lower else heap[0]
            if delayed[value] == 0:
                break
            heappop(heap)
            delayed[value] -= 1

    def balance() -> None:
        nonlocal small_size, large_size
        if small_size > large_size + 1:
            heappush(large, -heappop(small))
            small_size -= 1
            large_size += 1
            prune(small, True)
        elif small_size < large_size:
            heappush(small, -heappop(large))
            small_size += 1
            large_size -= 1
            prune(large, False)

    def insert(value: int) -> None:
        nonlocal small_size, large_size
        if not small or value <= -small[0]:
            heappush(small, -value)
            small_size += 1
        else:
            heappush(large, value)
            large_size += 1
        balance()

    def erase(value: int) -> None:
        nonlocal small_size, large_size
        delayed[value] += 1
        if value <= -small[0]:
            small_size -= 1
            if value == -small[0]:
                prune(small, True)
        else:
            large_size -= 1
            if large and value == large[0]:
                prune(large, False)
        balance()

    def median() -> float:
        if k % 2:
            return float(-small[0])
        return (-small[0] + large[0]) / 2.0

    for value in nums[:k]:
        insert(value)
    medians = [median()]
    for index in range(k, len(nums)):
        insert(nums[index])
        erase(nums[index - k])
        medians.append(median())
    return medians
