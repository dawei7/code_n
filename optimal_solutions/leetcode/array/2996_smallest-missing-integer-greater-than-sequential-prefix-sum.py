from typing import List

def solve(nums: List[int]) -> int:
    # Calculate the sum of the longest sequential prefix
    prefix_sum = nums[0]
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1] + 1:
            prefix_sum += nums[i]
        else:
            break
    
    # Use a set for O(1) average time complexity lookups
    num_set = set(nums)
    
    # Find the smallest integer >= prefix_sum not in the set
    current = prefix_sum
    while current in num_set:
        current += 1
        
    return current
