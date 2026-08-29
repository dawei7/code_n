"""Project Euler Problem 511: Sequences with Nice Divisibility Properties.

Find the last nine digits of Seq(1234567898765, 4321), where Seq(n, k)
is the number of sequences {a_i} of length n of divisors of n whose sum + n is divisible by k.
"""

from typing import List

MOD = 10**9

P1, G1 = 998244353, 3
P2, G2 = 1004535809, 3
P3, G3 = 469762049, 3


def _ntt(a: List[int], inv: bool = False, p: int = P1, g: int = G1) -> None:
    n = len(a)
    j = 0
    for i in range(1, n):
        bit = n >> 1
        while j & bit:
            j ^= bit
            bit >>= 1
        j ^= bit
        if i < j:
            a[i], a[j] = a[j], a[i]

    length = 2
    while length <= n:
        wlen = pow(g, (p - 1) // length, p)
        if inv:
            wlen = pow(wlen, p - 2, p)
        half = length >> 1
        for i in range(0, n, length):
            w = 1
            for j in range(half):
                u = a[i + j]
                v = a[i + j + half] * w % p
                a[i + j] = (u + v) % p
                a[i + j + half] = (u - v) % p
                w = w * wlen % p
        length <<= 1

    if inv:
        n_inv = pow(n, p - 2, p)
        for i in range(n):
            a[i] = a[i] * n_inv % p


def _crt3(
    c1: List[int], c2: List[int], c3: List[int], mod: int = MOD
) -> List[int]:
    m12 = P1 * P2
    inv_p1_mod_p2 = pow(P1, P2 - 2, P2)
    inv_m12_mod_p3 = pow(m12 % P3, P3 - 2, P3)

    n = len(c1)
    res = [0] * n
    for i in range(n):
        v1 = c1[i]
        v2 = (c2[i] - v1) * inv_p1_mod_p2 % P2
        x12 = v1 + v2 * P1
        v3 = ((c3[i] - x12) % P3) * inv_m12_mod_p3 % P3
        x = x12 + v3 * m12
        res[i] = x % mod
    return res


def _poly_mul_ntt(
    a: List[int], b: List[int], k: int, mod: int = MOD
) -> List[int]:
    n_size = 1
    while n_size < 2 * k:
        n_size <<= 1

    a_pad = a + [0] * (n_size - len(a))
    b_pad = b + [0] * (n_size - len(b))

    def mul_prime(p: int, g: int) -> List[int]:
        fa = a_pad[:]
        fb = b_pad[:]
        _ntt(fa, False, p, g)
        _ntt(fb, False, p, g)
        fc = [fa[i] * fb[i] % p for i in range(n_size)]
        _ntt(fc, True, p, g)
        return fc

    c1 = mul_prime(P1, G1)
    c2 = mul_prime(P2, G2)
    c3 = mul_prime(P3, G3)

    c = _crt3(c1, c2, c3, mod)

    res = [0] * k
    for i in range(len(c)):
        res[i % k] = (res[i % k] + c[i]) % mod
    return res


def solve(n: int = 1234567898765, k: int = 4321, mod: int = MOD) -> int:
    """Compute Seq(n, k) mod mod using 3-prime NTT circular polynomial exponentiation."""
    divs = [1]
    temp = n
    d = 2
    while d * d <= temp:
        if temp % d == 0:
            count = 0
            while temp % d == 0:
                count += 1
                temp //= d
            divs = [x * (d**i) for x in divs for i in range(count + 1)]
        d += 1
    if temp > 1:
        divs = [x * (temp**i) for x in divs for i in range(2)]

    poly = [0] * k
    for d_val in divs:
        poly[d_val % k] = (poly[d_val % k] + 1) % mod

    res = [0] * k
    res[0] = 1
    base = poly[:]
    exp = n

    while exp > 0:
        if exp & 1:
            res = _poly_mul_ntt(res, base, k, mod)
        base = _poly_mul_ntt(base, base, k, mod)
        exp >>= 1

    target_idx = (-n) % k
    return res[target_idx]


if __name__ == "__main__":
    print(solve())
