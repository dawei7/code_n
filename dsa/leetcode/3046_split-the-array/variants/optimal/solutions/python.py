from collections import Counter
from typing import List

def solve(nums: List[int]) -> bool:
    """
    Determines if the array can be split into two subsets of equal size
    where each subset contains only unique elements.
    """
    counts = Counter(nums)
    
    # If any number appears more than twice, it's impossible to split
    # because one subset would inevitably receive at least two of that number.
    for count in counts.values():
        if count > 2:
            return False
            
    return True
