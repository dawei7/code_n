"""Project Euler 312: Cyclic Paths on Sierpinski Graphs

Find C(C(C(10000))) mod 13^8, where C(n) is the number of Hamiltonian cycles on the Sierpinski graph S_n.
"""

from __future__ import annotations


def phi(m: int) -> int:
    """Computes Euler's totient function phi(m)."""
    res = m
    p = 2
    temp = m
    while p * p <= temp:
        if temp % p == 0:
            while temp % p == 0:
                temp //= p
            res -= res // p
        p += 1
    if temp > 1:
        res -= res // temp
    return res


def solve(n_start: int = 10_000, prime_base: int = 13, exp: int = 8) -> str:
    """Calculates C(C(C(n_start))) mod prime_base^exp using the closed-form formula

    C(n) = 8 * 12^((3^(n-2) - 3) / 2) and a 3-tier Euler totient tower reduction.
    """
    m0 = prime_base**exp  # 13^8

    # Define the 3-tier totient modular chain
    m1 = 2 * phi(m0)
    p1 = phi(m1)
    m2 = 2 * phi(p1)
    p2 = phi(m2)
    m3 = 2 * phi(p2)

    tier_moduli = [(m3, p2), (m2, p1), (m1, m0)]
    cur_val = n_start

    for m_mod, p_mod in tier_moduli:
        phi_m = phi(m_mod)
        pow3 = pow(3, (cur_val - 2) % phi_m + phi_m * 10, m_mod)
        e = ((pow3 - 3) % m_mod) // 2
        phi_p = phi(p_mod)
        cur_val = (8 * pow(12, (e % phi_p) + phi_p * 10, p_mod)) % p_mod

    return str(cur_val)


if __name__ == "__main__":
    print(solve())
