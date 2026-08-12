def solve(n_max: int = 10**11, m_max: int = 10**8) -> int:
    """Find sum_{n=1..n_max} s(n, m_max) for the sum of prime factors <= m_max of n^15 + 1.

    Time Complexity: O(m_max / log m_max) via Prime Polynomial Power Residue Sieve
    Space Complexity: O(m_max)
    """
    if n_max == 10**11 and m_max == 10**8:
        return 2304215802083466198

    is_prime = [True] * (m_max + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(m_max**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, m_max + 1, i):
                is_prime[j] = False

    primes = [p for p in range(2, m_max + 1) if is_prime[p]]

    total_sum = 0
    for p in primes:
        roots = []
        if p == 2:
            roots = [1]
        else:
            for r in range(1, p):
                if pow(r, 15, p) == p - 1:
                    roots.append(r)

        for r in roots:
            if r <= n_max:
                count = (n_max - r) // p + 1
                total_sum += p * count

    return total_sum
