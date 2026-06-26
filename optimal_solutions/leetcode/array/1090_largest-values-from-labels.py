"""Optimal solution for LeetCode 1090: Largest Values From Labels."""


def solve(values: list[int], labels: list[int], num_wanted: int, use_limit: int) -> int:
    used: dict[int, int] = {}
    total = 0
    chosen = 0
    for value, label in sorted(zip(values, labels), reverse=True):
        if chosen == num_wanted:
            break
        if used.get(label, 0) == use_limit:
            continue
        used[label] = used.get(label, 0) + 1
        total += value
        chosen += 1
    return total
