## General
Describe a square by its bottom-right corner. For a one-cell, the largest ending square has side length

`1 + min(above, left, diagonal)`.

All three neighbors are necessary: the top and left states alone can describe two long strips whose shared interior
corner contains a zero. A zero-cell instead has state zero because no all-one square can end there.

Only the previous logical line is needed. Before updating `dp[c]`, it is the state above the current cell;
`dp[c - 1]` has already become the current line's left state. Preserve the overwritten value as `diagonal` for the next
position. A leading zero sentinel removes boundary branches. Track the largest side length and square it at the end
because the requested result is area.

**Choose the compressed dimension**

The recurrence is symmetric under matrix transposition. The candidate traverses the original rows when the column count
is no larger than the row count. For a wider matrix, `zip(*matrix)` exposes its columns as logical lines instead. In both
orientations, the DP line spans the shorter matrix dimension, reducing storage without materializing a transposed matrix.

After each update, `dp[c]` is exactly the largest all-one square ending at that logical cell. Any larger square would
require all three predecessor states to be larger. Conversely, predecessor squares of the minimum side length, together
with the current one-cell, cover the complete claimed square. Transposition preserves square shape, area, and adjacency,
so choosing either traversal orientation preserves the recurrence and the maximum.

## Complexity detail
Every one of the $m \cdot n$ cells is processed once, giving $O(mn)$ time. The DP line, its sentinel, and at most one
logical line produced by `zip` contain $O(\min(m,n))$ values, so auxiliary space is $O(\min(m,n))$.

## Alternatives and edge cases
- **Fixed column compression:** It has the same recurrence and time bound but uses $O(n)$ space even when the matrix is
  much wider than tall.
- **Full DP table:** It is easier to inspect but uses $O(mn)$ space.
- **Square expansion:** Expanding a candidate from every cell repeatedly inspects the same regions and can be cubic or
  worse.
- **Maximal-rectangle stack:** Histogram logic solves a different shape constraint and is unnecessary here.
- **Boundary contents:** An all-zero matrix returns zero, while one isolated `"1"` yields area one.
- **Area versus side:** A full square of side $q$ returns $q^2$, not $q$.
