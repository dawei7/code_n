"""Project Euler 339: Peredur Fab Efrawg

Find E(10000) rounded to 6 decimal places, where E(n) is the expected final number
of black sheep under Peredur's optimal removal strategy.
"""

from __future__ import annotations


def solve(n: int = 10_000) -> str:
    """Calculates E(n) in pure Python in O(n) time using the optimal-stopping

    martingale scale function formulation on the birth-death chain:
    B[b] = B[b-1] + (2b - 1 - B[b-1]) * (2p / (1 + p))
    and E(n) = 0.5 * B[n-1] + 0.5 * (B[n] + (2n - B[n]) * R_n).
    """
    # 1. Compute stoppable boundary values B[b] for b = 1 .. n
    b_arr = [0.0] * (n + 1)
    p = 1.0  # Central binomial coefficient probability C(2k, k) / 4^k

    for b in range(1, n + 1):
        r = (2.0 * p) / (1.0 + p)
        m = 2 * b - 1
        b_arr[b] = b_arr[b - 1] + (m - b_arr[b - 1]) * r
        # Update central binomial probability for next step: p_{k+1} = p_k * (2k+1) / (2k+2)
        p = p * (2 * b - 1) / (2 * b)

    # 2. Compute scale function ratio R_n = 1 / sum_{k=0}^{n-1} [binom(2n-1, n) / binom(2n-1, n+k)]
    term = 1.0
    denom = 1.0
    for k in range(1, n):
        term *= (n - k) / (n + k)
        denom += term
        if term < 1e-18:
            break
    r_n = 1.0 / denom

    # 3. State value after black bleats: V(2n, n+1) = B[n] + (2n - B[n]) * R_n
    v_next = b_arr[n] + (2 * n - b_arr[n]) * r_n

    # 4. Expected value from initial state (n, n) before first bleat:
    # With prob 1/2, white bleats -> state (n-1, n+1) reduced to B[n-1]
    # With prob 1/2, black bleats -> state (n+1, n-1) with value V_next
    e_n = 0.5 * b_arr[n - 1] + 0.5 * v_next

    return f"{e_n:.6f}"


if __name__ == "__main__":
    print(solve())
