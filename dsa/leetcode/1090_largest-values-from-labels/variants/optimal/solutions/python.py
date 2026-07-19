"""Optimal solution for LeetCode 1090: Largest Values From Labels."""


def solve(values: list[int], labels: list[int], num_wanted: int, use_limit: int) -> int:
    label_usage: dict[int, int] = {}
    total = 0
    selected = 0

    for value, label in sorted(zip(values, labels), reverse=True):
        if selected == num_wanted:
            break
        if label_usage.get(label, 0) == use_limit:
            continue
        label_usage[label] = label_usage.get(label, 0) + 1
        total += value
        selected += 1

    return total
