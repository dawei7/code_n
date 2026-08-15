"""
Project Euler Problem 253: Tidying Up A

Problem Statement:
A small child has a "number caterpillar" consisting of forty jigsaw pieces,
numbered 1 to 40 in order.
The child's father picks up the pieces in random order and places them down.
As pieces are placed, they form distinct connected segments that gradually merge.
Let M be the maximum number of segments encountered during the process.
For a 10-piece caterpillar, the average value of M is 385643/113400 ≈ 3.400732.
For a 40-piece caterpillar, find the average value of M, rounded to 6 decimal places.
"""

import collections


def solve(num_pieces: int = 40) -> str:
    """
    Computes the expected maximum number of segments for a caterpillar of size N.
    Uses dynamic programming over gap multisets.
    """
    memo = {}

    def get_distribution(left_gap: int, right_gap: int, internal_gaps: tuple):
        # Symmetrize boundary gaps
        if left_gap > right_gap:
            left_gap, right_gap = right_gap, left_gap
        state = (left_gap, right_gap, internal_gaps)
        if state in memo:
            return memo[state]

        cur_segments = len(internal_gaps) + 1
        total_unplaced = left_gap + right_gap + sum(internal_gaps)

        if total_unplaced == 0:
            return {cur_segments: 1}

        res = collections.defaultdict(int)

        # 1. Pick a piece from the left boundary gap
        if left_gap > 0:
            # Pick piece 1 (boundary)
            new_gaps = list(internal_gaps)
            if left_gap - 1 > 0:
                new_gaps.append(left_gap - 1)
            new_gaps.sort()
            dist = get_distribution(0, right_gap, tuple(new_gaps))
            for m, count in dist.items():
                res[max(m, cur_segments)] += count

            # Pick piece at distance x from left boundary (2 <= x <= left_gap)
            for x in range(2, left_gap + 1):
                new_l = x - 1
                new_gaps = list(internal_gaps)
                if left_gap - x > 0:
                    new_gaps.append(left_gap - x)
                new_gaps.sort()
                dist = get_distribution(new_l, right_gap, tuple(new_gaps))
                for m, count in dist.items():
                    res[max(m, cur_segments)] += count

        # 2. Pick a piece from the right boundary gap
        if right_gap > 0:
            # Pick piece N (boundary)
            new_gaps = list(internal_gaps)
            if right_gap - 1 > 0:
                new_gaps.append(right_gap - 1)
            new_gaps.sort()
            dist = get_distribution(left_gap, 0, tuple(new_gaps))
            for m, count in dist.items():
                res[max(m, cur_segments)] += count

            # Pick piece at distance x from right boundary (2 <= x <= right_gap)
            for x in range(2, right_gap + 1):
                new_r = x - 1
                new_gaps = list(internal_gaps)
                if right_gap - x > 0:
                    new_gaps.append(right_gap - x)
                new_gaps.sort()
                dist = get_distribution(left_gap, new_r, tuple(new_gaps))
                for m, count in dist.items():
                    res[max(m, cur_segments)] += count

        # 3. Pick a piece from internal gaps
        counts = collections.Counter(internal_gaps)
        for g in sorted(counts.keys()):
            mult = counts[g]
            idx = internal_gaps.index(g)
            rem_gaps = list(internal_gaps[:idx] + internal_gaps[idx + 1 :])

            if g == 1:
                # Fills the gap between two segments (merging them)
                new_gaps = sorted(rem_gaps)
                dist = get_distribution(left_gap, right_gap, tuple(new_gaps))
                for m, count in dist.items():
                    res[max(m, cur_segments)] += mult * count
            else:
                # Pick one of the 2 end pieces (shrinks gap to g - 1)
                new_gaps = sorted(rem_gaps + [g - 1])
                dist = get_distribution(left_gap, right_gap, tuple(new_gaps))
                for m, count in dist.items():
                    res[max(m, cur_segments)] += mult * 2 * count

                # Pick an interior piece (splits gap into g1 and g2)
                for x in range(2, g):
                    g1 = x - 1
                    g2 = g - x
                    new_gaps = sorted(rem_gaps + [g1, g2])
                    dist = get_distribution(
                        left_gap, right_gap, tuple(new_gaps)
                    )
                    for m, count in dist.items():
                        res[max(m, cur_segments)] += mult * count

        memo[state] = res
        return res

    total_dist = collections.defaultdict(int)
    # Exploit left-right reflection symmetry for the first placed piece
    for k in range(1, (num_pieces + 1) // 2 + 1):
        l = k - 1
        r = num_pieces - k
        sym_mult = 1 if k == num_pieces - k + 1 else 2
        dist = get_distribution(l, r, ())
        for m, count in dist.items():
            total_dist[max(m, 1)] += sym_mult * count

    total_ways = sum(total_dist.values())
    expected_m = sum(m * count for m, count in total_dist.items()) / total_ways
    return f"{expected_m:.6f}"


if __name__ == "__main__":
    print(solve())
