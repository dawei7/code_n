"""Project Euler Problem 615: The Millionth Number with at Least One Million Prime Factors.

Find the 10^6-th number having at least 10^6 prime factors, modulo 123454321.
"""

import math
from typing import List, Tuple

_MOD = 123454321


def _sieve_primes(limit: int) -> List[int]:
    is_p = bytearray(b"\x01") * (limit + 1)
    is_p[0:2] = b"\x00\x00"
    for i in range(2, int(limit**0.5) + 1):
        if is_p[i]:
            is_p[i * i : limit + 1 : i] = b"\x00" * (
                ((limit - i * i) // i) + 1
            )
    return [p for p in range(3, limit + 1) if is_p[p]]


def solve(k_factors: int = 1_000_000, m_th: int = 1_000_000) -> int:
    """Find the m_th smallest number with at least k_factors prime factors modulo 123454321."""
    t_max = 17.0
    limit_p = int(2 ** (t_max + 1)) + 10
    primes = _sieve_primes(limit_p)
    log_primes = [math.log2(p / 2.0) for p in primes]

    all_u: List[Tuple[float, int, int]] = []

    def dfs(
        p_idx: int, current_cost: float, current_u_mod: int, current_omega: int
    ) -> None:
        all_u.append((current_cost, current_u_mod, current_omega))
        for i in range(p_idx, len(primes)):
            c = log_primes[i]
            if current_cost + c > t_max:
                break
            p = primes[i]
            pw = 1
            cost_pw = c
            p_pw = p
            while current_cost + cost_pw <= t_max:
                dfs(
                    i + 1,
                    current_cost + cost_pw,
                    (current_u_mod * p_pw) % _MOD,
                    current_omega + pw,
                )
                pw += 1
                cost_pw = pw * c
                p_pw = (p_pw * p) % _MOD

    dfs(0, 0.0, 1, 0)

    items: List[Tuple[float, int, int, int]] = []
    for c, u_mod, omega in all_u:
        j = 0
        while c + j <= t_max:
            items.append((c + j, j, u_mod, omega))
            j += 1

    items.sort(key=lambda x: x[0])

    _, j_val, u_mod_val, omega_val = items[m_th - 1]
    exponent = k_factors - omega_val + j_val
    ans = (pow(2, exponent, _MOD) * u_mod_val) % _MOD
    return ans


if __name__ == "__main__":
    print(solve())
