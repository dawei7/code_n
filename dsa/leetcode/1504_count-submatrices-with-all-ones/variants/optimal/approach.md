## General

**Assigning every rectangle a unique bottom-right corner**

An all-ones submatrix is a rectangle. It has one bottom row and one rightmost column, so it can be counted exactly once by its bottom-right cell. The stored solution iterates over every cell and asks how many valid rectangles end there.

To answer that question, it first builds `g`. The value `g[i][j]` is the number of consecutive ones in row `i` ending at column `j` and extending left.

If `mat[i][j]` is zero, the prefilled `g[i][j]` remains zero because no all-ones horizontal segment can end there. If it is one at column zero, the width is one. Otherwise, the width is one plus `g[i][j - 1]`, extending the run ending at the previous column.

For example, a row ending with `1, 1, 1` has successive widths one, two, and three. A zero resets the next possible run.

**Counting rectangles for one bottom-right cell**

Fix cell `(i, j)` as the bottom-right corner. A rectangle can choose any top row `k` from `i` upward. For every row between `k` and `i`, the rectangle must fit inside that row's consecutive-one width ending at column `j`.

Therefore, the maximum valid width for top row `k` is

$$
\min_{r=k}^{i} g[r][j].
$$

If that minimum is `w`, there are exactly `w` valid rectangles with top row `k` and right boundary `j`: their widths can be one through `w`. Each width chooses a different left boundary.

The source computes this minimum incrementally. It starts `col = inf` and scans `k` from `i` down to zero. At each row, `col = min(col, g[k][j])`. It then adds `col` to `ans`.

Starting with infinity makes the first minimum equal to `g[i][j]`. As more rows are included, `col` can only stay the same or decrease, which exactly reflects the constraint that a taller rectangle must fit through every included row.

**A concrete small trace**

Suppose the widths ending at one column, read from top to bottom, are two, three, and one. For the bottom cell, the top-row choices produce:

- Bottom row alone: minimum width one, contributing one rectangle.
- Bottom two rows: minimum of three and one is one, contributing one.
- All three rows: minimum of two, three, and one is one, contributing one.

At a different bottom row where the upward widths are three and two, contributions are three for height one and two for height two. These counts represent every possible width, not merely the widest rectangle.

**Why zeros are handled without a special break**

If any included row has `g[k][j] = 0`, `col` becomes zero. Every taller choice that includes still more rows also has minimum zero, so all later additions contribute zero.

The exact source continues scanning to the top rather than breaking at zero. This preserves correctness but performs unnecessary iterations. An early break would improve constants without changing the worst-case bound on an all-ones matrix.

**Why nothing is missed or counted twice**

Take any all-ones rectangle. Its bottom-right corner appears in the outer two loops, and its top row appears in that cell's upward loop. Its width is at most every included row's stored left-run width, so it is one of the `col` widths counted for that top row.

Conversely, every width counted by `col` is no larger than the one-run width of any row from top through bottom. Thus every cell inside the corresponding rectangle is one.

The tuple of bottom row, right column, top row, and width uniquely identifies a rectangle. No other iteration uses the same bottom-right and top-left boundaries, proving there is neither omission nor duplication.

**The exact algorithm differs from the manifest method**

The reference editorial also describes an $O(mn)$ monotonic-stack method. The stored source does not use that stack. It stores the full width matrix and performs an upward scan for every cell. Its explanation and complexity must therefore follow the enumeration algorithm actually present.

## Complexity detail

Let $m$ be the number of rows and $n$ the number of columns. Building `g` takes $O(mn)$ time and $O(mn)$ storage.

For row `i`, each of $n$ cells scans `i+1` rows upward. Summing across bottom rows gives

$$
n\sum_{i=0}^{m-1}(i+1)
=
O(m^2n).
$$

The exact worst-case time is therefore $O(m^2n)$, not the manifest's $O(mn)$. There is no data-dependent early break in the stored loop, so even zero-heavy matrices still execute all upward iterations.

The full `g` matrix uses $O(mn)$ space, not the manifest's $O(n)$. Scalars use constant additional space. The manifest bounds describe the monotonic-histogram-stack alternative rather than this source.

## Alternatives and edge cases

- **Monotonic stack per row:** Build upward histogram heights and count rectangles ending at each column with an increasing stack. It achieves the manifest's $O(mn)$ time and $O(n)$ space.
- **Early break at zero width:** Stop the upward scan when `col` becomes zero. It improves zero-heavy inputs but retains $O(m^2n)$ worst-case time on all ones.
- **Brute-force four boundaries:** Enumerating every rectangle and checking all its cells is much slower because it repeats cell validation.
- **Single cell:** A one contributes one submatrix, while a zero contributes none.
- **All zeros:** Every width is zero and the answer is zero, though the exact source still runs every upward loop.
- **All ones:** Every axis-aligned submatrix is valid; this also triggers the enumeration's worst-case meaningful work.
- **One row:** Each run of ones contributes all contiguous subarrays within that run.
- **One column:** The method counts all vertical runs through the incremental minimum.
- **Infinity initialization:** `inf` must be available in the module environment; the first minimum converts it to a finite width.
- **No input mutation:** `mat` is read only, while widths are written to a separate matrix.
