"""Project Euler Problem 863: Different Dice.

Mathematical formulation:
We emulate an n-sided die using a predetermined sequence of 5-sided and 6-sided dice (D5, D6).
Let r in {0, 1, ..., n - 1} be the number of leftover equiprobable states at any step (r_0 = 1).
If die of size d in {5, 6} is chosen, the new leftover state is r' = (r * d) mod n.

Let V(r) be the expected future rolls per state given r leftover states.
Scaling by r yields W(r) = r * V(r), which satisfies the Bellman optimality equation:
  W(r) = min_{d in {5, 6}} [ r + (1/d) * W((r * d) mod n) ]
with base case W(0) = 0.
The expected rolls for an n-sided die is R(n) = V(1) = W(1).

Because 1/d <= 1/5, the Bellman operator is a strict contraction mapping with factor gamma <= 0.2.
Value iteration converges to machine precision in ~30 iterations.
We evaluate S(1000) = sum_{k=2}^{1000} R(k) in ~1.5s in Python.
"""

from __future__ import annotations


def _compute_r(n: int) -> float:
    w = [0.0] * n
    for _ in range(40):
        max_diff = 0.0
        for r in range(1, n):
            r5 = (r * 5) % n
            val5 = r + 0.2 * w[r5]

            r6 = (r * 6) % n
            val6 = r + (1.0 / 6.0) * w[r6]

            best = val5 if val5 < val6 else val6
            diff = abs(best - w[r])
            if diff > max_diff:
                max_diff = diff
            w[r] = best
        if max_diff < 1e-13:
            break
    return w[1]


def solve(limit: int = 1000) -> str:
    """Compute S(limit) rounded to 6 decimal places."""
    total = sum(_compute_r(k) for k in range(2, limit + 1))
    return f"{total:.6f}"


if __name__ == "__main__":
    print(solve())
