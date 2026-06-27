from collections import deque

def solve(nums: list[int], limit: int) -> list[int]:
    n = len(nums)
    # Store pairs of (value, original_index) and sort them
    sorted_nums = sorted([(nums[i], i) for i in range(n)])
    
    # Groups will store lists of indices that can be swapped with each other
    groups = []
    if n > 0:
        current_group = [sorted_nums[0]]
        for i in range(1, n):
            if sorted_nums[i][0] - sorted_nums[i-1][0] <= limit:
                current_group.append(sorted_nums[i])
            else:
                groups.append(current_group)
                current_group = [sorted_nums[i]]
        groups.append(current_group)
    
    result = [0] * n
    
    # For each group, the values can be placed in any of the indices belonging to that group.
    # To get the lexicographically smallest result, we place the smallest values 
    # in the smallest indices.
    for group in groups:
        indices = sorted([item[1] for item in group])
        values = sorted([item[0] for item in group])
        
        for i in range(len(indices)):
            result[indices[i]] = values[i]
            
    return result
