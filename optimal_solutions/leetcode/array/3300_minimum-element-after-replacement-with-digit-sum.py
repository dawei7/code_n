from typing import List

def get_digit_sum(n: int) -> int:
    """Helper function to calculate the sum of digits of an integer."""
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

def solve(nums: List[int]) -> int:
    """
    Transforms each element in nums to its digit sum and returns the minimum.
    """
    min_val = float('inf')
    
    for num in nums:
        digit_sum = get_digit_sum(num)
        if digit_sum < min_val:
            min_val = digit_sum
            
    return int(min_val)
