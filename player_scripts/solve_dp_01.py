"""Example solution for dp_01: Fibonacci.

Compute n-th Fibonacci number efficiently.

Run with:
    python run_challenge.py dp_01 player_scripts/solve_dp_01.py
"""

from code_n.api import get_counter


def solve(n: int) -> int:
    """Bottom-up DP Fibonacci - O(n) solution."""
    counter = get_counter()

    if n <= 1:
        return n

    a, b = 0, 1
    for i in range(2, n + 1):
        counter.write(f"dp[{i}]")  # Count the computation
        a, b = b, a + b

    return b
