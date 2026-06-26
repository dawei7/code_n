"""Optimal solution for LeetCode 1124: Longest Well-Performing Interval."""


def solve(hours: list[int]) -> int:
    score = 0
    first_seen: dict[int, int] = {}
    best = 0
    for i, hour in enumerate(hours):
        score += 1 if hour > 8 else -1
        if score > 0:
            best = i + 1
        else:
            first_seen.setdefault(score, i)
            if score - 1 in first_seen:
                best = max(best, i - first_seen[score - 1])
    return best
