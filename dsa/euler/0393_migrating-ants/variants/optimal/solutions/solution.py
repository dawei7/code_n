"""Project Euler Problem 393: Migrating Ants.

Find f(10), the number of valid simultaneous movements of n^2 ants on an nxn grid without collisions
or edge crossings.
"""

from collections import defaultdict
from functools import lru_cache
from typing import Dict, Iterator, List, Tuple

FILLED = 0
HORIZONTAL = 1
VERTICAL = 2


def solve(size: int = 10) -> int:
    """Compute f(size) using row-by-row profile dynamic programming on dual-flow matching."""
    if size & 1:
        return 0

    full = (1 << size) - 1

    @lru_cache(maxsize=None)
    def transitions(
        state: int, last_row: bool
    ) -> Tuple[Tuple[int, int], ...]:
        in1 = state & full
        in2 = state >> size
        counts: Dict[int, int] = defaultdict(int)

        def options(
            occupied: int, out_mask: int, col: int
        ) -> Iterator[Tuple[int, int, int]]:
            bit = 1 << col
            if occupied & bit:
                yield FILLED, occupied, out_mask
                return

            if col + 1 < size:
                next_bit = bit << 1
                if not (occupied & next_bit):
                    yield HORIZONTAL, occupied | bit | next_bit, out_mask

            if not last_row:
                yield VERTICAL, occupied | bit, out_mask | bit

        def fill_row(
            col: int,
            occupied1: int,
            occupied2: int,
            out1: int,
            out2: int,
        ) -> None:
            if col == size:
                if occupied1 == full and occupied2 == full:
                    counts[out1 | (out2 << size)] += 1
                return

            for kind1, next_occ1, next_out1 in options(occupied1, out1, col):
                for kind2, next_occ2, next_out2 in options(
                    occupied2, out2, col
                ):
                    if kind1 != FILLED and kind1 == kind2:
                        continue
                    fill_row(
                        col + 1,
                        next_occ1,
                        next_occ2,
                        next_out1,
                        next_out2,
                    )

        fill_row(0, in1, in2, 0, 0)
        return tuple(counts.items())

    dp: Dict[int, int] = {0: 1}
    for row in range(size):
        last_row = row + 1 == size
        next_dp: Dict[int, int] = defaultdict(int)
        for state, ways in dp.items():
            for out_state, multiplicity in transitions(state, last_row):
                next_dp[out_state] += ways * multiplicity
        dp = dict(next_dp)

    return dp.get(0, 0)


if __name__ == "__main__":
    print(solve())
