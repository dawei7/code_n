from typing import List

def solve(nums: List[int], target: int) -> int:
    # dp[i] will store the maximum length of a subsequence that sums to i.
    # Initialize with -1 to indicate that the sum is currently unreachable.
    dp = [-1] * (target + 1)
    dp[0] = 0
    
    for num in nums:
        # Iterate backwards to ensure each element is used at most once (0/1 Knapsack)
        for current_sum in range(target, num - 1, -1):
            if dp[current_sum - num] != -1:
                dp[current_sum] = max(dp[current_sum], dp[current_sum - num] + 1)
                
    return dp[target]
