def solve(limit: int = 10**6) -> int:
    """Find the number of grids for which S(m, n) = p^2 for primes p < 10^6.
    
    Time Complexity: O(pi(limit)) via Arithmetic Progression Interval Counting
    Space Complexity: O(limit)
    """

    def sieve_primes(n):
        is_p = bytearray([1]) * (n + 1)
        is_p[0] = is_p[1] = 0
        for i in range(2, int(n**0.5) + 1):
            if is_p[i]:
                is_p[i * i :: i] = b"\x00" * len(is_p[i * i :: i])
        return [i for i in range(2, n + 1) if is_p[i]]

    primes = sieve_primes(limit)
    total = 0

    for p in primes:
        p2 = p * p
        if (p2 + 11) % 8 == 0:
            total += 1

        max_m = (p2 + 13 - 1) // 8
        if max_m >= 1:
            rem = (p2 + 13) % 6
            m1 = 1
            while (2 * m1) % 6 != rem:
                m1 += 1
            if m1 <= max_m:
                cnt = (max_m - m1) // 3 + 1
                total += 2 * cnt

    return total
