"""Project Euler 340: Crazy Function

Find the last 9 digits of S(21^7, 7^21, 12^7), where S(a, b, c) = sum_{n=0}^b F(n)
and F(n) is the recursive McCarthy-type crazy function.
"""

from __future__ import annotations


def solve(
    a_exp: tuple[int, int] = (21, 7),
    b_exp: tuple[int, int] = (7, 21),
    c_exp: tuple[int, int] = (12, 7),
    mod: int = 1_000_000_000,
) -> str:
    """Calculates S(a, b, c) mod mod in pure Python in O(1) time using the exact closed-form identity

    F(n) = n + 4(a - c) + floor((b - n) / a) * (4a - 3c)
    and evaluating the arithmetic progressions analytically.
    """
    a = pow(a_exp[0], a_exp[1])
    b = pow(b_exp[0], b_exp[1])
    c = pow(c_exp[0], c_exp[1])

    # 1. Term 1: sum_{n=0}^b n = b * (b + 1) / 2
    term1 = b * (b + 1) // 2

    # 2. Term 2: sum_{n=0}^b 4*(a - c) = 4 * (a - c) * (b + 1)
    term2 = 4 * (a - c) * (b + 1)

    # 3. Term 3: (4a - 3c) * sum_{u=0}^b floor(u / a)
    q = b // a
    r = b % a
    sum_floor = a * q * (q - 1) // 2 + q * (r + 1)
    term3 = (4 * a - 3 * c) * sum_floor

    # Sum all component terms dynamically
    terms = [term1, term2, term3]
    total_s = sum(t % mod for t in terms) % mod

    return f"{total_s:09d}"


if __name__ == "__main__":
    print(solve())
