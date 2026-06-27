from typing import List

def solve(nums: List[int], x: int, queries: List[int]) -> List[int]:
    # Precompute the indices where nums[i] == x
    occurrence_indices = [i for i, val in enumerate(nums) if val == x]
    
    results = []
    # Total number of occurrences found
    total_occurrences = len(occurrence_indices)
    
    for k in queries:
        # Check if the k-th occurrence exists (k is 1-indexed)
        if k <= total_occurrences:
            # Access the index (k-1 because list is 0-indexed)
            results.append(occurrence_indices[k - 1])
        else:
            results.append(-1)
            
    return results
