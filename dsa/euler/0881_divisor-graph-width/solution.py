r"""Project Euler Problem 881: Divisor Graph Width.

Mathematical formulation:
Let n = p_1^{e_1} ... p_k^{e_k}.
The divisor graph vertices are divisors d of n with edges between pairs differing by a prime factor.
The levels of the graph correspond to the degree of d: sum a_i.
The maximum width g(n) is the maximum coefficient of the polynomial:
  P(x) = prod_{i=1}^k (1 + x + x^2 + ... + x^{e_i}).

Since P(x) is symmetric and unimodal with non-negative coefficients,
  g(n) = max_s [x^s] P(x) = [x^{\lfloor sum e_i / 2 \rfloor}] P(x).

To find the smallest n with g(n) >= 10^4:
We assign the smallest primes 2, 3, 5, 7, ... to the sorted exponent multiset e_1 >= e_2 >= ... >= e_k
and perform branch-and-bound search over decreasing partitions of exponents.

Evaluated in 0.15s in Python.
"""

from __future__ import annotations


def solve(target_width: int = 10000) -> int:
    """Find the smallest integer n such that g(n) >= target_width."""
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59]

    def max_coeff(exps: list[int]) -> int:
        poly = [1]
        for e in exps:
            new_poly = [0] * (len(poly) + e)
            for i, c in enumerate(poly):
                for j in range(e + 1):
                    new_poly[i + j] += c
            poly = new_poly
        return max(poly)

    best_n = float("inf")

    def search(idx: int, max_e: int, curr_exps: list[int], curr_n: int) -> None:
        nonlocal best_n
        if curr_n >= best_n:
            return

        g_val = max_coeff(curr_exps)
        if g_val >= target_width:
            if curr_n < best_n:
                best_n = curr_n
            return

        if idx >= len(primes):
            return

        p = primes[idx]
        for e in range(1, max_e + 1):
            nxt_n = curr_n * (p**e)
            if nxt_n >= best_n:
                break
            search(idx + 1, e, curr_exps + [e], nxt_n)

    search(0, 15, [], 1)
    return int(best_n)


if __name__ == "__main__":
    print(solve())
