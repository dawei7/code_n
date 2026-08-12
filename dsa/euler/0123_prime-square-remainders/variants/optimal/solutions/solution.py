def solve(target_rem: int = 10000000000) -> int:
    """Find least n for which remainder r = (p_n - 1)^n + (p_n + 1)^n mod p_n^2 exceeds target_rem.
    
    Time Complexity: O(N)
    Space Complexity: O(N)
    """
    limit = 1000000
    is_p = [True] * limit
    is_p[0] = is_p[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if is_p[i]:
            for j in range(i * i, limit, i):
                is_p[j] = False

    primes = [i for i in range(limit) if is_p[i]]

    # Only odd n yield non-trivial remainder 2 * n * p_n
    for n in range(1, len(primes) + 1, 2):
        p_n = primes[n - 1]
        r = 2 * n * p_n
        if r > target_rem:
            return n

    return -1
