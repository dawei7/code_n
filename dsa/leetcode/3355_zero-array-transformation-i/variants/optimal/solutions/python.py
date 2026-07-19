from typing import List

def solve(nums: List[int], queries: List[List[int]]) -> bool:
    n = len(nums)
    diff = [0] * (n + 1)
    
    # Populate the difference array
    for l, r in queries:
        diff[l] += 1
        diff[r + 1] -= 1
        
    # Compute prefix sums on the fly and validate coverage
    curr_coverage = 0
    for i in range(n):
        curr_coverage += diff[i]
        if curr_coverage < nums[i]:
            return False
            
    return True
