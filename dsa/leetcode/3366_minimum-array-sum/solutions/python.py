import math
from functools import lru_cache

def solve(nums: list[int], k: int, op1: int, op2: int) -> int:
    n = len(nums)
    
    @lru_cache(None)
    def dp(idx, r1, r2):
        if idx == n:
            return 0
        
        # Option 0: Do nothing to current element
        res = nums[idx] + dp(idx + 1, r1, r2)
        
        # Option 1: Divide by 2
        if r1 > 0:
            val = math.ceil(nums[idx] / 2)
            res = min(res, val + dp(idx + 1, r1 - 1, r2))
            
        # Option 2: Subtract k
        if r2 > 0 and nums[idx] >= k:
            res = min(res, (nums[idx] - k) + dp(idx + 1, r1, r2 - 1))
            
        # Option 3: Divide then subtract
        if r1 > 0 and r2 > 0:
            val = math.ceil(nums[idx] / 2)
            if val >= k:
                res = min(res, (val - k) + dp(idx + 1, r1 - 1, r2 - 1))
        
        # Option 4: Subtract then divide
        if r1 > 0 and r2 > 0 and nums[idx] >= k:
            val = math.ceil((nums[idx] - k) / 2)
            res = min(res, val + dp(idx + 1, r1 - 1, r2 - 1))
            
        return res

    return dp(0, op1, op2)
