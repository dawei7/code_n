from typing import List

def solve(hours: List[int]) -> int:
    """
    Counts the number of pairs (i, j) with i < j such that (hours[i] + hours[j]) % 24 == 0.
    Uses a frequency array to store remainders encountered so far.
    """
    remainder_counts = [0] * 24
    total_pairs = 0
    
    for h in hours:
        remainder = h % 24
        # The complement remainder needed to make the sum divisible by 24
        complement = (24 - remainder) % 24
        
        # Add the number of times we have seen the complement so far
        total_pairs += remainder_counts[complement]
        
        # Update the frequency of the current remainder
        remainder_counts[remainder] += 1
        
    return total_pairs
