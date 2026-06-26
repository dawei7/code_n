"""Optimal solution for LeetCode 1000: Minimum Cost to Merge Stones."""


def solve(stones: list[int], k: int) -> int:
    n = len(stones)
    if (n - 1) % (k - 1) != 0:
        return -1

    prefix = [0]
    for value in stones:
        prefix.append(prefix[-1] + value)

    dp = [[0] * n for _ in range(n)]
    for length in range(k, n + 1):
        for left in range(n - length + 1):
            right = left + length - 1
            best = min(
                dp[left][mid] + dp[mid + 1][right]
                for mid in range(left, right, k - 1)
            )
            if (length - 1) % (k - 1) == 0:
                best += prefix[right + 1] - prefix[left]
            dp[left][right] = best
    return dp[0][n - 1]
