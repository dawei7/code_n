def solve(limit: int = 2000000) -> int:
    """Find the sum of all primes below limit using a bytearray Sieve of Eratosthenes.
    
    Time Complexity: O(N log log N)
    Space Complexity: O(N)
    """
    is_prime = bytearray([1]) * limit
    is_prime[0] = is_prime[1] = 0

    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            is_prime[i * i : limit : i] = bytearray([0]) * len(range(i * i, limit, i))

    return sum(i for i, prime in enumerate(is_prime) if prime)
