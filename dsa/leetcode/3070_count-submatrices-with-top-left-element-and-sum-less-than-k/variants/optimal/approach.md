## General

**Represent every valid submatrix by its bottom-right corner.** A submatrix that contains `grid[0][0]` must start at the matrix's top-left corner. Choosing a cell `(row, column)` as its opposite corner therefore identifies exactly one candidate: all cells from row `0` through `row` and column `0` through `column`.

**Build each anchored sum during one traversal.** Maintain `column_sums[column]` as the sum of that column from row `0` through the current row. At the start of a new row, set `rectangle_sum` to zero. Moving from left to right, first add the current cell to its column sum and then add that updated column sum to `rectangle_sum`.

After processing column `column`, `rectangle_sum` equals the sum of every cell in the rectangle from `(0, 0)` through `(row, column)`: each included column contributes exactly its vertical sum through the current row. Compare this value with `k` and count it when `rectangle_sum <= k`. Thus every possible bottom-right corner is examined once, and the maintained value is exactly the corresponding anchored submatrix sum, so the final count is correct.

## Complexity detail

Let $m$ and $n$ be the numbers of rows and columns. The algorithm performs constant work at each of the $m n$ cells, so its time complexity is $O(m n)$. The column accumulator contains $n$ values, giving $O(n)$ auxiliary space; the input matrix is not modified.

## Alternatives and edge cases

- **Full two-dimensional prefix table:** Computing a prefix value for every cell also gives $O(m n)$ time, but stores $O(m n)$ values even though only the previous vertical contribution per column is needed.
- **Modify `grid` in place:** Replacing cells with anchored prefix sums can achieve $O(1)$ auxiliary space, but destroys the caller's matrix and obscures the separation between input data and accumulated state.
- **Recompute each horizontal prefix:** Summing `column_sums[:column + 1]` for every bottom-right corner is correct but costs $O(m n^2)$ time.
- **Inclusive threshold:** A rectangle whose sum equals `k` must be counted; the title's shortened wording does not change the statement's `<= k` condition.
- **Zero values:** Rectangle sums can stay equal across adjacent corners, so no strict-increase assumption is valid.
- **Top-left value above `k`:** Since all entries are non-negative, no candidate then qualifies, and the ordinary comparisons return zero without a special case.
- **Single row or column:** The same accumulators reduce naturally to ordinary one-dimensional prefix sums.
- **Large totals:** An anchored sum can reach $10^9$, so languages with fixed-width integers must use a type that safely represents that bound.
