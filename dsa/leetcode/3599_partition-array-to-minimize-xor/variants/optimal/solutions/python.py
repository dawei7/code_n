"""Optimal app-local solution for LeetCode 3599."""


def solve(nums, k):
    n = len(nums)
    prefix = [0] * (n + 1)
    for i, value in enumerate(nums):
        prefix[i + 1] = prefix[i] ^ value

    infinity = 1 << 60
    previous = [infinity] * (n + 1)
    previous[0] = 0

    for parts in range(1, k + 1):
        current = [infinity] * (n + 1)
        for end in range(parts, n + 1):
            best = infinity
            for start in range(parts - 1, end):
                candidate = max(
                    previous[start],
                    prefix[end] ^ prefix[start],
                )
                if candidate < best:
                    best = candidate
            current[end] = best
        previous = current

    return previous[n]
