from typing import List

def solve(nums: List[int]) -> bool:
    """
    Determines if there are two subarrays of length 2 with the same sum.
    """
    seen_sums = set()
    
    # Iterate through the array to calculate sums of adjacent pairs
    for i in range(len(nums) - 1):
        current_sum = nums[i] + nums[i + 1]
        
        # If the sum has been seen before, we found a duplicate
        if current_sum in seen_sums:
            return True
        
        # Otherwise, add the sum to our set
        seen_sums.add(current_sum)
        
    return False
