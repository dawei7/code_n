## General

**Label each available-seat island.** Filter out occupied seats and order the remaining rows by `seat_id`. Within one run of consecutive available IDs, both `seat_id` and `ROW_NUMBER()` increase by one, so their difference stays constant. The difference changes after an occupied seat or a missing integer ID. Therefore `seat_id - ROW_NUMBER() OVER (ORDER BY seat_id)` is an exact group label for each available island.

**Summarize and select the longest runs.** Group by that label. `MIN(seat_id)` and `MAX(seat_id)` recover the island boundaries, while `COUNT(*)` gives its length. Dense-rank these summaries by length descending. Every maximum-length island receives rank 1, so filtering to that rank preserves all ties instead of choosing an arbitrary single run.

The grouping is correct in both directions: consecutive available seats retain one difference and thus one group, while any break in integer adjacency changes the difference and starts another group. Aggregation consequently produces every maximal available run exactly once. Ranking returns precisely those whose length equals the global maximum, and the final ascending sort satisfies the output order.

## Complexity detail

Let $n$ be the number of rows in `Cinema`. Filtering is linear, while the window ordering and final result ordering require $O(n\log n)$ time in the general case. Grouping and ranking remain within that bound. Database engines may avoid some sorting with a useful `seat_id` access path, but the required bound does not assume that optimization.

The window and grouping stages may materialize up to $O(n)$ rows, so auxiliary working space is $O(n)$.

## Alternatives and edge cases

- **Correlated prefix count:** Replacing `ROW_NUMBER()` with a count of earlier free seats produces the same island key but can rescan the table for every free row, leading to $O(n^2)$ work.
- **`LAG` plus cumulative sum:** Mark every row whose predecessor is not `seat_id - 1`, then cumulatively sum the markers. This is correct but needs two window stages instead of the compact difference invariant.
- **Recursive traversal:** Walking from each run start to successive IDs is more verbose and depends on recursive-CTE behavior and limits.
- Multiple maximum-length runs must all be returned; `LIMIT 1` is incorrect.
- Missing seat IDs break a run even when the rows on both sides are marked free.
- Physical input order is irrelevant because the window explicitly orders by `seat_id`.
- A one-seat run has equal first and last IDs and length 1.
- The output sort is by `first_seat_id`, not by run length or discovery order.
