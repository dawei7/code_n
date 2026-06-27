from typing import List

def solve(nums: List[int], k: int) -> int:
    """
    Calculates the sum of all 'good' numbers in the array.
    A number is good if it is strictly greater than its neighbors at index i-k and i+k.
    """
    total_sum = 0
    n = len(nums)
    
    for i in range(n):
        is_good = True
        
        # Check left neighbor
        if i - k >= 0:
            if nums[i] <= nums[i - k]:
                is_good = False
        
        # Check right neighbor
        if i + k < n:
            if nums[i] <= nums[i + k]:
                is_good = False
        
        # If it passed both checks, add to sum
        if is_good:
            total_sum += nums[i]
            
    return total_sum
