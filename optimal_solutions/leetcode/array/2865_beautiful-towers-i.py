from typing import List

def solve(maxHeights: List[int]) -> int:
    """
    Calculates the maximum sum of a beautiful tower configuration.
    Iterates through each index as a potential peak and computes the 
    resulting mountain sum.
    """
    n = len(maxHeights)
    max_total_sum = 0
    
    for i in range(n):
        current_sum = maxHeights[i]
        
        # Build to the left
        last_height = maxHeights[i]
        for j in range(i - 1, -1, -1):
            last_height = min(last_height, maxHeights[j])
            current_sum += last_height
            
        # Build to the right
        last_height = maxHeights[i]
        for j in range(i + 1, n):
            last_height = min(last_height, maxHeights[j])
            current_sum += last_height
            
        max_total_sum = max(max_total_sum, current_sum)
        
    return max_total_sum
