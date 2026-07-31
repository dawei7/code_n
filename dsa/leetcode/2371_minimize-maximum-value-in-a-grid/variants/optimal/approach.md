## General

Each cell must be larger than every originally smaller cell in its own row and column. Because all original values are distinct, sorting the cells produces an unambiguous order in which all such prerequisites appear before the cell that depends on them.

**Track the strongest processed prerequisite.** Maintain the greatest replacement assigned so far in each row and in each column. When processing cell `(r, c)`, every smaller original value in row `r` or column `c` has already been assigned, and every larger one remains unprocessed. The new replacement must exceed both recorded maxima, so assign:

`score = max(row_max[r], col_max[c]) + 1`.

Then store `score` in the answer and update both maxima. The value is positive even when the cell has no smaller row or column neighbor because both maxima initially equal zero.

**Why the greedy score minimizes the global maximum.** Any valid result must assign the current cell at least one more than the greatest score among its smaller same-row and same-column prerequisites. The algorithm chooses exactly this lower bound. By induction over ascending original values, no valid replacement can give any processed cell a smaller score than the greedy result. Consequently, no alternative can achieve a smaller overall maximum.

The distinct-value guarantee matters: there is no group of equal original values that would require simultaneous processing before row and column maxima are updated.

## Complexity detail

Let $N = mn$ be the number of cells. Building and sorting the cell list costs $O(N \log N)$ time, and the subsequent scan costs $O(N)$ time. The sorted cells, output matrix, and row and column maxima use $O(N + m + n) = O(N)$ space.

## Alternatives and edge cases

- **Directed acyclic graph:** Connecting each cell to its next larger neighbor in every row and column and computing longest-path levels also models the ordering constraints, but it needs more graph machinery and edges.
- **Repeated minimum selection:** Selecting the smallest remaining original cell by a full scan preserves the same greedy logic but takes $O(N^2)$ time.
- **Single row or column:** The answer is simply the rank of every value within that line.
- **Unrelated cells:** Cells sharing neither a row nor a column may receive the same score; forcing all replacement values to be distinct can needlessly increase the maximum.
- **Single cell:** With no comparisons to preserve, the optimal replacement is `1`.
- **Distinct originals:** Updating maxima immediately is correct only because no two original values tie.
