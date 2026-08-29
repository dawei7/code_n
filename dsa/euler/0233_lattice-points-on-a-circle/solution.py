def solve(limit: int = 10**11) -> int:
    """Find sum of all positive integers N <= limit such that f(N) = 420.

    Problem Context & Mathematical Principles:
    -------------------------------------------
    1. Circle Equation & Lattice Points:
       The circle passing through (0, 0), (N, 0), (0, N), (N, N) has equation:
           (2x - N)^2 + (2y - N)^2 = 2N^2.
       The number of integer lattice points f(N) equals the number of representations
       of 2N^2 as the sum of two squares:
           f(N) = r_2(2N^2) = 4 * (d_1(2N^2) - d_3(2N^2)).

    2. Multiplicative Divisor Formula:
       If N = 2^(a_0) * prod p_i^(a_i) * prod q_j^(b_j) where p_i = 1 (mod 4) and q_j = 3 (mod 4):
           f(N) = 4 * prod (2 * a_i + 1).
       Setting f(N) = 420 yields:
           prod (2 * a_i + 1) = 105 = 3 * 5 * 7.

    3. Feasible Core Factorizations:
       The only factorizations of 105 into odd factors > 1 yielding cores <= 10^11 are:
       - Pattern 1: p1^10 * p2^2  (factors 21 * 5)
       - Pattern 2: p1^7 * p2^3   (factors 15 * 7)
       - Pattern 3: p1^3 * p2^2 * p3^1 (factors 7 * 5 * 3)
       where p1, p2, p3 are distinct primes = 1 (mod 4).

    4. Multiplier Summation:
       For each valid core <= limit, all N = core * m are valid where m has NO prime
       factors = 1 (mod 4). We precompute prefix sums of such m up to max_m <= 280,000.

    Complexity:
    -----------
    - Time Complexity: O(M_max + pi(5*10^6)) operations (< 0.8s for limit = 10^11).
    - Space Complexity: O(M_max + pi(5*10^6)) memory (~15 MB).
    """
    LIMIT = limit

    # Sieve primes up to 5,000,000 (since max p3 <= 10^11 / (5^3 * 13^2) ~ 4.73 * 10^6)
    def sieve_primes(n: int) -> list[int]:
        is_p = bytearray([1]) * (n + 1)
        is_p[0] = is_p[1] = 0
        for i in range(2, int(n**0.5) + 1):
            if is_p[i]:
                is_p[i * i :: i] = b"\x00" * len(is_p[i * i :: i])
        return [i for i in range(2, n + 1) if is_p[i]]

    primes = sieve_primes(5000000)
    p1 = [p for p in primes if p % 4 == 1]

    # Precompute prefix sums of multiplier m having no prime factor = 1 (mod 4)
    MAX_M = LIMIT // (5**3 * 13**2 * 17) + 5
    has_p1 = [False] * (MAX_M + 1)
    for p in p1:
        if p > MAX_M:
            break
        for j in range(p, MAX_M + 1, p):
            has_p1[j] = True

    prefix_sum_M = [0] * (MAX_M + 1)
    curr = 0
    for m in range(1, MAX_M + 1):
        if not has_p1[m]:
            curr += m
        prefix_sum_M[m] = curr

    ans_total = 0

    # 1. Pattern 1: p1^10 * p2^2
    for i in range(len(p1)):
        c1 = p1[i] ** 10
        if c1 > LIMIT:
            break
        for j in range(len(p1)):
            if i == j:
                continue
            core = c1 * (p1[j] ** 2)
            if core > LIMIT:
                break
            max_m = LIMIT // core
            ans_total += core * prefix_sum_M[max_m]

    # 2. Pattern 2: p1^7 * p2^3
    for i in range(len(p1)):
        c1 = p1[i] ** 7
        if c1 > LIMIT:
            break
        for j in range(len(p1)):
            if i == j:
                continue
            core = c1 * (p1[j] ** 3)
            if core > LIMIT:
                break
            max_m = LIMIT // core
            ans_total += core * prefix_sum_M[max_m]

    # 3. Pattern 3: p1^3 * p2^2 * p3^1
    for i in range(len(p1)):
        c1 = p1[i] ** 3
        if c1 > LIMIT:
            break
        for j in range(len(p1)):
            if i == j:
                continue
            c2 = c1 * (p1[j] ** 2)
            if c2 > LIMIT:
                break
            for k in range(len(p1)):
                if k == i or k == j:
                    continue
                core = c2 * p1[k]
                if core > LIMIT:
                    break
                max_m = LIMIT // core
                ans_total += core * prefix_sum_M[max_m]

    return ans_total


if __name__ == "__main__":
    print(solve())
