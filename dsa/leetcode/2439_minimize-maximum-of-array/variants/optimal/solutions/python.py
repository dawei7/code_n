import math

def solve(nums: list[int]) -> int:
    """
    Calculates the minimum possible maximum value of the array after 
    performing the allowed operations.
    """
    max_val = 0
    prefix_sum = 0
    
    for i, val in enumerate(nums):
        prefix_sum += val
        # The average of the prefix [0...i] is the minimum possible 
        # maximum value for this segment. We take the ceiling of the average.
        current_avg = math.ceil(prefix_sum / (i + 1))
        if current_avg > max_val:
            max_val = current_avg
            
    return max_val
