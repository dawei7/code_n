from typing import List

def solve(original: List[int], bounds: List[List[int]]) -> int:
    # The difference between consecutive elements in the copy array
    # must match the difference in the original array.
    # Let diff[i] = original[i] - original[i-1].
    # Then copy[i] = copy[0] + sum(diff[1...i]).
    # Let S[i] = sum(diff[1...i]) with S[0] = 0.
    # Then copy[i] = copy[0] + S[i].
    # The constraint is: bounds[i][0] <= copy[0] + S[i] <= bounds[i][1]
    # Which rearranges to: bounds[i][0] - S[i] <= copy[0] <= bounds[i][1] - S[i]
    
    current_min = bounds[0][0]
    current_max = bounds[0][1]
    
    cumulative_diff = 0
    for i in range(1, len(original)):
        cumulative_diff += (original[i] - original[i-1])
        
        # Update the valid range for copy[0] based on the current index constraint
        # copy[0] must be >= bounds[i][0] - cumulative_diff
        # copy[0] must be <= bounds[i][1] - cumulative_diff
        current_min = max(current_min, bounds[i][0] - cumulative_diff)
        current_max = min(current_max, bounds[i][1] - cumulative_diff)
        
    if current_min > current_max:
        return 0
    
    return current_max - current_min + 1
