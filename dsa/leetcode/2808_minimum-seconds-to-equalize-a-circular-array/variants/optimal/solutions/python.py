from collections import defaultdict
import math

def solve(nums: list[int]) -> int:
    n = len(nums)
    indices = defaultdict(list)
    
    for i, val in enumerate(nums):
        indices[val].append(i)
        
    min_seconds = n
    
    for val in indices:
        pos = indices[val]
        # Calculate gaps between consecutive occurrences
        max_gap = 0
        for i in range(len(pos) - 1):
            max_gap = max(max_gap, pos[i+1] - pos[i] - 1)
        
        # Account for circular gap (last element to first element)
        circular_gap = (n - 1 - pos[-1]) + pos[0]
        max_gap = max(max_gap, circular_gap)
        
        # The time to fill a gap of size 'g' is ceil(g / 2)
        # which is equivalent to (g + 1) // 2
        seconds_needed = (max_gap + 1) // 2
        min_seconds = min(min_seconds, seconds_needed)
        
    return min_seconds
