from typing import List

def solve(nums: List[int]) -> int:
    n = len(nums)
    max_diff = 0
    
    # Iterate through the array to compare adjacent elements
    for i in range(n):
        # Use modulo operator to handle the circular adjacency (last element to first)
        diff = abs(nums[i] - nums[(i + 1) % n])
        if diff > max_diff:
            max_diff = diff
            
    return max_diff
