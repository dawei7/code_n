from typing import List

def solve(coins: List[int], target: int) -> int:
    """
    Calculates the minimum number of coins to add to make all values 
    from 1 to target representable.
    """
    coins.sort()
    reachable = 0
    added_count = 0
    i = 0
    n = len(coins)
    
    while reachable < target:
        # If the next coin is within the reachable range + 1, 
        # we can extend the range to reachable + coins[i]
        if i < n and coins[i] <= reachable + 1:
            reachable += coins[i]
            i += 1
        else:
            # Otherwise, we must add a coin of value (reachable + 1)
            # to bridge the gap and extend the range to (2 * reachable + 1)
            reachable += (reachable + 1)
            added_count += 1
            
    return added_count
