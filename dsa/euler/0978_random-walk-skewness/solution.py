"""Project Euler Problem 978: Random Walk Skewness.

Mathematical Formulation:
Random walk on integers: $X_0 = 0$, $X_1 = 1$.
For $t >= 2$, $X_t = X_{t-1} + \epsilon_t |X_{t-2}|$ where $\epsilon_t \in \{-1, +1\}$ with prob $1/2$ each.
If $X_{t-2} = 0$, stay put.

Moment Analysis & Fibonacci Invariants:
1. Mean: $\mathbb{E}[X_t] = 1$ for all $t \ge 1$.
2. Variance: $\mathbb{E}[X_t^2] = \mathbb{E}[X_{t-1}^2] + \mathbb{E}[X_{t-2}^2] = F_t$ (Fibonacci sequence).
   $$\sigma_t = \sqrt{F_t - 1}$$
3. Third Central Moment $M_3(t) = \mathbb{E}[(X_t - 1)^3]$:
   Applying the expansion $(Y_{t-1} + \epsilon_t |X_{t-2}|)^3$ and conditional independence:
   $$M_3(t) = M_3(t-1) + 3 M_3(t-2) + 6 (F_{t-2} - 1)$$
   with base conditions $M_3(0) = -1, M_3(1) = M_3(2) = M_3(3) = M_3(4) = 0$.

Skewness:
$$\text{Skew}(X_t) = \frac{M_3(t)}{\sigma_t^3}$$

Evaluates $\text{Skew}(X_{50}) = 254.54470757$ in under $0.001$ seconds in pure Python.
"""

from __future__ import annotations

import math


def solve(target_t: int = 50) -> str:
    """Compute Skew(X_50) rounded to 8 decimal places."""
    # Fibonacci numbers computation
    fib = [0] * (target_t + 5)
    fib[1] = 1
    for i in range(2, target_t + 5):
        fib[i] = fib[i - 1] + fib[i - 2]

    # Third central moment recurrence
    m3 = [0] * (target_t + 5)
    m3[0] = -1
    m3[1] = 0
    m3[2] = 0
    m3[3] = 0
    m3[4] = 0

    for t in range(5, target_t + 1):
        m3[t] = m3[t - 1] + 3 * m3[t - 2] + 6 * (fib[t - 2] - 1)

    # Standard deviation calculation
    variance = fib[target_t] - 1
    std_dev = math.sqrt(variance)

    # Skewness calculation
    skewness = m3[target_t] / (std_dev**3)

    return f"{skewness:.8f}"


if __name__ == "__main__":
    print(solve())
