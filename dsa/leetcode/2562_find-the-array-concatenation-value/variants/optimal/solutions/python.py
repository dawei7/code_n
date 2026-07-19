from typing import List

def solve(nums: List[int]) -> int:
    """
    Calculates the concatenation value of an array using two pointers.
    """
    total_sum = 0
    left = 0
    right = len(nums) - 1
    
    while left <= right:
        if left == right:
            # If there is only one element left, add it directly
            total_sum += nums[left]
        else:
            # Concatenate the first and last elements as strings
            concat_str = str(nums[left]) + str(nums[right])
            total_sum += int(concat_str)
        
        left += 1
        right -= 1
        
    return total_sum
