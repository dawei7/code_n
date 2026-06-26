from typing import List

def solve(nums: List[int]) -> bool:
    n = len(nums)
    # dp[i] will be True if the prefix of length i is validly partitionable
    dp = [False] * (n + 1)
    dp[0] = True
    
    for i in range(2, n + 1):
        # Check for 2 equal elements
        if i >= 2:
            if nums[i-1] == nums[i-2]:
                if dp[i-2]:
                    dp[i] = True
        
        # Check for 3 equal elements or 3 consecutive increasing elements
        if i >= 3:
            # 3 equal elements
            if nums[i-1] == nums[i-2] == nums[i-3]:
                if dp[i-3]:
                    dp[i] = True
            # 3 consecutive increasing elements
            elif nums[i-1] == nums[i-2] + 1 == nums[i-3] + 2:
                if dp[i-3]:
                    dp[i] = True
                    
    return dp[n]
