"""Optimal app-local solution for LeetCode 1152."""

from collections import Counter, defaultdict
from itertools import combinations


def solve(
    username: list[str], timestamp: list[int], website: list[str]
) -> list[str]:
    histories: dict[str, list[str]] = defaultdict(list)
    for _, user, site in sorted(zip(timestamp, username, website)):
        histories[user].append(site)

    scores: Counter[tuple[str, str, str]] = Counter()
    for sites in histories.values():
        scores.update(set(combinations(sites, 3)))

    best = min(scores, key=lambda pattern: (-scores[pattern], pattern))
    return list(best)
