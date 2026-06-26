from typing import List

def solve(nums: List[int]) -> int:
    """
    Calculates the number of distinct prime factors of the product of all elements in nums.
    """
    distinct_primes = set()
    
    for n in nums:
        d = 2
        temp = n
        # Trial division up to sqrt(temp)
        while d * d <= temp:
            if temp % d == 0:
                distinct_primes.add(d)
                while temp % d == 0:
                    temp //= d
            d += 1
        # If temp > 1, the remaining value is a prime factor
        if temp > 1:
            distinct_primes.add(temp)
            
    return len(distinct_primes)
