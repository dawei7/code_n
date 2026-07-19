## General
**Summarize every path ending in the previous row.** Let `previous[col]` be the minimum sum of a falling path that ends at column `col` of the row already processed. For the first row, these values are simply the matrix entries because a path may start at any column.

**Extend only from legal predecessors.** For each cell in the next row, inspect the available predecessor totals at columns `col - 1`, `col`, and `col + 1`. Add the current matrix value to their minimum and store the result in `current[col]`. Boundary columns omit the nonexistent diagonal predecessor. Every path reaching this cell must use exactly one of these predecessors, and extending the cheapest one is therefore optimal; conversely, that predecessor followed by the current cell constructs a valid path with the stored total.

**Finish anywhere in the last row.** Replace `previous` after each row. By induction, it contains the optimum for every possible endpoint of that row. A complete falling path may end at any last-row column, so the answer is `min(previous)` after all rows have been processed. Negative entries require no special treatment because the recurrence compares complete path sums rather than making a locally greedy choice.

## Complexity detail
There are $n^2$ cells and each considers at most three predecessors, giving $O(n^2)$ time. Two arrays of $n$ path totals are retained, so the auxiliary-space cost is $O(n)$.

## Alternatives and edge cases
- **In-place bottom-up dynamic programming:** Add the cheapest predecessor directly into each matrix cell. This keeps $O(n^2)$ time and uses $O(1)$ extra space but mutates the input.
- **Memoized depth-first search:** Explore the three downward moves from every state and cache results. It has the same asymptotic bounds but adds recursion overhead and $O(n^2)$ cached state.
- **Unrestricted predecessor scan:** Checking every column of the previous row and discarding nonadjacent ones remains correct but wastes $O(n^3)$ time.
- **Single-cell matrix:** The only entry is both the start and end, so it is the answer.
- **Negative values:** The minimum path may deliberately include them; no pruning based on a partial positive or negative sum is valid.
