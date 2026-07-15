"""Optimal app-local solution for LeetCode 1399: Count Largest Group."""


def solve(n: int) -> int:
    group_sizes: dict[int, int] = {}
    for value in range(1, n + 1):
        remaining = value
        digit_sum = 0
        while remaining:
            remaining, digit = divmod(remaining, 10)
            digit_sum += digit
        group_sizes[digit_sum] = group_sizes.get(digit_sum, 0) + 1

    largest = max(group_sizes.values())
    return sum(size == largest for size in group_sizes.values())
