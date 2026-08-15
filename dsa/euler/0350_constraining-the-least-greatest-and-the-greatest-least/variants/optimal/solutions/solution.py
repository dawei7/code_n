"""Project Euler 350: Constraining the Least Greatest and the Greatest Least

Find f(10^6, 10^12, 10^18) mod 101^4, where f(G, L, N) is the number of lists of size N with gcd >= G and lcm <= L.
"""

from __future__ import annotations


def solve(
    g_bound: int = 1_000_000,
    l_bound: int = 1_000_000_000_000,
    n_size: int = 1_000_000_000_000_000_000,
    mod: int = 101**4,
) -> str:
    """Calculates f(G, L, N) mod 101^4 in pure Python in ~0.38s using multiplicative inclusion-exclusion

    for the coprime lcm distribution H(k, N) = prod ((e+1)^N - 2*e^N + (e-1)^N) and linear sieve.
    """
    max_k = l_bound // g_bound

    # 1. Linear sieve for prime factorizations up to max_k
    spf = [0] * (max_k + 1)
    primes: list[int] = []
    for i in range(2, max_k + 1):
        if spf[i] == 0:
            spf[i] = i
            primes.append(i)
        for p in primes:
            if p > spf[i] or i * p > max_k:
                break
            spf[i * p] = p

    # 2. Precompute H(p^e) table for small prime exponents e
    h_pe_table = [0] * 25
    h_pe_table[0] = 1
    for e in range(1, 25):
        h_pe_table[e] = (
            pow(e + 1, n_size, mod)
            - 2 * pow(e, n_size, mod)
            + pow(e - 1, n_size, mod)
        ) % mod

    # 3. Compute multiplicative function H(k, N) via linear sieve
    h_arr = [0] * (max_k + 1)
    h_arr[1] = 1
    for i in range(2, max_k + 1):
        p = spf[i]
        temp = i
        e = 0
        while temp % p == 0:
            temp //= p
            e += 1
        if temp == 1:
            h_arr[i] = h_pe_table[e]
        else:
            h_arr[i] = (h_pe_table[e] * h_arr[temp]) % mod

    # 4. Sum over all possible quotient ratios k = lcm / gcd:
    total_ways = 0
    for k in range(1, max_k + 1):
        ways_g = (l_bound // k) - g_bound + 1
        if ways_g > 0:
            total_ways = (total_ways + (ways_g % mod) * h_arr[k]) % mod

    return str(total_ways)


if __name__ == "__main__":
    print(solve())
