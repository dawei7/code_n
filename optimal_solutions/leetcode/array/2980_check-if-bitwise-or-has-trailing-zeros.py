from typing import List

def solve(nums: List[int]) -> bool:
    """
    Checks if there are at least two even numbers in the array.
    If two numbers are even, their bitwise OR will have a 0 in the 
    least significant bit position, resulting in a trailing zero.
    """
    even_count = 0
    for num in nums:
        if num % 2 == 0:
            even_count += 1
        
        if even_count >= 2:
            return True
            
    return False
