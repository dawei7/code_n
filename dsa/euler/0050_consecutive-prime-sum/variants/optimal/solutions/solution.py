def solve(limit: int = 1000000) -> int:
    """Find prime below limit that can be written as the sum of the most consecutive primes.
    
    Time Complexity: O(P)
    Space Complexity: O(limit)
    """
    is_prime = [True] * limit
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, limit, i):
                is_prime[j] = False

    primes = [i for i in range(limit) if is_prime[i]]
    prime_set = set(primes)

    # Prefix sums of primes
    prefix = [0] * (len(primes) + 1)
    for i in range(len(primes)):
        prefix[i + 1] = prefix[i] + primes[i]

    # Find max consecutive length L
    max_len = 0
    while max_len < len(primes) and prefix[max_len] < limit:
        max_len += 1

    # Search window length L from max_len down to 1
    for L in range(max_len, 0, -1):
        for i in range(len(primes) - L + 1):
            s = prefix[i + L] - prefix[i]
            if s >= limit:
                break
            if s in prime_set:
                return s

    return -1
