from collections import Counter
import math

def solve(nums: list[int]) -> int:
    counts = Counter(nums)
    total_operations = 0
    
    for count in counts.values():
        if count == 1:
            return -1
        # For any count > 1:
        # If count % 3 == 0: operations = count // 3
        # If count % 3 == 1: operations = (count // 3) - 1 + 2 = (count // 3) + 1
        # If count % 3 == 2: operations = (count // 3) + 1
        # All these cases are covered by math.ceil(count / 3)
        total_operations += math.ceil(count / 3)
        
    return total_operations
