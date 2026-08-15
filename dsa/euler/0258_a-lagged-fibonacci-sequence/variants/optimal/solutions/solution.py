"""Project Euler 258: A lagged Fibonacci sequence

Find g_k mod 20092010 for k = 10^18 where:
g_k = 1 for 0 <= k <= 1999
g_k = g_{k-2000} + g_{k-1999} for k >= 2000.
"""

from __future__ import annotations


def solve(k: int = 10**18, mod: int = 20092010) -> str:
    """Computes g_k mod mod using polynomial ring exponentiation

    modulo the characteristic polynomial x^2000 - x - 1.
    """
    d = 2000

    def mul_poly(a_poly: list[int], b_poly: list[int]) -> list[int]:
        c_poly = [0] * (2 * d - 1)
        for i in range(d):
            ai = a_poly[i]
            if ai == 0:
                continue
            for j in range(d):
                c_poly[i + j] += ai * b_poly[j]

        # Reduce modulo (x^d - x - 1) and mod
        for i in range(2 * d - 2, d - 1, -1):
            c_val = c_poly[i] % mod
            if c_val != 0:
                c_poly[i - d + 1] += c_val
                c_poly[i - d] += c_val

        return [c % mod for c in c_poly[:d]]

    # Exponentiation by squaring: compute x^k mod (x^d - x - 1)
    res = [0] * d
    res[0] = 1

    base = [0] * d
    base[1] = 1

    power = k
    while power > 0:
        if power & 1:
            res = mul_poly(res, base)
        base = mul_poly(base, base)
        power >>= 1

    # g_k = sum_{i=0}^{d-1} res[i] * g_i with g_i = 1 for all i < d
    ans = sum(res) % mod
    return str(ans)


if __name__ == "__main__":
    print(solve())
