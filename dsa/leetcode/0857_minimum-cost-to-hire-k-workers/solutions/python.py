"""Optimal app-local solution for LeetCode 857."""

import heapq


def solve(quality, wage, k):
    workers = sorted(
        (minimum_wage / worker_quality, worker_quality)
        for worker_quality, minimum_wage in zip(quality, wage)
    )

    largest_qualities = []
    quality_sum = 0
    best_cost = float("inf")

    for ratio, worker_quality in workers:
        heapq.heappush(largest_qualities, -worker_quality)
        quality_sum += worker_quality

        if len(largest_qualities) > k:
            quality_sum += heapq.heappop(largest_qualities)

        if len(largest_qualities) == k:
            best_cost = min(best_cost, quality_sum * ratio)

    return best_cost
