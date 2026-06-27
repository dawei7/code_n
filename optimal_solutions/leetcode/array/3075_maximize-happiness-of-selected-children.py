from typing import List

def solve(happiness: List[int], k: int) -> int:
    """
    Calculates the maximum happiness by selecting k children greedily.
    """
    # Sort happiness in descending order to pick the largest values first
    happiness.sort(reverse=True)
    
    total_happiness = 0
    for i in range(k):
        # The actual happiness is the initial value minus the number of children already picked
        # We use max(0, ...) because happiness cannot be negative
        current_val = happiness[i] - i
        if current_val > 0:
            total_happiness += current_val
        else:
            # Since the array is sorted, if current_val <= 0, 
            # all subsequent values will also result in <= 0
            break
            
    return total_happiness
