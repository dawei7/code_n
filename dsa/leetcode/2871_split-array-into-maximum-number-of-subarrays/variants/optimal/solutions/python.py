from typing import List

def solve(nums: List[int]) -> int:
    # First, calculate the total bitwise AND of the entire array.
    # This represents the minimum possible AND sum for any partition.
    total_and = nums[0]
    for x in nums[1:]:
        total_and &= x
    
    # If the total AND is greater than 0, we cannot split the array into 
    # multiple subarrays that each result in this same total_and.
    # Therefore, the maximum number of subarrays is 1.
    if total_and > 0:
        return 1
    
    # If the total AND is 0, we can greedily count how many subarrays
    # have an AND sum of 0.
    count = 0
    current_and = -1  # Initialize with all bits set
    
    for x in nums:
        if current_and == -1:
            current_and = x
        else:
            current_and &= x
            
        if current_and == 0:
            count += 1
            current_and = -1
            
    return count
