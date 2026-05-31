"""Example solution for dp_01: Fibonacci.

Compute n-th Fibonacci number efficiently.

Run with:
    python run_challenge.py dp_01 player_scripts/solve_dp_01.py
"""


def solve(n: int) -> int:
    """Bottom-up DP Fibonacci - O(n) solution."""
    if n <= 1:
        return n

    previous_value, current_value = 0, 1
    for _ in range(2, n + 1):
        previous_value, current_value = current_value, previous_value + current_value

    return current_value
