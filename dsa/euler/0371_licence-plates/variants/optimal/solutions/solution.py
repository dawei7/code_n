"""Project Euler Problem 371: Licence Plates.

Find the expected number of 3-digit licence plates (000-999) needed to see two that sum to 1000,
rounded to 8 decimal places.
"""

from typing import List


def solve(total_plates: int = 1000) -> str:
    """Compute the expected plates to win via backward dynamic programming on the 2D Markov chain."""
    num_pairs = (total_plates - 2) // 2  # 499 complementary pairs (x, 1000 - x)

    # E1[k]: expected additional plates given k unmatched pairs seen and 500 already seen
    e1: List[float] = [0.0] * (num_pairs + 1)
    for k in range(num_pairs, -1, -1):
        next_e1 = e1[k + 1] if k < num_pairs else 0.0
        # (1 - (1 + k)/1000) * E1[k] = 1 + ((998 - 2k)/1000) * E1[k+1]
        e1[k] = (total_plates + (2 * num_pairs - 2 * k) * next_e1) / (
            total_plates - 1 - k
        )

    # E0[k]: expected additional plates given k unmatched pairs seen and 500 not seen
    e0: List[float] = [0.0] * (num_pairs + 1)
    for k in range(num_pairs, -1, -1):
        next_e0 = e0[k + 1] if k < num_pairs else 0.0
        # (1 - (1 + k)/1000) * E0[k] = 1 + ((998 - 2k)/1000) * E0[k+1] + (1/1000) * E1[k]
        e0[k] = (
            total_plates + (2 * num_pairs - 2 * k) * next_e0 + e1[k]
        ) / (total_plates - 1 - k)

    return f"{e0[0]:.8f}"


if __name__ == "__main__":
    print(solve())
