from typing import List

def solve(nums: List[int]) -> float:
    """
    Calculates the minimum average of the smallest and largest elements
    by sorting the array and using two pointers.
    """
    nums.sort()
    n = len(nums)
    min_avg = float('inf')
    
    left = 0
    right = n - 1
    
    while left < right:
        current_avg = (nums[left] + nums[right]) / 2
        if current_avg < min_avg:
            min_avg = current_avg
        left += 1
        right -= 1
        
    return float(min_avg)
