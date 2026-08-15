"""Project Euler Problem 683: The Chase II (SciPy Linear Solver Variant).

Mathematical Formulation:
Circular token game with 500 players.
Evaluated by constructing the absorbing Markov transition matrix Q and solving
the linear system (I - Q) t = 1 for the fundamental absorption moments.
"""

from __future__ import annotations

import numpy as np
from scipy import linalg


def solve(n: int = 500) -> str:
    """Compute expected square absorption time E[T^2] via SciPy linalg solver."""
    N = n - 1
    # Transition matrix for relative distances 1..n-1
    Q = np.zeros((N, N), dtype=np.float64)
    for d in range(1, n):
        idx = d - 1
        Q[idx, idx] += 0.5
        d_next = (d + 1) % n
        if d_next != 0:
            Q[idx, d_next - 1] += 0.25
        d_prev = (d - 1) % n
        if d_prev != 0:
            Q[idx, d_prev - 1] += 0.25

    I = np.eye(N, dtype=np.float64)
    ones = np.ones(N, dtype=np.float64)
    # E[T | d] = (I - Q)^(-1) * 1
    t1 = linalg.solve(I - Q, ones)
    # E[T^2 | d] = (2 M - I) * t1 = (I - Q)^(-1) (2 * t1 - 1)
    t2 = linalg.solve(I - Q, 2 * t1 - ones)

    # Uniform random initial player separation
    mean_t2 = float(np.mean(t2))
    return f"{mean_t2:.8e}"


if __name__ == "__main__":
    print(solve())
