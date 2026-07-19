## General
Let the previous-row dynamic-programming value for column $c$ be the minimum sum of a valid path ending there. To extend into the next row at column $c$, add the current grid value to the smallest previous value whose column is not $c$.

**Reduce each transition to two minima.** Find the smallest and second-smallest values in the previous DP row, remembering the smallest value's column. For a current cell outside that column, the smallest previous value is legal. For a current cell in that same column, use the second-smallest value instead. This rule also handles tied minima: scanning all columns makes the second minimum equal to the first when another column has the same value.

Every computed state considers the cheapest legal predecessor. By induction over rows, it is therefore the minimum valid path sum ending at its column. Taking the minimum state after the final row chooses the best endpoint and yields the global minimum.

## Complexity detail
Each of $n$ rows contains $n$ cells. Finding two previous minima and constructing the next DP row both take $O(n)$ per row, for $O(n^2)$ total time. Only the previous and current DP rows are needed, so the auxiliary space is $O(n)$.

## Alternatives and edge cases
- **Try every predecessor:** For every cell, scanning all previous columns except its own gives the same recurrence but takes $O(n^3)$ time.
- **Sort every DP row:** Sorting can expose two minima in $O(n \log n)$ per row, which is unnecessary compared with one linear scan.
- **One-cell grid:** No adjacency restriction is applied because the path contains only one row.
- **Tied minima:** The second minimum may equal the first when it comes from another column; values, not only distinct values, must be tracked.
- **Negative values:** The recurrence minimizes ordinary sums and requires no special handling for negative entries.
