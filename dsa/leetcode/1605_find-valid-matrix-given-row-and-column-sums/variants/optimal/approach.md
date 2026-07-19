## General
**Treat margins as remaining supply and demand.** Start with a zero-filled $m \times n$ result and pointers to the first unfinished row and column. At their intersection, place the smaller of the remaining row sum and remaining column sum. Subtract that amount from both margins.

**Finish at least one margin on every placement.** If the row held the smaller remainder, that row now needs zero more and the row pointer advances. If the column held the smaller remainder, advance the column pointer. When the two remainders were equal, both pointers advance. Thus every iteration permanently completes a row, a column, or both.

Every placed value is non-negative and never exceeds either active remainder, so no row or column can be overfilled. Completed margins never change again. The total unfinished row supply always equals the total unfinished column demand because each placement subtracts the same amount from both sides. Consequently, when one pointer reaches the end, the other side also has no positive remainder, and the constructed matrix has exactly all requested margins.

## Complexity detail
Creating the returned $m \times n$ matrix costs $O(mn)$ time and space. The two pointers advance at most $m+n$ times, so the greedy filling phase costs $O(m+n)$ additional time and $O(1)$ auxiliary state. The required output therefore dominates the total bounds.

## Alternatives and edge cases
- **Fill every cell while recomputing used margins:** This can be correct, but repeatedly summing partial rows and columns costs $O(mn(m+n))$ time.
- **Network flow:** Modeling rows as supplies and columns as demands is valid but introduces a much heavier general-purpose algorithm than this complete bipartite transportation instance needs.
- **Backtracking over cell values:** It explores many unnecessary allocations even though the greedy choice can never make the remaining balanced margins infeasible.
- Zero-sum rows or columns are valid and may cause a pointer to advance after placing zero.
- When both active remainders are equal, both the row and column become complete at the same cell.
- A one-row or one-column input determines the matrix directly.
- The returned matrix may differ from a displayed example; correctness depends on non-negativity, dimensions, and margins rather than exact cell equality.
