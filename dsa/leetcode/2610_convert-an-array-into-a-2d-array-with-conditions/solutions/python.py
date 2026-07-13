from collections import Counter
from typing import List

def solve(nums: List[int]) -> List[List[int]]:
    """
    Constructs a 2D array from nums such that each row contains unique elements.
    The number of rows is determined by the maximum frequency of any element.
    """
    counts = Counter(nums)
    result = []
    
    # The maximum frequency of any element dictates the number of rows needed.
    # We iterate through the frequency map and place each instance of a number
    # into a unique row index.
    for num, freq in counts.items():
        for i in range(freq):
            # If the current row index doesn't exist in the result yet, create it.
            if i >= len(result):
                result.append([])
            result[i].append(num)
            
    return result
