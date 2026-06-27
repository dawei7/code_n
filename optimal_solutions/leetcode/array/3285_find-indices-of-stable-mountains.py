from typing import List

def solve(height: List[int], threshold: int) -> List[int]:
    """
    Finds indices i such that height[i-1] > threshold.
    The range of i is from 1 to len(height) - 1.
    """
    stable_indices = []
    
    # We start from index 1 because the condition depends on height[i-1]
    for i in range(1, len(height)):
        if height[i - 1] > threshold:
            stable_indices.append(i)
            
    return stable_indices
