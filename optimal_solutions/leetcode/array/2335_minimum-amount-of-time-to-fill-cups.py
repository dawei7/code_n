import math

def solve(amount: list[int]) -> int:
    # Sort the amount array to easily identify the smallest, middle, and largest counts.
    # Since there are only 3 elements, sorting is O(1).
    amount.sort()
    
    a, b, c = amount[0], amount[1], amount[2]
    
    total_cups = a + b + c
    
    # The minimum time is the maximum of two possibilities:
    # 1. The count of the most numerous cup type (c). This is the bottleneck if c is very large.
    #    If c > a + b, then we will spend a + b seconds pairing c with a and b,
    #    and then c - (a + b) seconds filling the remaining c cups one by one.
    #    Total time = (a + b) + (c - (a + b)) = c.
    # 2. Half the total number of cups, rounded up (ceil(total_cups / 2)).
    #    This represents the time if we can always fill two cups per second,
    #    or if the counts are balanced enough that no single type is a bottleneck.
    #    We use (total_cups + 1) // 2 for integer ceiling division.
    
    return max(c, (total_cups + 1) // 2)
