"""Optimal solution for LeetCode 1066: Campus Bikes II."""

from functools import lru_cache


def solve(workers: list[list[int]], bikes: list[list[int]]) -> int:
    @lru_cache(maxsize=None)
    def minimum_cost(used_bikes: int) -> int:
        worker_index = used_bikes.bit_count()
        if worker_index == len(workers):
            return 0

        worker_x, worker_y = workers[worker_index]
        best = float("inf")
        for bike_index, (bike_x, bike_y) in enumerate(bikes):
            bike_bit = 1 << bike_index
            if used_bikes & bike_bit:
                continue
            distance = abs(worker_x - bike_x) + abs(worker_y - bike_y)
            best = min(best, distance + minimum_cost(used_bikes | bike_bit))
        return int(best)

    return minimum_cost(0)
