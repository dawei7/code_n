"""Iterative seeded-bracket construction for LeetCode 544."""


def solve(n: int) -> str:
    groups = [str(seed) for seed in range(1, n + 1)]

    while len(groups) > 1:
        count = len(groups)
        groups = [
            f"({groups[index]},{groups[count - 1 - index]})"
            for index in range(count // 2)
        ]

    return groups[0]

