
## General

Updating every covered cell separately repeats work wherever query rectangles are large or overlap. A two-dimensional difference matrix records only where each rectangle's contribution starts and stops.

**Encoding one inclusive rectangle**

For a query `[row1, col1, row2, col2]`, add one at its upper-left corner. Subtract one immediately below the rectangle and immediately to its right when those positions exist. The lower-right correction is then added back because the two subtractions overlap there. Thus each query changes at most four entries:

- add at `difference[row1][col1]`;
- subtract at `difference[row2 + 1][col1]` when `row2 + 1 < n`;
- subtract at `difference[row1][col2 + 1]` when `col2 + 1 < n`;
- add at `difference[row2 + 1][col2 + 1]` when both indices are valid.

**Recovering every cell**

After all queries have been encoded, take a two-dimensional prefix sum in row-major order. At `[row][col]`, add the prefix above and the prefix to the left, then subtract the upper-left prefix because it was counted twice. The resulting value is the sum of all rectangle markers whose regions contain that cell.

For any one query, these four signed markers make its reconstructed contribution exactly one inside the inclusive rectangle and zero outside it. Prefix sums are linear, so reconstructing the combined markers produces the sum of every query's contribution, which is precisely the requested final matrix.

## Complexity detail

Let $q$ be the number of queries. Each query creates at most four constant-time updates, costing $O(q)$. Reconstructing the $n \times n$ matrix costs $O(n^2)$, for $O(n^2 + q)$ total time. The difference matrix is also the returned matrix, so the algorithm uses $O(n^2)$ space including the output and $O(1)$ auxiliary space beyond it.

## Alternatives and edge cases

- **Direct rectangle updates:** Iterating through every cell of every query is easy to implement but can require $O(qn^2)$ time when all rectangles cover the full matrix.
- **Row-wise difference arrays:** Marking the horizontal interval on every covered row reduces each query to $O(n)$ work and reconstructs rows in $O(n^2)$, but remains slower than four-corner updates for tall rectangles.
- **Boundary-touching rectangles:** A rectangle may end on the last row or column; its out-of-matrix cancellation marker must simply be omitted.
- **Single-cell and repeated queries:** The same four-corner rule handles a one-cell rectangle, and repeated rectangles correctly accumulate independent increments.
- **Inclusive lower-right corner:** Cancellation happens at `row2 + 1` and `col2 + 1`, not at `row2` or `col2`.
