## General

For every matrix cell, we need the sum of a rectangular block centered around that cell and clipped to the matrix boundaries. Neighboring blocks overlap heavily. Adding each block cell by cell would repeat the same work many times.

The Optimal solution builds a two-dimensional prefix-sum table. After this preprocessing, any axis-aligned rectangle sum is obtained from four prefix entries using inclusion-exclusion. The algorithm then computes one clipped rectangle for every output cell.

**Meaning of the padded prefix table**

If the matrix has `m` rows and `n` columns, `s` has `m + 1` rows and `n + 1` columns. Its row zero and column zero remain zero.

`s[i][j]` stores the sum of original matrix rows zero through `i - 1` and columns zero through `j - 1`. In other words, its indices are exclusive boundaries in the original matrix.

The extra border serves as the sum of an empty prefix. Rectangles touching the top or left edge can use the same formula as interior rectangles without negative indices or special branches.

**Building each prefix value**

The loops use `enumerate(mat, 1)` and `enumerate(row, 1)`, so `i` and `j` already refer to padded-table positions. The current original value is `x = mat[i - 1][j - 1]`.

The update is

`s[i][j] = s[i - 1][j] + s[i][j - 1] - s[i - 1][j - 1] + x`.

`s[i - 1][j]` contains the rectangle above the current cell. `s[i][j - 1]` contains the rectangle to its left. Their upper-left overlap appears in both, so `s[i - 1][j - 1]` is subtracted once. Finally, `x` adds the current cell.

By filling rows and columns in increasing order, all three earlier prefix values are ready when a new entry is computed.

**Clipping one requested block**

For output cell `(i, j)`, the unbounded requested rows would run from `i - k` through `i + k`. Valid row indices must stay from zero through `m - 1`. The code clamps them:

`x1 = max(i - k, 0)` and `x2 = min(m - 1, i + k)`.

It does the same for columns:

`y1 = max(j - k, 0)` and `y2 = min(n - 1, j + k)`.

The resulting inclusive rectangle `[x1, x2]` by `[y1, y2]` contains exactly the valid matrix positions satisfying the distance conditions. Near a corner, both lower bounds may become zero. When `k` is large, the upper bounds may reach the last row and column, making the block the whole matrix.

**Converting inclusive coordinates to prefix boundaries**

The desired rectangle uses inclusive endpoints, while `s` uses exclusive lower-right boundaries. Its sum is

`s[x2 + 1][y2 + 1] - s[x1][y2 + 1] - s[x2 + 1][y1] + s[x1][y1]`.

Start with the prefix ending just after `(x2, y2)`. Subtract the rows above `x1` and the columns left of `y1`. Their upper-left overlap was subtracted twice, so add it back once.

Every requested cell remains exactly once. Cells outside the block cancel.

**A corner example**

For the top-left cell of a $3 \times 3$ matrix with `k = 1`, the bounds are rows zero through one and columns zero through one. The block contains four values, not a nonexistent $3 \times 3$ region extending beyond the matrix.

With matrix

`[[1,2,3],[4,5,6],[7,8,9]]`,

that block sums to $1+2+4+5=12$, which becomes `ans[0][0]`.

For the center cell, bounds are zero through two in both dimensions, so the whole matrix sum $45$ is used. With `k = 2`, every cell's clipped block covers the entire $3 \times 3$ matrix, producing $45$ everywhere.

**Why all output values are correct**

The prefix construction stores exact top-left rectangle sums by inclusion-exclusion. Clamping computes exactly the valid portion of each requested block. The four-term rectangle formula then returns exactly that block's sum.

The output loops visit every pair `(i, j)` once and store its independently correct rectangle total in the matching position. Therefore, the complete `ans` matrix satisfies the definition.

## Complexity detail

Building the prefix table visits all $mn$ input cells and performs constant work per cell, taking $O(mn)$ time.

The output also has $mn$ cells. Each uses constant-time bounds calculations and four prefix accesses, adding another $O(mn)$ time. Total time is $O(mn)$.

The prefix table has $(m+1)(n+1)=O(mn)$ entries. The returned answer has $mn$ entries. Counting both gives $O(mn)$ storage, matching the manifest. Excluding required output, auxiliary space remains $O(mn)$ because of `s`.

No loop depends multiplicatively on `k`. Once prefix sums exist, a very large block costs the same constant work as a small block.

## Alternatives and edge cases

- **Directly sum each block:** It is simple but can take $O(mn(2k+1)^2)$ time because overlapping values are repeatedly added.
- **Row prefix sums only:** They reduce each block to one range query per included row, costing $O(mn\min(m,2k+1))$. Two-dimensional prefixes remove the remaining row factor.
- **Sliding windows:** Horizontal and vertical rolling sums can also achieve $O(mn)$ time, but boundary handling and two passes are more intricate.
- **Top or left boundary:** The zero-padded prefix row and column let `x1` or `y1` equal zero without special cases.
- **Bottom or right boundary:** `min` clamps inclusive endpoints before the required `+1` prefix conversion.
- **`k = 0` outside the local lower bound:** Each rectangle would contain only the cell itself, and the same formula would return a copy of `mat`.
- **`k` larger than both dimensions:** Every clipped block is the entire matrix, so all output entries are equal.
- **One-row or one-column matrix:** The two-dimensional formula still works and naturally behaves like a one-dimensional range sum.
- **Positive values:** Positivity is not required for prefix inclusion-exclusion; negative values would also be summed correctly.
- **Integer overflow in other languages:** The block total can exceed one cell's range, so a wider accumulator may be necessary. Python integers expand automatically.
- **Inclusive versus exclusive endpoints:** The `x2 + 1` and `y2 + 1` conversions are essential. Omitting them would exclude the last requested row or column.
