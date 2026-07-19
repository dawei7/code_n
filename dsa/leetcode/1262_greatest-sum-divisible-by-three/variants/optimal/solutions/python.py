from typing import List


def solve(nums: List[int]) -> int:
    dp = [0, float("-inf"), float("-inf")]
    for value in nums:
        current = dp[:]
        for residue in range(3):
            current[(residue + value) % 3] = max(current[(residue + value) % 3], dp[residue] + value)
        dp = current
    return dp[0]
