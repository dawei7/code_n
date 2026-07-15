"""Optimal solution for LeetCode 1086: High Five."""

from collections import defaultdict
from heapq import heappush, heappushpop


def solve(items: list[list[int]]) -> list[list[int]]:
    best: dict[int, list[int]] = defaultdict(list)
    for student_id, score in items:
        scores = best[student_id]
        if len(scores) < 5:
            heappush(scores, score)
        elif score > scores[0]:
            heappushpop(scores, score)

    return [
        [student_id, sum(best[student_id]) // 5]
        for student_id in sorted(best)
    ]
