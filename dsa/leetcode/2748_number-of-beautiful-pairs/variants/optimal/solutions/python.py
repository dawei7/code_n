from typing import List
import math

def solve(nums: List[int]) -> int:
    # count[d] stores the frequency of digit 'd' appearing as the first digit of numbers processed so far
    count = [0] * 10
    beautiful_pairs = 0
    
    for num in nums:
        last_digit = num % 10
        
        # Check coprime with all previously seen first digits
        for first_digit in range(1, 10):
            if count[first_digit] > 0 and math.gcd(first_digit, last_digit) == 1:
                beautiful_pairs += count[first_digit]
        
        # Find the first digit of the current number
        first_digit = int(str(num)[0])
        count[first_digit] += 1
        
    return beautiful_pairs
