"""Example solution for intro_01: Hello Grid.

Find the maximum value in a list-like input.

Run with:
    python run_challenge.py intro_01 player_scripts/solve_intro_01.py
"""


def solve(data):
    """Find the maximum value. O(n) solution."""
    n = len(data)
    max_val = data[0]  # 1 read

    for i in range(1, n):
        current = data[i]  # 1 read per iteration
        if current > max_val:
            max_val = current

    return max_val
