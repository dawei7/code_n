from typing import List

def solve(nums: List[int]) -> bool:
    """
    Determines if there exists an increasing triplet subsequence in O(n) time
    and O(1) space using a greedy strategy.
    """
    first = float('inf')
    second = float('inf')
    
    for n in nums:
        if n <= first:
            # Update the smallest element found so far
            first = n
        elif n <= second:
            # Update the second smallest element found so far
            # This n is greater than first, but smaller than or equal to second
            second = n
        else:
            # If we reach here, we found a number greater than both first and second
            # which implies an increasing triplet (first < second < n)
            return True
            
    return False
