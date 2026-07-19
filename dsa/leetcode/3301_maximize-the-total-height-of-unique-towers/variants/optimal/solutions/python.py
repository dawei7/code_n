from typing import List

def solve(maximumHeight: List[int]) -> int:
    # Sort in descending order to greedily pick the largest possible values first
    maximumHeight.sort(reverse=True)
    
    total_sum = 0
    # The first tower can take its maximum allowed height
    current_max = maximumHeight[0]
    total_sum += current_max
    
    # Iterate through the rest of the towers
    for i in range(1, len(maximumHeight)):
        # The current tower must be at most its limit, 
        # and strictly less than the previous tower's height
        current_max = min(maximumHeight[i], current_max - 1)
        
        # If the height becomes non-positive, we cannot assign unique heights
        if current_max <= 0:
            return -1
        
        total_sum += current_max
        
    return total_sum
