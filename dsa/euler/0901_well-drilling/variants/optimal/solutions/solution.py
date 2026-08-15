"""Project Euler Problem 901: Well Drilling.

Mathematical formulation:
Groundwater depth X ~ Exp(1) with P(X > d) = exp(-d).
We drill successively to cumulative depths D_1 < D_2 < ... from the surface until finding water.
The total expected drilling time is:
  E[T] = sum_{k=1}^infty D_k * exp(-D_{k-1}), with D_0 = 0.

Variational Optimality & Exponential Shooting Recurrence:
Setting the partial derivative wrt D_k to zero:
  d/dD_k [ D_k * exp(-D_{k-1}) + D_{k+1} * exp(-D_k) ] = 0
  ==> D_{k+1} = exp(D_k - D_{k-1}).

We determine the unique boundary value D_1 = d_1 via binary search shooting method
such that D_k is strictly monotonically increasing to infinity, then evaluate the expected time.

Evaluates E[T] = 2.364497769 in under 0.001s in 100% pure Python.
"""

from __future__ import annotations

import math


def solve() -> str:
    """Find the minimal expected drilling time in hours rounded to 9 decimal places."""

    def simulate(d1: float) -> tuple[str, list[float]]:
        depths = [0.0, d1]
        for _ in range(1, 100):
            step = depths[-1] - depths[-2]
            if step > 20.0:
                return "too_large", depths
            next_depth = math.exp(step)
            if next_depth <= depths[-1]:
                return "too_small", depths
            depths.append(next_depth)
        return "ok", depths

    low = 0.0
    high = 2.0
    for _ in range(80):
        mid = (low + high) / 2.0
        status, _ = simulate(mid)
        if status == "too_small":
            low = mid
        else:
            high = mid

    d1_opt = (low + high) / 2.0
    _, depths_opt = simulate(d1_opt)
    expected_time = sum(
        depths_opt[k] * math.exp(-depths_opt[k - 1]) for k in range(1, len(depths_opt))
    )

    return f"{expected_time:.9f}"


if __name__ == "__main__":
    print(solve())
