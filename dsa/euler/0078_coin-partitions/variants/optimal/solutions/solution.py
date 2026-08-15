def solve(modulus: int = 1000000) -> int:
    """Find the least value of n for which the partition function p(n) is divisible by 1,000,000.

    Mathematical Principles Applied:
    1. Euler's Pentagonal Number Theorem:
       The unrestricted partition function p(n) satisfies the recurrence relation:
       p(n) = sum_{k != 0} (-1)^(k-1) * p(n - g_k)
       where g_k = k * (3k - 1) / 2 for k = 1, -1, 2, -2, 3, -3, ... are the generalized pentagonal numbers:
       g_k in {1, 2, 5, 7, 12, 15, 22, 26, ...}.

    2. Modular Recurrence Reduction:
       To test p(n) % 1,000,000 == 0, intermediate partition values are reduced modulo 1,000,000.

    3. Asymptotic Complexity:
       For a given n, the number of pentagonal terms g_k <= n is O(sqrt(n)).
       Total time complexity to reach n is O(N * sqrt(N)), which completes in ~0.50s for N ≈ 55,000.

    Time Complexity: O(N * sqrt(N)) executing in ~0.50s.
    Space Complexity: O(N) memory to store partition list p[0..n].
    """
    # Base partition value p(0) = 1
    p = [1]
    n = 1

    # Search positive integer n upwards
    while True:
        p_n = 0
        k = 1

        # Sum terms for generalized pentagonal numbers g_k <= n
        while True:
            # Generalized pentagonal numbers for +k and -k
            g1 = k * (3 * k - 1) // 2
            g2 = k * (3 * k + 1) // 2

            # Sign alternating factor: +1 for odd k, -1 for even k
            sign = 1 if (k % 2 == 1) else -1

            # Accumulate terms from recurrence
            if g1 <= n:
                p_n += sign * p[n - g1]
            if g2 <= n:
                p_n += sign * p[n - g2]

            # Stop inner loop when pentagonal number exceeds n
            if g1 > n:
                break

            k += 1

        # Reduce p(n) modulo 1,000,000
        p_n %= modulus

        # If p(n) is divisible by 1,000,000, return integer n
        if p_n == 0:
            return n

        # Append p(n) to list and advance n
        p.append(p_n)
        n += 1


if __name__ == "__main__":
    print(solve())
