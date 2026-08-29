"""Project Euler Problem 764: Asymmetric Diophantine Equation.

Find S(10^16) modulo 10^9, where S(N) = sum(x+y+z) over all primitive solutions (x,y,z)
to 16x^2 + y^4 = z^2 with 1 <= x, y, z <= N and gcd(x, y, z) = 1.
"""

from math import isqrt
from typing import Dict, List, Tuple

_MOD_DEFAULT = 1_000_000_000


def _iroot4(n: int) -> int:
    if n <= 0:
        return 0
    return isqrt(isqrt(n))


def _ceil_root4(n: int) -> int:
    if n <= 0:
        return 0
    r = _iroot4(n)
    if r * r * r * r < n:
        r += 1
    return r


def _odd_count(n: int) -> int:
    if n <= 0:
        return 0
    return (n + 1) // 2


def _odd_sum1(n: int) -> int:
    if n <= 0:
        return 0
    m = (n + 1) // 2
    return m * m


def _odd_sum4(n: int) -> int:
    if n <= 0:
        return 0
    m = (n + 1) // 2
    s1 = m * (m + 1) // 2
    s2 = m * (m + 1) * (2 * m + 1) // 6
    s3 = s1 * s1
    s4 = m * (m + 1) * (2 * m + 1) * (3 * m * m + 3 * m - 1) // 30
    return 16 * s4 - 32 * s3 + 24 * s2 - 8 * s1 + m


def _sieve_spf(n: int) -> List[int]:
    spf = list(range(n + 1))
    limit = int(n**0.5)
    for i in range(2, limit + 1):
        if spf[i] == i:
            for j in range(i * i, n + 1, i):
                if spf[j] == j:
                    spf[j] = i
    return spf


def _squarefree_divs_mu(
    n: int, spf: List[int], cache: Dict[int, List[Tuple[int, int, int, int]]]
) -> List[Tuple[int, int, int, int]]:
    if n in cache:
        return cache[n]
    if n <= 1:
        cache[n] = [(1, 1, 1, 1)]
        return cache[n]

    primes: List[int] = []
    tmp = n
    while tmp > 1:
        p = spf[tmp]
        primes.append(p)
        while tmp % p == 0:
            tmp //= p

    divs: List[Tuple[int, int]] = [(1, 1)]
    for p in primes:
        divs += [(d * p, -mu) for (d, mu) in divs]

    out: List[Tuple[int, int, int, int]] = []
    for d, mu in divs:
        out.append((d, mu, d, d * d * d * d))

    cache[n] = out
    return out


def _coprime_odd_prefix(
    base: int,
    L: int,
    divs: List[Tuple[int, int, int, int]],
    mod_s1: int,
    mod_s4: int,
) -> Tuple[int, int, int]:
    if L <= 0:
        return 0, 0, 0

    cnt = 0
    s1 = 0
    s4 = 0

    for d, mu, d1, d4 in divs:
        m = L // d
        if m <= 0:
            continue

        cnt += mu * _odd_count(m)

        if mod_s1:
            s1 = (s1 + mu * (d1 % mod_s1) * (_odd_sum1(m) % mod_s1)) % mod_s1

        if mod_s4:
            s4 = (s4 + mu * (d4 % mod_s4) * (_odd_sum4(m) % mod_s4)) % mod_s4

    return int(cnt), s1 % mod_s1, s4 % mod_s4


def _coprime_odd_range(
    base: int,
    lo: int,
    hi: int,
    divs: List[Tuple[int, int, int, int]],
    mod_s1: int,
    mod_s4: int,
) -> Tuple[int, int, int]:
    if hi < lo or hi <= 0:
        return 0, 0, 0
    if lo <= 1:
        return _coprime_odd_prefix(base, hi, divs, mod_s1, mod_s4)

    c1, s1_1, s4_1 = _coprime_odd_prefix(base, hi, divs, mod_s1, mod_s4)
    c0, s1_0, s4_0 = _coprime_odd_prefix(base, lo - 1, divs, mod_s1, mod_s4)

    cnt = c1 - c0
    s1 = (s1_1 - s1_0) % mod_s1
    s4 = (s4_1 - s4_0) % mod_s4
    return cnt, s1, s4


def solve(N: int = 10_000_000_000_000_000, mod: int = _MOD_DEFAULT) -> int:
    """Compute S(N) modulo mod using primitive 2-adic Pythagorean parameterization."""
    mod8 = 8 * mod
    mod2 = 2 * mod

    max_base = _iroot4(2 * N) + 2
    spf = _sieve_spf(max_base)
    div_cache: Dict[int, List[Tuple[int, int, int, int]]] = {}

    pow4 = [0] * (max_base + 1)
    for i in range(max_base + 1):
        pow4[i] = i * i * i * i

    total = 0

    # Family A: z - 4x = p^4, z + 4x = q^4 with odd coprime p < q
    q_max = _iroot4(2 * N - 1)
    for q in range(1, q_max + 1, 2):
        q4 = pow4[q]
        rem = 2 * N - q4
        if rem <= 0:
            break

        p_max = _iroot4(rem)
        p_max = min(p_max, q - 1)
        p_max = min(p_max, N // q)

        if q4 <= 8:
            continue
        p_max = min(p_max, _iroot4(q4 - 8))
        if p_max <= 0:
            continue

        p_min = 1
        low = q4 - 8 * N
        if low > 1:
            p_min = _ceil_root4(low)
        if p_min % 2 == 0:
            p_min += 1

        if p_min > p_max:
            continue

        divs = _squarefree_divs_mu(q, spf, div_cache)
        cnt, s1, s4_mod8 = _coprime_odd_range(q, p_min, p_max, divs, mod, mod8)
        if cnt <= 0:
            continue

        numx_mod8 = ((cnt % mod8) * (q4 % mod8) - s4_mod8) % mod8
        sum_x = (numx_mod8 // 8) % mod

        numz_mod2 = ((s4_mod8 % mod2) + (cnt % mod2) * (q4 % mod2)) % mod2
        sum_z = (numz_mod2 // 2) % mod

        sum_y = (q % mod) * (s1 % mod) % mod
        total = (total + sum_x + sum_y + sum_z) % mod

    # Family B: min(v2(z-4x), v2(z+4x)) = 3
    k = 1
    while (1 << (4 * k)) <= N:
        scale4k = 1 << (4 * k)
        scale4k_2 = 1 << (4 * k - 2)
        y_scale = 1 << (k + 1)

        # Case B_high: z-4x = 8*p^4, z+4x = 2^(4k+1)*q^4
        if N > 4:
            q_max2 = _iroot4((N - 4) // scale4k)
            for q in range(1, q_max2 + 1, 2):
                q4 = pow4[q]
                remN = N - scale4k * q4
                if remN < 4:
                    continue

                p_max_z = _iroot4(remN // 4)
                bound_pos = scale4k_2 * q4 - 1
                if bound_pos <= 0:
                    continue
                p_max_pos = _iroot4(bound_pos)
                p_max = min(p_max_z, p_max_pos, N // (y_scale * q))
                if p_max <= 0:
                    continue

                low = scale4k_2 * q4 - N
                p_min = 1
                if low > 1:
                    p_min = _ceil_root4(low)
                if p_min % 2 == 0:
                    p_min += 1

                if p_min > p_max:
                    continue

                divs = _squarefree_divs_mu(q, spf, div_cache)
                cnt, s1, s4 = _coprime_odd_range(q, p_min, p_max, divs, mod, mod)
                if cnt <= 0:
                    continue

                term_p4 = (3 * s4) % mod
                term_q4 = (5 * (scale4k_2 % mod) * (q4 % mod) * (cnt % mod)) % mod
                term_pq = ((y_scale % mod) * (q % mod) * (s1 % mod)) % mod
                total = (total + term_p4 + term_q4 + term_pq) % mod

        # Case B_low: z-4x = 2^(4k+1)*p^4, z+4x = 8*q^4
        p_max_all = _iroot4(N // scale4k)
        for p in range(1, p_max_all + 1, 2):
            p4 = pow4[p]
            remN = N - scale4k * p4
            if remN < 4:
                continue

            q_max_z = _iroot4(remN // 4)
            q_max = min(q_max_z, N // (y_scale * p))
            q_max = min(q_max, _iroot4(N + scale4k_2 * p4))
            if q_max <= 0:
                continue

            q_min = _ceil_root4(scale4k_2 * p4 + 1)
            if q_min % 2 == 0:
                q_min += 1

            if q_min > q_max:
                continue

            divs = _squarefree_divs_mu(p, spf, div_cache)
            cnt, s1, s4 = _coprime_odd_range(p, q_min, q_max, divs, mod, mod)
            if cnt <= 0:
                continue

            term_q4 = (5 * s4) % mod
            term_p4 = (3 * (scale4k_2 % mod) * (p4 % mod) * (cnt % mod)) % mod
            term_pq = ((y_scale % mod) * (p % mod) * (s1 % mod)) % mod
            total = (total + term_q4 + term_p4 + term_pq) % mod

        k += 1

    return total % mod


if __name__ == "__main__":
    print(solve())
