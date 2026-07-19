from typing import List

def solve(nums: List[int]) -> int:
    """
    Calculates the number of partitions where the difference between 
    the left sum and right sum is even.
    """
    total_sum = sum(nums)
    left_sum = 0
    count = 0
    
    # We iterate up to len(nums) - 1 because the right partition 
    # must be non-empty.
    for i in range(len(nums) - 1):
        left_sum += nums[i]
        right_sum = total_sum - left_sum
        
        if (left_sum - right_sum) % 2 == 0:
            count += 1
            
    return count
