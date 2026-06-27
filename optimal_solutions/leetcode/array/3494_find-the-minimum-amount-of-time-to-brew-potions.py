from typing import List

def solve(brewTime: List[int], prevAction: List[int]) -> int:
    """
    Calculates the minimum time to brew all potions.
    Since each potion must be brewed one at a time, the total time
    is simply the sum of all individual brew times, regardless of 
    the dependency order, provided the dependencies form a valid 
    sequence (which is guaranteed by the problem constraints).
    """
    if not brewTime:
        return 0
    
    return sum(brewTime)
