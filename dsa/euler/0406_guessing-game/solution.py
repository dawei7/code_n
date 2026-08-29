"""Project Euler Problem 406: Guessing Game.

Find sum_{k=1..30} C(10^12, sqrt(k), sqrt(F_k)) rounded to 8 decimal places,
where C(n, a, b) is the minimax worst-case cost of guessing a number from 1 to n with costs a and b.
"""

from math import comb, sqrt
from typing import List


def max_capacity(t: float, a: float, b: float) -> int:
    """Compute maximum range size searchable with cost budget t via hockey-stick sum of binomials."""
    u_max = int(t / a)
    total = 0
    for u in range(u_max + 1):
        v_max = int((t - u * a) / b)
        total += comb(u + v_max + 1, u + 1)
    return total


def min_cost(n_val: int, a: float, b: float) -> float:
    """Bisection root finding for the minimal cost t such that capacity(t) >= n_val."""
    if n_val <= 1:
        return 0.0

    hi = 1.0
    while max_capacity(hi, a, b) < n_val:
        hi *= 2.0

    lo = 0.0
    for _ in range(80):
        mid = (lo + hi) / 2.0
        if max_capacity(mid, a, b) >= n_val:
            hi = mid
        else:
            lo = mid

    return hi


def solve(n_target: int = 10**12, k_limit: int = 30) -> str:
    """Compute sum_{k=1..k_limit} C(n_target, sqrt(k), sqrt(F_k))."""
    # Fibonacci numbers F_1..F_30
    fib: List[int] = [0, 1, 1]
    for _ in range(3, k_limit + 1):
        fib.append(fib[-1] + fib[-2])

    total_cost = 0.0
    for k in range(1, k_limit + 1):
        a_cost = sqrt(float(k))
        b_cost = sqrt(float(fib[k]))
        total_cost += min_cost(n_target, a_cost, b_cost)

    return f"{total_cost:.8f}"


if __name__ == "__main__":
    print(solve())
