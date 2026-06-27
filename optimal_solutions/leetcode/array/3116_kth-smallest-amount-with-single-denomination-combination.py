import math
from typing import List

def solve(coins: List[int], k: int) -> int:
    """
    Finds the k-th smallest multiple using binary search and inclusion-exclusion.
    """
    n = len(coins)
    
    # Precompute LCMs for all subsets to speed up inclusion-exclusion
    # Since N is small (up to 15), we can use bitmasking or recursion.
    def get_lcm(a, b):
        return abs(a * b) // math.gcd(a, b)

    def count_multiples(mid: int) -> int:
        count = 0
        # Inclusion-Exclusion Principle
        # Iterate through all non-empty subsets of coins
        for i in range(1, 1 << n):
            lcm_val = 1
            bits = 0
            for j in range(n):
                if (i >> j) & 1:
                    lcm_val = get_lcm(lcm_val, coins[j])
                    bits += 1
                    if lcm_val > mid:
                        break
            
            if bits % 2 == 1:
                count += mid // lcm_val
            else:
                count -= mid // lcm_val
        return count

    # Binary search range
    low = min(coins)
    high = min(coins) * k
    ans = high
    
    while low <= high:
        mid = (low + high) // 2
        if count_multiples(mid) >= k:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
            
    return ans
