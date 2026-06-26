"""Optimal solution for LeetCode 1383: Maximum Performance of a Team."""

from heapq import heappop, heappush


def solve(n: int, speed: list[int], efficiency: list[int], k: int) -> int:
    engineers = sorted(zip(efficiency, speed), reverse=True)
    speed_heap: list[int] = []
    speed_sum = 0
    best = 0

    for eff, spd in engineers:
        heappush(speed_heap, spd)
        speed_sum += spd
        if len(speed_heap) > k:
            speed_sum -= heappop(speed_heap)
        best = max(best, speed_sum * eff)
    return best % 1_000_000_007
