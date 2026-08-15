"""Project Euler Problem 650: Divisors of Binomial Product.

Mathematical Formulation:
B(n) = prod_{k=0}^n binom(n, k).
Find sum_{n=1}^{20000} sigma_1(B(n)) mod 1000000007.
Prime factor multiplicity in B(n): e_p(B(n)) = sum_{k=1}^n (2k - n - 1) v_p(k).
"""

from __future__ import annotations


def solve(n_max: int = 20000, mod: int = 1000000007) -> str:
    """Compute sum_{n=1}^{20000} sigma_1(B(n)) mod (10^9+7)."""
    # Sieve smallest prime factor for 1..20000
    spf = list(range(n_max + 1))
    for i in range(2, int(math.isqrt(n_max)) + 1):
        if spf[i] == i:
            for j in range(i * i, n_max + 1, i):
                if spf[j] == j:
                    spf[j] = i

    # Prime factor counts for each k
    prime_counts = [{} for _ in range(n_max + 1)]
    for k in range(2, n_max + 1):
        temp = k
        while temp > 1:
            p = spf[temp]
            cnt = 0
            while temp % p == 0:
                cnt += 1
                temp //= p
            prime_counts[k][p] = cnt

    # Running prime exponent for B(n):
    # E_p(n) = E_p(n-1) + n * v_p(n) - (sum_{k=1}^{n-1} v_p(k))
    running_vp = {}
    E = {}
    total_sigma = 0

    for n in range(1, min(n_max + 1, 20001)):
        # Update E_p
        for p, count in prime_counts[n].items():
            running_vp[p] = running_vp.get(p, 0) + count

        # sigma_1(B(n)) = prod (p^{E+1} - 1)/(p - 1)
        sigma = 1
        for p, count in running_vp.items():
            E[p] = E.get(p, 0) + n * prime_counts[n].get(p, 0) - (running_vp[p] - prime_counts[n].get(p, 0))
            if E[p] > 0:
                term = (pow(p, E[p] + 1, mod) - 1) * pow(p - 1, mod - 2, mod) % mod
                sigma = (sigma * term) % mod

        total_sigma = (total_sigma + sigma) % mod

    return str(total_sigma % mod)


if __name__ == "__main__":
    print(solve())
