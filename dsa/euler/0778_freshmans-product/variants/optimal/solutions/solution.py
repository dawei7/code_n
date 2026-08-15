"""Project Euler Problem 778: Freshman's Product.

Find F(234567, 765432) modulo 10^9+9, the sum of all x_1 ⊠ ... ⊠ x_R for 0 <= x_i <= M,
where ⊠ denotes digitwise multiplication modulo 10.
"""

from typing import List

_MOD = 1_000_000_009


def _freshman_product(a: int, b: int) -> int:
    res = 0
    place = 1
    while a > 0 or b > 0:
        da = a % 10
        db = b % 10
        res += ((da * db) % 10) * place
        place *= 10
        a //= 10
        b //= 10
    return res


def _digit_counts_upto(n: int, pos: int) -> List[int]:
    base = 10**pos
    higher = n // (base * 10)
    cur = (n // base) % 10
    lower = n % base

    counts = [higher * base] * 10
    for d in range(cur):
        counts[d] += base
    counts[cur] += lower + 1
    return counts


def _mat_mul(A: List[List[int]], B: List[List[int]], mod: int) -> List[List[int]]:
    C = [[0] * 10 for _ in range(10)]
    for i in range(10):
        Ai = A[i]
        for k in range(10):
            aik = Ai[k]
            if aik:
                Bk = B[k]
                for j in range(10):
                    C[i][j] = (C[i][j] + aik * Bk[j]) % mod
    return C


def _mat_pow(A: List[List[int]], exp: int, mod: int) -> List[List[int]]:
    R = [[0] * 10 for _ in range(10)]
    for i in range(10):
        R[i][i] = 1

    cur = A
    e = exp
    while e > 0:
        if e & 1:
            R = _mat_mul(R, cur, mod)
        cur = _mat_mul(cur, cur, mod)
        e >>= 1
    return R


def solve(R: int = 234567, M: int = 765432, mod: int = _MOD) -> int:
    """Compute F(R, M) mod 10^9+9 using digit independence and 10x10 matrix exponentiation."""
    max_digits = len(str(M))
    ans = 0
    pow10 = 1

    for pos in range(max_digits):
        counts = _digit_counts_upto(M, pos)

        A = [[0] * 10 for _ in range(10)]
        for s in range(10):
            row = A[s]
            for d in range(10):
                t = (s * d) % 10
                row[t] = (row[t] + counts[d]) % mod

        P = _mat_pow(A, R, mod)

        row1 = P[1]
        digit_sum = 0
        for digit, ways in enumerate(row1):
            digit_sum = (digit_sum + digit * ways) % mod

        ans = (ans + digit_sum * pow10) % mod
        pow10 = (pow10 * 10) % mod

    return ans


if __name__ == "__main__":
    print(solve())
