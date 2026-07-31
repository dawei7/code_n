from heapq import heapify, heappop, heappush


def solve(sticks: list[int]) -> int:
    heapify(sticks)
    total = 0
    while len(sticks) > 1:
        combined = heappop(sticks) + heappop(sticks)
        total += combined
        heappush(sticks, combined)
    return total
