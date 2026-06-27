from typing import List

def solve(nums: List[int], target: int) -> int:
    n = len(nums)
    # dp[i] stores the max jumps to reach index i.
    # Initialize with -1 to represent unreachable states.
    dp = [-1] * n
    dp[0] = 0
    
    for i in range(1, n):
        for j in range(i):
            # Check if index j is reachable and if the jump condition is met
            if dp[j] != -1 and abs(nums[i] - nums[j]) <= target:
                dp[i] = max(dp[i], dp[j] + 1)
                
    return dp[n - 1]
