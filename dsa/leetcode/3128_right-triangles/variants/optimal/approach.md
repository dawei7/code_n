## General

**Choose the right-angle vertex first.** Every valid triangle has one distinguished `1` cell that shares a row with one of the other vertices and a column with the remaining vertex. If `(row, column)` is that cell, let its row contain $R_{\text{row}}$ ones and its column contain $C_{\text{column}}$ ones. There are $R_{\text{row}}-1$ choices for the horizontal arm and $C_{\text{column}}-1$ independent choices for the vertical arm.

**Count each pivot's Cartesian product.** The number of triangles having this right-angle vertex is therefore

$$
(R_{\text{row}}-1)(C_{\text{column}}-1).
$$

Precompute every row and column count, visit each cell containing `1`, and add that product. A chosen horizontal partner and vertical partner always lie in different cells because one changes only the column and the other changes only the row, so each product term creates a valid triangle. Conversely, every valid triangle has exactly one vertex at the intersection of its horizontal and vertical arms and is counted once by that vertex. Summing all contributions is therefore exact and does not double-count any collection of three cells.

## Complexity detail

Let $m$ be the number of rows and $n$ the number of columns. Computing all row and column totals and then accumulating the contributions each inspect $mn$ cells, so the running time is $O(mn)$. The two count arrays use $O(m+n)$ auxiliary space. The returned total may exceed 32-bit range even though each count fits within the input dimensions.

## Alternatives and edge cases

- **Rescan the pivot's row and column:** Count both arms anew for every `1`. This is correct but can take $O(mn(m+n))$ time on a dense grid.
- **Enumerate triples:** Testing every collection of three `1` cells obscures the unique pivot structure and has prohibitive cubic combinatorial growth.
- **Four directional prefix tables:** Left, right, up, and down counts also produce each pivot's contribution in $O(mn)$ time, but require $O(mn)$ space instead of two one-dimensional arrays.
- **Single row or column:** One arm is necessarily missing, so every contribution is zero.
- **Non-adjacent vertices:** Only row and column equality matters; gaps and intervening zeroes do not invalidate a triangle.
- **All-one matrix:** Every cell contributes $(n-1)(m-1)$, giving $mn(m-1)(n-1)$ triangles.
