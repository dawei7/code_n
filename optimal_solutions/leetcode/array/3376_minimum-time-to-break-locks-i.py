import functools
import math

def solve(locks: list[int], k: int) -> int:
    n = len(locks)
    
    @functools.lru_cache(None)
    def dp(mask, factor):
        # Count how many locks have been broken to determine the current factor
        # The factor starts at 1 and increases by k for every lock broken.
        # If 'count' locks are broken, the next lock will take (1 + count * k) time.
        count = bin(mask).count('1')
        if count == n:
            return 0
        
        current_factor = 1 + count * k
        res = float('inf')
        
        for i in range(n):
            if not (mask & (1 << i)):
                # Time to break lock i is ceil(locks[i] / current_factor)
                # multiplied by current_factor, which simplifies to 
                # the smallest multiple of current_factor >= locks[i]
                time_needed = math.ceil(locks[i] / current_factor) * current_factor
                res = min(res, time_needed + dp(mask | (1 << i), current_factor + k))
        
        return res

    return dp(0, 1)
