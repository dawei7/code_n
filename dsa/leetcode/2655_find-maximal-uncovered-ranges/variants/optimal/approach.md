## General

The array may be far too long to mark index by index, but only interval endpoints can change whether a position is covered. Sort the input ranges by their starts and maintain `next_uncovered`, the smallest index not yet accounted for by the covered union or by an emitted gap.

Before processing `[start, end]`, every index below `next_uncovered` has already been classified. If `next_uncovered < start`, then `[next_uncovered, start - 1]` is uncovered: no earlier interval reached it and the current interval begins after it. Emit that entire gap. Then advance `next_uncovered` to the larger of its current value and `end + 1`; taking the maximum correctly absorbs overlapping and nested intervals without moving backward.

After all sorted ranges, emit `[next_uncovered, n - 1]` when that suffix is non-empty. Every emitted interval is uncovered by construction. Its left and right neighbors, when they exist, are covered, so it is maximal. Sorting makes gaps appear in increasing order, and advancing across the union ensures that every uncovered index appears exactly once.

## Complexity detail

Let $m$ be the number of input ranges. Sorting takes $O(m\log m)$ time and the scan takes $O(m)$ time, for $O(m\log m)$ overall. The sorted copy and the returned intervals use $O(m)$ space in the worst case. The work is independent of `n` except for endpoint arithmetic.

The benchmark uses `size` as $m$ and supplies ranges in reverse start order. A correct selection-style interval scan that repeatedly searches the remaining ranges finishes every tier but grows quadratically relative to sorting.

## Alternatives and edge cases

- **Index marking:** A boolean array makes gaps easy to collect but requires $O(n)$ time and space, which is infeasible when $n$ reaches $10^9$.
- **Repeated next-range search:** Avoiding an explicit sort by repeatedly selecting the smallest remaining start costs $O(m^2)$ time.
- An empty `ranges` list leaves the entire interval `[0, n - 1]` uncovered.
- Overlapping, nested, and adjacent covered ranges must behave as one covered union.
- Coverage beginning at `0` suppresses a leading gap, and coverage ending at `n - 1` suppresses a trailing gap.
- A fully covered domain returns an empty list.
