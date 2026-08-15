"""Project Euler Problem 624: Two Heads Are Better Than One.

Find Q(P(10^18), 1000000009), where P(n) is the probability that the number of coin tosses M
until two consecutive heads occur is divisible by n.
"""

from typing import List

_MOD = 1_000_000_009


def _mat_mul(
    a: List[List[int]], b: List[List[int]], mod: int
) -> List[List[int]]:
    return [
        [
            (a[0][0] * b[0][0] + a[0][1] * b[1][0]) % mod,
            (a[0][0] * b[0][1] + a[0][1] * b[1][1]) % mod,
        ],
        [
            (a[1][0] * b[0][0] + a[1][1] * b[1][0]) % mod,
            (a[1][0] * b[0][1] + a[1][1] * b[1][1]) % mod,
        ],
    ]


def solve(n: int = 10**18, p: int = _MOD) -> int:
    """Compute Q(P(n), p) using the closed-form Binet-Lucas geometric series formula."""
    res = [[1, 0], [0, 1]]
    base = [[1, 1], [1, 0]]
    bit_str = bin(n)[2:]
    for bit in bit_str:
        res = _mat_mul(res, res, p)
        if bit == "1":
            res = _mat_mul(res, base, p)

    fn_plus_1 = res[0][0]
    fn_minus_1 = res[1][1]
    ln = (fn_minus_1 + fn_plus_1) % p

    pow2 = pow(2, n, p)
    pow4 = (pow2 * pow2) % p

    sign = 1 if (n % 2 == 0) else -1

    num = (pow2 * fn_minus_1 - sign) % p
    den = (pow4 - pow2 * ln + sign) % p

    ans = (num * pow(den, p - 2, p)) % p
    return ans


if __name__ == "__main__":
    print(solve())
