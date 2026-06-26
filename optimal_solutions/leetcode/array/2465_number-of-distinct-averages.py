from typing import List

def solve(nums: List[int]) -> int:
    """
    Calculates the number of distinct averages by repeatedly pairing 
    the minimum and maximum elements of the array.
    """
    nums.sort()
    distinct_averages = set()
    
    left = 0
    right = len(nums) - 1
    
    while left < right:
        avg = (nums[left] + nums[right]) / 2
        distinct_averages.add(avg)
        left += 1
        right -= 1
        
    return len(distinct_averages)
