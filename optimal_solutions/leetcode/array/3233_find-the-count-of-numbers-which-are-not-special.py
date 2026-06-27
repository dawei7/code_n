import math

def solve(l: int, r: int) -> int:
    """
    Calculates the count of non-special numbers in [l, r].
    A special number is the square of a prime.
    """
    limit = int(math.isqrt(r))
    
    # Sieve of Eratosthenes to find primes up to sqrt(r)
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for p in range(2, int(math.isqrt(limit)) + 1):
        if is_prime[p]:
            for i in range(p * p, limit + 1, p):
                is_prime[i] = False
    
    # Count special numbers (p^2) that fall within [l, r]
    special_count = 0
    for p in range(2, limit + 1):
        if is_prime[p]:
            square = p * p
            if l <= square <= r:
                special_count += 1
                
    total_numbers = r - l + 1
    return total_numbers - special_count
