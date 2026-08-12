def solve(modulus: int = 1000000) -> int:
    """Find least n for which partition function p(n) is divisible by modulus using Pentagonal Number Theorem.
    
    Time Complexity: O(N * sqrt(N))
    Space Complexity: O(N)
    """
    p = [1]
    n = 1

    while True:
        p_n = 0
        k = 1
        while True:
            # Generalized pentagonal numbers g_k = k(3k - 1) // 2
            g1 = k * (3 * k - 1) // 2
            g2 = k * (3 * k + 1) // 2

            sign = 1 if (k % 2 == 1) else -1

            if g1 <= n:
                p_n += sign * p[n - g1]
            if g2 <= n:
                p_n += sign * p[n - g2]

            if g1 > n:
                break
            k += 1

        p_n %= modulus
        if p_n == 0:
            return n

        p.append(p_n)
        n += 1
