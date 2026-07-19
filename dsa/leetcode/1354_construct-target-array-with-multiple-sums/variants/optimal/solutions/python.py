"""Optimal app-local solution for LeetCode 1354."""

from heapq import heapify, heappop, heappush


def solve(target):
    if len(target) == 1:
        return target[0] == 1

    total = sum(target)
    heap = [-value for value in target]
    heapify(heap)

    while True:
        largest = -heappop(heap)
        rest = total - largest
        if largest == 1 or rest == 1:
            return True
        if rest == 0 or rest >= largest:
            return False
        previous = largest % rest
        if previous == 0:
            return False
        total = rest + previous
        heappush(heap, -previous)
