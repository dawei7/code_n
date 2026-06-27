from typing import List

def solve(nums: List[int]) -> int:
    # Count total evens and odds
    count_even = 0
    count_odd = 0
    
    # Count alternating sequences
    # alt_even_start: length of sequence starting with even
    # alt_odd_start: length of sequence starting with odd
    alt_even_start = 0
    alt_odd_start = 0
    
    for x in nums:
        parity = x % 2
        if parity == 0:
            count_even += 1
            # If we need an even number to continue an alternating sequence
            if alt_odd_start % 2 == 0:
                alt_odd_start += 1
            # If we start a new alternating sequence with even
            if alt_even_start % 2 == 0:
                alt_even_start += 1
        else:
            count_odd += 1
            # If we need an odd number to continue an alternating sequence
            if alt_even_start % 2 == 1:
                alt_even_start += 1
            # If we start a new alternating sequence with odd
            if alt_odd_start % 2 == 1:
                alt_odd_start += 1
                
    return max(count_even, count_odd, alt_even_start, alt_odd_start)
