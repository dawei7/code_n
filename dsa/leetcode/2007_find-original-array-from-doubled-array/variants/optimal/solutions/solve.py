from collections import Counter


def solve(changed: list[int]) -> list[int]:
    if len(changed) % 2:
        return []

    remaining = Counter(changed)
    original: list[int] = []

    for value in sorted(changed):
        if remaining[value] == 0:
            continue
        if remaining[2 * value] == 0:
            return []

        original.append(value)
        remaining[value] -= 1
        remaining[2 * value] -= 1

    return original
