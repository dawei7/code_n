"""App-local reference solution for LeetCode 2829."""


def solve(n: int, k: int) -> int:
    """Return the minimum sum of a k-avoiding array of length n."""
    small_count = min(n, k // 2)
    remaining = n - small_count

    small_sum = small_count * (small_count + 1) // 2
    large_sum = remaining * (2 * k + remaining - 1) // 2
    return small_sum + large_sum
