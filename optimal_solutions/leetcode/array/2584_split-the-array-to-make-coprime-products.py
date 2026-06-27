import math
from collections import defaultdict

def solve(nums: list[int]) -> int:
    n = len(nums)
    if n == 1:
        return -1
    
    # Map each prime factor to its first and last occurrence index
    first_occurrence = {}
    last_occurrence = {}
    
    def get_prime_factors(num):
        factors = set()
        d = 2
        temp = num
        while d * d <= temp:
            if temp % d == 0:
                factors.add(d)
                while temp % d == 0:
                    temp //= d
            d += 1
        if temp > 1:
            factors.add(temp)
        return factors

    # Precompute prime factors for each number
    all_factors = []
    for i, x in enumerate(nums):
        factors = get_prime_factors(x)
        all_factors.append(factors)
        for p in factors:
            if p not in first_occurrence:
                first_occurrence[p] = i
            last_occurrence[p] = i
            
    # We need to find a split point i such that for all prime factors p
    # present in nums[0...i], their last occurrence is <= i.
    # This ensures no prime factor in the left part exists in the right part.
    
    max_last_idx = -1
    for i in range(n - 1):
        # Update the furthest index any prime factor in the current prefix reaches
        for p in all_factors[i]:
            max_last_idx = max(max_last_idx, last_occurrence[p])
        
        # If the furthest index any prime factor in the prefix reaches is <= i,
        # then no prime factor from the prefix exists in the suffix.
        if max_last_idx <= i:
            return i
            
    return -1
