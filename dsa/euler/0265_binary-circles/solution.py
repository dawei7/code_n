"""Project Euler 265: Binary Circles

Find S(5), the sum of all unique numeric representations of De Bruijn sequences of order N=5,
starting with N consecutive zeros.
"""

from __future__ import annotations


def solve(n: int = 5) -> str:
    """Computes S(N) by enumerating all circular De Bruijn sequences of order N

    using depth-first search with bitmask window tracking.
    """
    target_len = 1 << n
    mask = target_len - 1
    results: list[int] = []

    def backtrack(
        seq: list[int], visited_mask: int, curr_window: int
    ) -> None:
        if len(seq) == target_len:
            # Validate wrap-around subsequences
            valid = True
            w = curr_window
            temp_mask = visited_mask
            for i in range(n - 1):
                b = seq[i]
                w = ((w << 1) | b) & mask
                if (temp_mask & (1 << w)) != 0:
                    valid = False
                    break
                temp_mask |= 1 << w

            if valid and temp_mask == (1 << target_len) - 1:
                val = 0
                for bit in seq:
                    val = (val << 1) | bit
                results.append(val)
            return

        for b in (0, 1):
            next_w = ((curr_window << 1) | b) & mask
            if (visited_mask & (1 << next_w)) == 0:
                seq.append(b)
                backtrack(seq, visited_mask | (1 << next_w), next_w)
                seq.pop()

    initial_seq = [0] * n
    initial_visited_mask = 1 << 0
    backtrack(initial_seq, initial_visited_mask, 0)

    return str(sum(results))


if __name__ == "__main__":
    print(solve())
