"""Project Euler Problem 773: Ruff Numbers.

Find F(97) modulo 10^9+7, the sum of all k-Ruff numbers less than N_k that end in 7,
where S_k = {2, 5, p_1, ..., p_k} with p_i being the first k primes ending in 7.
"""

from typing import List

_MOD = 1_000_000_007


def _first_k_primes_ending_in_7(k: int) -> List[int]:
    if k <= 0:
        return []

    primes = [2]
    ending7: List[int] = []
    candidate = 3

    while len(ending7) < k:
        is_prime = True
        limit = int(candidate**0.5)
        for p in primes:
            if p > limit:
                break
            if candidate % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(candidate)
            if candidate % 10 == 7:
                ending7.append(candidate)
        candidate += 2

    return ending7


def solve(k: int = 97, mod: int = _MOD) -> int:
    """Compute F(k) mod 10^9+7 using Mobius inclusion-exclusion and cyclic mod 10 residue symmetry."""
    primes7 = _first_k_primes_ending_in_7(k)

    m_mod = 1
    phi_mod = 1
    for p in primes7:
        m_mod = (m_mod * p) % mod
        phi_mod = (phi_mod * (p - 1)) % mod

    q_table = (7, 1, 3, 9)
    a_sum = 0
    c = 1

    for s in range(0, k + 1):
        term = (c * q_table[s & 3]) % mod
        if s & 1:
            a_sum = (a_sum - term) % mod
        else:
            a_sum = (a_sum + term) % mod

        if s < k:
            c = (c * (k - s)) % mod
            c = (c * pow(s + 1, mod - 2, mod)) % mod

    return (m_mod * ((a_sum + 5 * phi_mod) % mod)) % mod


if __name__ == "__main__":
    print(solve())
