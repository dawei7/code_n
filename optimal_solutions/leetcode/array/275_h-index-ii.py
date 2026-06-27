from typing import List

def solve(citations: List[int]) -> int:
    """
    Calculates the H-index using binary search.
    The input is sorted in non-decreasing order.
    """
    n = len(citations)
    left, right = 0, n - 1
    
    while left <= right:
        mid = (left + right) // 2
        # The number of papers with at least citations[mid] citations is (n - mid)
        if citations[mid] >= n - mid:
            # This is a potential H-index, try to find a larger one to the left
            right = mid - 1
        else:
            # Need more citations, move to the right
            left = mid + 1
            
    # The H-index is the number of papers remaining from the 'left' index
    return n - left
