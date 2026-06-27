from typing import List

def solve(nums: List[int], k: int) -> int:
    """
    To make every subarray of length k equal, we must have nums[i] == nums[i + k].
    This partitions the array into k independent groups based on index % k.
    For each group, we need to make all elements equal to some value 'x'.
    The value 'x' that minimizes the sum of absolute differences is the median.
    """
    n = len(nums)
    groups = [[] for _ in range(k)]
    
    for i in range(n):
        groups[i % k].append(nums[i])
        
    total_operations = 0
    
    for group in groups:
        if not group:
            continue
        
        # Sort the group to find the median
        group.sort()
        
        # The median minimizes the sum of absolute differences
        median = group[len(group) // 2]
        
        # Calculate cost to make all elements in this group equal to the median
        for val in group:
            total_operations += abs(val - median)
            
    return total_operations
