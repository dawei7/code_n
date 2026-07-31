## General

**Separate each cell into a row term and a column term.** If row `i` contains `row_ones[i]` ones, it contains `n - row_ones[i]` zeros. Its net contribution is therefore `2 * row_ones[i] - n`. Likewise, column `j` contributes `2 * column_ones[j] - m`.

Scan the grid to compute every row and column one-count. Then create each answer cell by adding its precomputed row balance and column balance. This is algebraically identical to adding both one-counts and subtracting both zero-counts.

Every count includes exactly the cells prescribed by the contract, so each stored balance is correct. Combining the unique balance for row `i` with the unique balance for column `j` consequently produces the required value for `(i, j)`.

## Complexity detail

Computing the counts and constructing the output each visit all $mn$ cells, for $O(mn)$ time. The row and column arrays require $O(m+n)$ auxiliary space. The required $m \times n$ return matrix is output space and is not included in the auxiliary bound.

## Alternatives and edge cases

- **Recount for every cell:** Summing its complete row and column independently is correct but costs $O(mn(m+n))$ time.
- **Store ones and zeros separately:** This works but duplicates information because each zero-count follows from the corresponding dimension and one-count.
- **Single row or column:** The same formula applies; a cell still receives both its row and column contributions.
- **All zeros:** Every balance is negative, and negative output values are valid.
- **All ones:** Each row contributes `n` and each column contributes `m`, so every answer is `m + n`.
