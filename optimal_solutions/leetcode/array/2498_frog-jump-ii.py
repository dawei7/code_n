from typing import List

def solve(stones: List[int]) -> int:
    """
    To minimize the maximum jump, we should distribute the stones such that 
    the frog jumps over one stone whenever possible. 
    
    For any three consecutive stones i, i+1, i+2, the frog must jump 
    at least stones[i+2] - stones[i] to ensure the round trip is covered 
    efficiently. The only exception is the start and end of the array.
    """
    n = len(stones)
    
    # If there are only two stones, the only jump is the distance between them.
    if n == 2:
        return stones[1] - stones[0]
    
    # The maximum jump will be at least the distance between stones[i+2] and stones[i]
    # because one path will take stones[i] -> stones[i+2] and the other will 
    # visit stones[i+1].
    max_jump = 0
    
    # Check gaps of size 2 (skipping one stone)
    for i in range(n - 2):
        max_jump = max(max_jump, stones[i + 2] - stones[i])
        
    # Also consider the jump between the first two and last two stones
    # (though these are covered by the loop logic, it's good to be explicit)
    max_jump = max(max_jump, stones[1] - stones[0])
    max_jump = max(max_jump, stones[n - 1] - stones[n - 2])
    
    return max_jump
