from typing import List

def solve(hours: List[int]) -> int:
    """
    Counts the number of pairs (i, j) such that i < j and (hours[i] + hours[j]) % 24 == 0.
    Uses a frequency array to track remainders encountered so far.
    """
    remainder_counts = [0] * 24
    total_pairs = 0
    
    for h in hours:
        remainder = h % 24
        # If current remainder is r, we need a previous remainder of (24 - r) % 24
        target = (24 - remainder) % 24
        
        total_pairs += remainder_counts[target]
        remainder_counts[remainder] += 1
        
    return total_pairs
