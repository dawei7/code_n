def solve(limit: int = 1000000) -> int:
    """Find number of circular primes below limit using a prime sieve.
    
    Time Complexity: O(N log log N)
    Space Complexity: O(N)
    """
    is_prime = [True] * limit
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, limit, i):
                is_prime[j] = False

    prime_set = {i for i in range(limit) if is_prime[i]}

    circular_count = 0
    for p in prime_set:
        s = str(p)
        if any(c in s for c in "024568") and p not in (2, 5):
            continue
        rotations = [int(s[i:] + s[:i]) for i in range(len(s))]
        if all(r in prime_set for r in rotations):
            circular_count += 1

    return circular_count
