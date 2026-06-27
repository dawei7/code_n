from typing import List

def solve(nums: List[int]) -> int:
    """
    Finds the minimum partition value by sorting the array and 
    calculating the minimum difference between adjacent elements.
    """
    nums.sort()
    
    # Find the minimum difference between adjacent elements
    min_diff = float('inf')
    for i in range(1, len(nums)):
        diff = nums[i] - nums[i - 1]
        if diff < min_diff:
            min_diff = diff
            
    return min_diff
