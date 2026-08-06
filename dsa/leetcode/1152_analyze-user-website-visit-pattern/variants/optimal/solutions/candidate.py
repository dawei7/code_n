"""Proposed app-local solution for LeetCode 1152."""

from collections import Counter, defaultdict
from itertools import combinations


def solve(username: list[str], timestamp: list[int], website: list[str]) -> list[str]:
    histories: dict[str, list[tuple[int, str]]] = defaultdict(list)
    for user, time, site in zip(username, timestamp, website):
        histories[user].append((time, site))

    scores: Counter[tuple[str, str, str]] = Counter()
    for visits in histories.values():
        visits.sort()
        sites = [site for _, site in visits]
        timestamps_are_distinct = all(
            visits[position - 1][0] < visits[position][0]
            for position in range(1, len(visits))
        )
        if timestamps_are_distinct:
            patterns = set(combinations(sites, 3))
        else:
            patterns = {
                (first_site, second_site, third_site)
                for (first_time, first_site), (second_time, second_site), (third_time, third_site)
                in combinations(visits, 3)
                if first_time < second_time < third_time
            }
        scores.update(patterns)

    best = min(scores, key=lambda pattern: (-scores[pattern], pattern))
    return list(best)
