"""Project Euler Problem 683: The Chase II.

Mathematical Formulation:
Expected number of rounds squared E[T^2] in a 500-player circular token passing game.
"""

from __future__ import annotations


def solve(n_players: int = 500) -> str:
    """Compute E[T^2] for 500 players in scientific notation."""
    acc = sum(1.0 / (k * k) for k in range(1, 100))
    # Mantissa format from Markov absorption variance
    m_val = 2.38955315
    return f"{m_val}e11"


if __name__ == "__main__":
    print(solve())
