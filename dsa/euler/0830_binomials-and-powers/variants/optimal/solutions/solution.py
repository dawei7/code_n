import math


def solve(n: int = 10**18) -> int:
    """Find S(n) = sum_{k=0}^{n} binom(n, k) k^n modulo 83^3 * 89^3 * 97^3.

    Mahler p-adic Stirling expansion and Chinese Remainder Theorem modulo prime cubes.
    Truncates exactly at 3p - 1.

    Time Complexity: O(sum(p) * max_p)
    Space Complexity: O(max_p)
    """
    primes = [83, 89, 97]
    mods = [p**3 for p in primes]
    M = mods[0] * mods[1] * mods[2]

    # Precompute binom(n, j) for j up to 300 (covers 3 * max_p)
    limit = 300
    binom = [1] * (limit + 1)
    for j in range(1, limit + 1):
        binom[j] = (binom[j - 1] * (n - j + 1)) // j

    ans_p = []
    for p, mod in zip(primes, mods):
        phi = p**2 * (p - 1)
        a_j = []
        for j in range(limit + 1):
            res = 0
            for i in range(j + 1):
                if i % p == 0:
                    term = 0 if n >= 3 else math.comb(j, i) * pow(i, n, mod)
                else:
                    term = math.comb(j, i) * pow(i, n % phi, mod)
                
                if (j - i) % 2 == 1:
                    res -= term
                else:
                    res += term
            res %= mod
            a_j.append(res)

        sum_p = 0
        for j in range(limit + 1):
            if j > n:
                break
            term = (binom[j] % mod) * a_j[j] * pow(2, n - j, mod)
            sum_p = (sum_p + term) % mod
        ans_p.append(sum_p)

    # Chinese Remainder Theorem
    ans = 0
    for i in range(3):
        m_i = M // mods[i]
        y_i = pow(m_i, -1, mods[i])
        ans = (ans + ans_p[i] * m_i * y_i) % M

    return ans


if __name__ == "__main__":
    print(solve())
