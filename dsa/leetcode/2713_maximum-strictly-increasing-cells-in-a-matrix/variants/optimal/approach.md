## General

A legal move always increases the value, so the implicit graph of moves is acyclic when cells are ordered by value. This makes a bottom-up longest-path dynamic program possible: process smaller values before larger ones.

For each row, maintain the greatest sequence length already achieved by a processed cell in that row. Maintain the analogous maximum for every column. When considering cell `(row, column)`, any valid predecessor is a smaller-valued cell in one of those two lines. Therefore its best length is

$$
1 + \max(\texttt{row_best[row]},\texttt{column_best[column]}).
$$

**Why equal values require a batch.** Cells with the same value cannot be consecutive because moves must be strictly increasing. Their lengths must all be computed from state containing only smaller values. Store the proposed updates for the entire value group, then apply them to the row and column maxima only after the whole group has been evaluated.

Grouping coordinates by value and visiting the keys in sorted order supplies the required processing order. Every candidate predecessor represented by a row or column maximum is smaller because of deferred updates. Conversely, the last cell of any valid predecessor sequence shares the relevant row or column, so its length is included in one of those maxima. The recurrence therefore finds the optimal sequence ending at every cell, and the largest computed length is the requested answer.

## Complexity detail

Let $N=mn$ be the number of cells. Building the value groups takes $O(N)$ expected time. Sorting at most $N$ distinct values takes $O(N\log N)$ time, and processing all coordinates and updates takes another $O(N)$, for $O(mn\log(mn))$ total time. The groups and deferred updates use $O(mn)$ space; row and column maxima add $O(m+n)$. The benchmark uses `size` as $mn$.

## Alternatives and edge cases

- **Scan every possible predecessor:** After sorting cells, checking all earlier smaller cells that share a row or column is correct but takes $O((mn)^2)$ time in the worst case.
- **Depth-first search over explicit moves:** Materializing every larger cell in each row and column can create a quadratic graph before memoization helps.
- **Ordered row and column structures:** Per-line sorting with binary search can support other DP formulations, but their state and duplicate handling are more complicated than global value batching.
- All-equal matrices have answer $1$ because no move is strictly increasing.
- Equal values in a shared row or column must never update one another within the same batch.
- Negative entries require no special case; only relative order matters.
- A one-row or one-column matrix may still visit every cell when all values are distinct.
- The dimensions can each be large, but their product—not either dimension alone—bounds the total work.

