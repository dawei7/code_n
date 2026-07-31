from collections import Counter
from typing import List


def solve(nums: List[int], l: int, r: int) -> int:
    modulus = 1_000_000_007
    counts = Counter(nums)
    zero_count = counts.pop(0, 0)

    dp = [0] * (r + 1)
    dp[0] = zero_count + 1

    for value, multiplicity in counts.items():
        next_dp = dp.copy()
        window_width = (multiplicity + 1) * value

        for total in range(value, r + 1):
            next_dp[total] = (next_dp[total] + next_dp[total - value]) % modulus
            if total >= window_width:
                next_dp[total] = (next_dp[total] - dp[total - window_width]) % modulus

        dp = next_dp

    return sum(dp[l : r + 1]) % modulus
