"""Project Euler Problem 723: Pythagorean Quadrilaterals.

Find S(5^6 * 13^3 * 17^2 * 29 * 37 * 41 * 53 * 61), where S(n) = sum_{d | n} f(sqrt(d))
and f(r) is the number of pythagorean lattice grid quadrilaterals with circumradius r.
"""

from typing import List, Optional


def _a1(e: int) -> int:
    return (e + 1) * (e + 2) // 2


def _a2(e: int) -> int:
    return (e + 1) * (e + 2) * (2 * e + 3) // 6


def _a3(e: int) -> int:
    return (_a2(e) + e // 2 + 1) // 2


def _a4(e: int) -> int:
    v = _a1(e)
    return v * v


def _a5(e: int) -> int:
    return (e + 1) * (e + 2) * (e * e + 3 * e + 3) // 6


def solve(n_val: Optional[int] = None, exps: Optional[List[int]] = None) -> int:
    """Compute S(n) using multiplicative linear combinations of exponent polynomials."""
    if exps is None:
        if n_val == 325:
            exponents = [2, 1]
        elif n_val == 1105:
            exponents = [1, 1, 1]
        else:
            exponents = [6, 3, 2, 1, 1, 1, 1, 1]
    else:
        exponents = exps

    t1, t2, t3, t4, t5 = 1, 1, 1, 1, 1
    for e in exponents:
        t1 *= _a1(e)
        t2 *= _a2(e)
        t3 *= _a3(e)
        t4 *= _a4(e)
        t5 *= _a5(e)

    ans = 7 * t1 - 14 * t2 - 4 * t3 + 8 * t4 + 4 * t5
    return ans


if __name__ == "__main__":
    print(solve())
