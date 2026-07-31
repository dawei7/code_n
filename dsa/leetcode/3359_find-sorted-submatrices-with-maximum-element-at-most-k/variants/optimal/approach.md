## General

Fix a column $j$ as the right edge of a rectangle. For every row $i$, compute `widths[i][j]`: the longest suffix ending at $j$ whose values are all at most $k$ and are non-increasing from left to right. Scan each row once. A value above $k$ resets the width to zero; otherwise the previous suffix extends exactly when the preceding value is also legal and is at least the current value.

**Turn rectangles into interval minima.** Choose a bottom row $b$ and a top row $t\le b$. Every selected row must support the same left boundary. Consequently, the number of valid left edges for this fixed right edge and row interval is

$$
\min_{t\le i\le b}\texttt{widths}[i][j].
$$

Each possible left edge gives one distinct rectangle. The task for column $j$ is therefore to sum the minimum over every contiguous subarray of its vertical width sequence.

Process the widths from top to bottom with an increasing monotonic stack of `(width, count)` pairs. `ending_sum` stores the sum of minima for all row intervals ending at the current row. When a new width is no larger than stack entries, pop those entries, subtract their former contributions, and merge their counts because the new width becomes the minimum for all those intervals. Add the new contribution and then add `ending_sum` to the global answer.

Every rectangle has one unique right column and bottom row. Its row interval contributes exactly its minimum legal suffix width, which counts precisely the left boundaries that keep every row valid. Thus every qualifying rectangle is counted once, while a rectangle containing an oversized value or an increasing adjacent pair has zero support in at least one selected row and is excluded.

## Complexity detail

Let $m$ and $n$ be the matrix dimensions. Computing all suffix widths takes $O(mn)$ time. Each width is pushed once and popped at most once by its column's monotonic stack, so the vertical phase is also $O(mn)$. Total time is $O(mn)$.

The width table occupies $O(mn)$ space, and one column stack uses another $O(m)$ space, which does not change the $O(mn)$ bound.

The benchmark size is $m$, with a single column and every value equal to one. The optimal stack processes the $m$ cells once. A baseline that scans every possible top row separately for each bottom row performs $\Theta(m^2)$ work.

## Alternatives and edge cases

- **Enumerate every rectangle:** Directly checking all row and column bounds is polynomially much slower and repeatedly inspects the same cells.
- **Scan every top row for each bottom row:** Using the precomputed widths is correct, but explicitly recomputing the minimum for all vertical intervals costs $O(m^2n)$.
- **Histogram area counting:** Maximal-rectangle techniques count areas or maximal shapes, whereas this task needs the number of all valid rectangles.
- **Strictly decreasing check:** The required rows are non-increasing, so equal adjacent values must extend a run.
- **Value above $k$:** Its suffix width is zero and it prevents every rectangle containing that cell.
- **Increasing adjacent pair:** A legal suffix must begin after that pair even when both values are at most $k$.
- **Single column:** Row ordering is automatic; the problem reduces to counting vertical intervals containing only legal cells.
- **Single row:** Each legal non-increasing run of length $r$ contributes $r(r+1)/2$ column intervals.
- **Zero widths in the stack:** They correctly reset `ending_sum` to zero for intervals crossing an illegal row.
