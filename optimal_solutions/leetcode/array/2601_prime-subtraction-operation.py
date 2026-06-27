import bisect

def solve(nums: list[int]) -> bool:
    max_val = max(nums)
    
    # Sieve of Eratosthenes to find all primes up to max_val
    primes = []
    is_prime = [True] * (max_val + 1)
    is_prime[0] = is_prime[1] = False
    for p in range(2, max_val + 1):
        if is_prime[p]:
            primes.append(p)
            for i in range(p * p, max_val + 1, p):
                is_prime[i] = False
                
    prev = 0
    for num in nums:
        # We need to find a prime p such that:
        # num - p > prev  =>  p < num - prev
        target = num - prev
        
        # Find the largest prime strictly less than target
        idx = bisect.bisect_left(primes, target)
        
        # If idx > 0, we can subtract primes[idx-1]
        if idx > 0:
            current_val = num - primes[idx - 1]
        else:
            current_val = num
            
        # If the current value is not strictly greater than the previous, return False
        if current_val <= prev:
            return False
        
        prev = current_val
        
    return True
