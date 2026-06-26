from collections import Counter
from typing import List

def solve(nums: List[int]) -> int:
    # Filter only even numbers
    evens = [x for x in nums if x % 2 == 0]
    
    if not evens:
        return -1
    
    # Count frequencies
    counts = Counter(evens)
    
    # Find the element with max frequency, tie-break with smallest value
    # We sort by frequency descending, then by value ascending
    best_val = -1
    max_freq = -1
    
    for val, freq in counts.items():
        if freq > max_freq:
            max_freq = freq
            best_val = val
        elif freq == max_freq:
            if val < best_val:
                best_val = val
                
    return best_val
