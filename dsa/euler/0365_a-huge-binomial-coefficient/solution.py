"""Project Euler Problem 365: A Huge Binomial Coefficient.

Calculate sum M(10^18, 10^9, p * q * r) for 1000 < p < q < r < 5000 and p, q, r prime.
"""


def solve(
    n: int = 10**18,
    k: int = 10**9,
    min_prime: int = 1000,
    max_prime: int = 5000,
) -> int:
    """Compute the sum of M(n, k, p * q * r) over prime triplets via Lucas' Theorem and CRT."""
    if n <= 0 or k <= 0:
        return 0

    # Linear prime sieve up to max_prime
    is_p = [True] * (max_prime + 1)
    is_p[0] = is_p[1] = False
    for i in range(2, int(max_prime**0.5) + 1):
        if is_p[i]:
            for j in range(i * i, max_prime + 1, i):
                is_p[j] = False

    primes = [p for p in range(min_prime + 1, max_prime) if is_p[p]]
    num_primes = len(primes)

    # Compute c_p = C(n, k) mod p for each prime via Lucas' Theorem
    def lucas(n_val: int, k_val: int, p: int) -> int:
        fact = [1] * p
        inv = [1] * p
        for i in range(1, p):
            fact[i] = (fact[i - 1] * i) % p
        inv[p - 1] = p - 1
        for i in range(p - 2, -1, -1):
            inv[i] = (inv[i + 1] * (i + 1)) % p

        def n_cr(nv: int, kv: int) -> int:
            if kv < 0 or kv > nv:
                return 0
            return (fact[nv] * inv[kv] % p) * inv[nv - kv] % p

        ans = 1
        while n_val > 0 or k_val > 0:
            ans = (ans * n_cr(n_val % p, k_val % p)) % p
            n_val //= p
            k_val //= p
        return ans

    c_vals = [lucas(n, k, p) for p in primes]

    # Precompute modular inverses inv_mod[i][j] = primes[i]^-1 mod primes[j]
    inv_mod = [[0] * num_primes for _ in range(num_primes)]
    for i in range(num_primes):
        pi = primes[i]
        for j in range(num_primes):
            if i != j:
                inv_mod[i][j] = pow(pi, primes[j] - 2, primes[j])

    # 3-moduli CRT accumulation
    total_sum = 0
    for i in range(num_primes):
        pi = primes[i]
        ci = c_vals[i]
        inv_i = inv_mod[i]
        for j in range(i + 1, num_primes):
            pj = primes[j]
            cj = c_vals[j]
            x_ij = ci + pi * ((cj - ci) * inv_i[j] % pj)
            m_ij = pi * pj
            inv_j = inv_mod[j]

            for k_idx in range(j + 1, num_primes):
                pr = primes[k_idx]
                rem = (c_vals[k_idx] - x_ij) % pr
                inv_k = (inv_i[k_idx] * inv_j[k_idx]) % pr
                diff = (rem * inv_k) % pr
                total_sum += x_ij + m_ij * diff

    return total_sum


if __name__ == "__main__":
    print(solve())
