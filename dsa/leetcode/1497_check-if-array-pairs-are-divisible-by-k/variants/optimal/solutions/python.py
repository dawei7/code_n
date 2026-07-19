"""Optimal app-local solution for LeetCode 1497."""

from collections import Counter


def solve(arr: list[int], k: int) -> bool:
    """Return whether all values can form pairs summing to multiples of k."""
    counts = Counter(value % k for value in arr)

    for remainder, count in counts.items():
        complement = (-remainder) % k
        if remainder == complement:
            if count % 2 != 0:
                return False
        elif count != counts[complement]:
            return False

    return True
