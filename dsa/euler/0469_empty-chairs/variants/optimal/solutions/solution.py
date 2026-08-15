"""Project Euler Problem 469: Empty Chairs.

Find E(10^18), the expected fraction of empty chairs around a round table
when knights randomly sit with at least one empty chair between each other,
rounded to 14 decimal places.
"""

from decimal import Decimal, getcontext

getcontext().prec = 50


def solve(n_chairs: int = 10**18) -> str:
    """Compute E(n) using high-precision Decimal DP recurrence and asymptotic convergence."""
    steps = 100 if n_chairs > 100 else n_chairs
    l_arr = [Decimal(0)] * (steps + 1)
    cum = Decimal(0)

    for n in range(1, steps + 1):
        if n >= 2:
            cum += l_arr[n - 2]
        l_arr[n] = Decimal(1) + (Decimal(2) / Decimal(n)) * cum

    if n_chairs <= steps:
        k = Decimal(1) + l_arr[n_chairs - 3]
        ans = Decimal(1) - k / Decimal(n_chairs)
    else:
        k = Decimal(1) + l_arr[steps - 3]
        ans = Decimal(1) - k / Decimal(steps)

    return f"{ans:.14f}"


if __name__ == "__main__":
    print(solve())
