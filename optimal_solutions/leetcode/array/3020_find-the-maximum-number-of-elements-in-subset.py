from collections import Counter
import math

def solve(nums: list[int]) -> int:
    counts = Counter(nums)
    max_subset_size = 1
    
    # Handle the special case for 1
    if 1 in counts:
        ones = counts[1]
        if ones % 2 == 0:
            max_subset_size = max(max_subset_size, ones - 1)
        else:
            max_subset_size = max(max_subset_size, ones)
            
    # Handle numbers > 1
    # We only need to iterate through unique keys
    unique_nums = sorted(counts.keys())
    
    for x in unique_nums:
        if x == 1:
            continue
        
        curr = x
        count = 0
        # Build the chain x, x^2, x^4, ...
        while curr in counts and counts[curr] >= 2:
            count += 2
            curr = curr * curr
            
        # After the loop, we check if the last element exists
        if curr in counts:
            count += 1
            
        # The subset size must be odd. 
        # If we have a chain of length 'count' (which is always odd),
        # we take it. If 'count' is even, we take 'count - 1'.
        if count % 2 == 0:
            count -= 1
            
        max_subset_size = max(max_subset_size, count)
        
    return max_subset_size
