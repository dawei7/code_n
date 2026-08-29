"""Project Euler Problem 672: One More One.

Find H(10^9) mod 1117117717, where H(K) = S((7^K - 1) / 11) and S(N) is the sum of g(n)
for n <= N under the recursive division-by-7 or add-1 process.
"""

from typing import List

_MOD = 1_117_117_717


def _mat_mul(a: List[List[int]], b: List[List[int]], mod: int = _MOD) -> List[List[int]]:
    res = [[0] * 4 for _ in range(4)]
    for i in range(4):
        ai = a[i]
        for k in range(4):
            aik = ai[k]
            if aik == 0:
                continue
            bk = b[k]
            res[i][0] = (res[i][0] + aik * bk[0]) % mod
            res[i][1] = (res[i][1] + aik * bk[1]) % mod
            res[i][2] = (res[i][2] + aik * bk[2]) % mod
            res[i][3] = (res[i][3] + aik * bk[3]) % mod
    return res


def _mat_pow(m: List[List[int]], e: int, mod: int = _MOD) -> List[List[int]]:
    r = [[1 if i == j else 0 for j in range(4)] for i in range(4)]
    cur = m
    power = e
    while power > 0:
        if power & 1:
            r = _mat_mul(cur, r, mod)
        power >>= 1
        if power:
            cur = _mat_mul(cur, cur, mod)
    return r


def _digit_matrix(r: int, mod: int = _MOD) -> List[List[int]]:
    c1 = (-6 + 7 * r - (r * (r + 1)) // 2) % mod
    c2 = 0 if r == 6 else (6 - r) % mod
    return [
        [7 % mod, r % mod, 21 % mod, c1],
        [0, 1, 0, c2],
        [0, 0, 7 % mod, r % mod],
        [0, 0, 0, 1],
    ]


def _get_period_digits() -> List[int]:
    den = 11
    base = 7
    rem = 1 % den
    digits: List[int] = []
    for _ in range(10):
        rem *= base
        digits.append(rem // den)
        rem %= den
    return digits


def solve(k: int = 1_000_000_000, mod: int = _MOD) -> int:
    """Compute H(K) modulo 1117117717 using base-7 repeating digit linear state transition matrix exponentiation."""
    a_digits = _get_period_digits()
    b_digits = a_digits[1:] + a_digits[:1]

    total_digits = k - 1
    full_blocks = total_digits // 10
    rem_digits = total_digits % 10

    m_block = [
        [1 if i == j else 0 for j in range(4)] for i in range(4)
    ]
    for d in b_digits:
        md = _digit_matrix(d, mod)
        m_block = _mat_mul(md, m_block, mod)

    v = [0, 0, 0, 1]

    if full_blocks:
        m_pow = _mat_pow(m_block, full_blocks, mod)
        v = [
            (
                m_pow[0][0] * v[0]
                + m_pow[0][1] * v[1]
                + m_pow[0][2] * v[2]
                + m_pow[0][3] * v[3]
            )
            % mod,
            (
                m_pow[1][0] * v[0]
                + m_pow[1][1] * v[1]
                + m_pow[1][2] * v[2]
                + m_pow[1][3] * v[3]
            )
            % mod,
            (
                m_pow[2][0] * v[0]
                + m_pow[2][1] * v[1]
                + m_pow[2][2] * v[2]
                + m_pow[2][3] * v[3]
            )
            % mod,
            (
                m_pow[3][0] * v[0]
                + m_pow[3][1] * v[1]
                + m_pow[3][2] * v[2]
                + m_pow[3][3] * v[3]
            )
            % mod,
        ]

    for d in b_digits[:rem_digits]:
        md = _digit_matrix(d, mod)
        v = [
            (
                md[0][0] * v[0]
                + md[0][1] * v[1]
                + md[0][2] * v[2]
                + md[0][3] * v[3]
            )
            % mod,
            (
                md[1][0] * v[0]
                + md[1][1] * v[1]
                + md[1][2] * v[2]
                + md[1][3] * v[3]
            )
            % mod,
            (
                md[2][0] * v[0]
                + md[2][1] * v[1]
                + md[2][2] * v[2]
                + md[2][3] * v[3]
            )
            % mod,
            (
                md[3][0] * v[0]
                + md[3][1] * v[1]
                + md[3][2] * v[2]
                + md[3][3] * v[3]
            )
            % mod,
        ]

    return v[0] % mod


if __name__ == "__main__":
    print(solve())
