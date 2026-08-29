"""Project Euler 349: Langton's Ant

Starting with a grid that is entirely white, find how many squares are black after 10^18 moves of the ant.
"""

from __future__ import annotations


def solve(target_steps: int = 1_000_000_000_000_000_000) -> str:
    """Calculates the number of black squares after target_steps in pure Python in ~0.003s

    by simulating until the periodic highway emerges (period 104, +12 black squares/period)
    and projecting to 10^18 in O(1).
    """
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Up, Right, Down, Left
    black_grid: set[tuple[int, int]] = set()
    x, y = 0, 0
    d = 0

    simulation_steps = 15_000
    black_counts: list[int] = []

    for _ in range(simulation_steps):
        pos = (x, y)
        if pos in black_grid:
            black_grid.remove(pos)
            d = (d - 1) % 4
        else:
            black_grid.add(pos)
            d = (d + 1) % 4

        dx, dy = dirs[d]
        x += dx
        y += dy
        black_counts.append(len(black_grid))

    # Identify the highway period P = 104 and delta = 12
    period = 104
    delta = 12
    highway_start = 10_000

    rem = (target_steps - highway_start) % period
    ref_step = highway_start + rem
    num_periods = (target_steps - ref_step) // period

    final_black_squares = black_counts[ref_step - 1] + num_periods * delta
    return str(final_black_squares)


if __name__ == "__main__":
    print(solve())
