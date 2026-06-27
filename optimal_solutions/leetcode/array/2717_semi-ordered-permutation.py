from typing import List

def solve(nums: List[int]) -> int:
    n = len(nums)
    idx_1 = nums.index(1)
    idx_n = nums.index(n)
    
    ans = idx_1 + (n - 1 - idx_n)
    if idx_1 > idx_n:
        ans -= 1
        
    return ans
