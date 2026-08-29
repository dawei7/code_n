## General

**Reduce each diagonal to local neighbor comparisons**

A top-left-to-bottom-right diagonal has constant row-minus-column difference. Every cell except those in the first row or first column has one immediate predecessor on its diagonal at `(i - 1, j - 1)`.

The matrix is Toeplitz exactly when every such cell equals that predecessor.

**Why adjacent equality is sufficient**

Suppose a diagonal contains values `a0, a1, a2, ...`. If every adjacent pair is equal, then `a1 = a0`, `a2 = a1 = a0`, and induction shows every value equals the first.

Conversely, if the whole diagonal is constant, every adjacent comparison obviously passes.

Therefore the solution never needs to collect or separately traverse entire diagonals. Checking all local diagonal edges is equivalent.

**Skip the first row and first column**

Cells there have no upper-left predecessor inside the matrix. They start their diagonals and impose no comparison of their own.

The loops begin at row one and column one. Every other cell is checked once:

`matrix[i][j] != matrix[i - 1][j - 1]`.

If any mismatch appears, that diagonal contains two different values, so the method returns `False` immediately.

If all comparisons pass, every diagonal is constant and the method returns `True`.

**Trace the valid example**

For

`[[1,2,3,4],[5,1,2,3],[9,5,1,2]]`,

cell `(1,1)` equals `(0,0)`, cell `(2,2)` equals `(1,1)`, and so the main diagonal is all ones. Equivalent comparisons confirm the two-diagonals and three-diagonals containing values two, three, and five.

Single-cell diagonals at the outer corners require no comparison and are automatically valid.

**Trace an invalid example**

In `[[1,2],[2,2]]`, cell `(1,1)` is two while its upper-left predecessor is one. The first comparison fails, proving the main diagonal is not constant.

**Why row and column dimensions are both needed**

The matrix may be rectangular. `m` controls valid row indices and `n` controls columns. The nested loops cover the entire interior rectangle `1..m-1` by `1..n-1`, which contains exactly the cells with predecessors.

**Every diagonal has one unchecked starting cell**

A diagonal begins either in the first row or in the first column. That starting cell establishes the value that all later cells on the diagonal must match. Every later cell appears in the nested loops and is linked to that start by a chain of upper-left comparisons.

No diagonal is omitted: a length-one diagonal consists only of its start and is automatically constant, while every longer diagonal contributes all but its first cell to the checks.

**Streaming interpretation**

The local comparison also explains the first follow-up. If only one row can be loaded at once, retain the previous row while reading the current row. Compare current column `j` with previous column `j - 1`.

For partial-row streaming, retain the necessary shifted overlap between chunks so each current cell can access its upper-left predecessor. The full in-memory implementation is the same dependency expressed directly.

If rows arrive sequentially, the current row can replace the older row after all its comparisons finish. Memory then depends on one row rather than the full matrix. With partial rows, chunk boundaries must overlap enough to retain the predecessor at column `j - 1`; otherwise a mismatch spanning two chunks could be missed.

**Why comparing values directly is sufficient**

The property depends only on equality, not numeric order or arithmetic differences. Values may repeat on unrelated diagonals without causing a problem, and two diagonals do not need distinct values. The method compares only cells that belong to the same diagonal.

**The loop invariant**

Before processing a cell, every previously visited interior cell equals its upper-left predecessor. A mismatch proves failure. A match extends the invariant to the current cell.

After the loops, all diagonal adjacency relations hold. Transitivity of equality then makes every complete diagonal constant.


If the method returns false, it found two neighboring cells on one diagonal with different values, so the matrix cannot be Toeplitz.

If it returns true, every nonstarting diagonal cell equals the preceding cell. Chaining these equalities from each diagonal’s start proves all values on every diagonal are identical. Both return cases exactly match the definition.

## Complexity detail

Let `m` and `n` be the matrix dimensions. The method checks `(m - 1)(n - 1)` cells in the worst case, so time complexity is `O(mn)`.

It stores only dimensions and loop indices. Auxiliary space is `O(1)`. The input matrix is read without modification.

Early return can reduce work when a mismatch occurs near the beginning, but the worst case remains linear in the number of cells.

## Alternatives and edge cases

- **Group by `i - j`:** Store the first value for every diagonal key and compare later cells. This works but uses `O(m + n)` extra space.

- **Traverse each diagonal separately:** It has the same time bound but requires more boundary-start loops and bookkeeping.

- **Compare with upper-right:** That checks the opposite diagonal direction and solves a different property.

- **One row or one column:** Every diagonal has length one, the loops perform no comparisons, and the answer is true.

- **Rectangular matrices:** The same upper-left rule applies without requiring equal dimensions.

- **Early mismatch:** One unequal adjacent pair is sufficient proof of failure.

- **Disk streaming:** Keep the preceding row rather than the complete matrix.

- **Partial-row streaming:** Preserve boundary values needed for shifted predecessor comparisons between chunks.
