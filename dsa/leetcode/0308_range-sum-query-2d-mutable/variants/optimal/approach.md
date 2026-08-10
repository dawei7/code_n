## General

Updates change one matrix cell, while a query asks for the sum across several rows and columns. The exact source handles the column dimension with a Fenwick tree in each row. It does not build one fully two-dimensional Fenwick tree.

The object stores `self.trees`, where `self.trees[r]` summarizes every value in original matrix row `r`. A point assignment updates only that row's tree. A rectangle query asks each included row tree for its horizontal interval sum, then adds those row results.

This decomposition uses the identity

$$
\sum_{i=row1}^{row2}\sum_{j=col1}^{col2}\texttt{matrix}[i][j]
=
\sum_{i=row1}^{row2}
\left(
\sum_{j=col1}^{col2}\texttt{matrix}[i][j]
\right).
$$

In words, the sum of a rectangle is the sum of its horizontal row segments.

**The one-dimensional Fenwick tree inside each row**

Each `BinaryIndexedTree` uses one-based positions. Original column 0 maps to tree position 1, and original column `j` maps to position `j + 1`.

For a positive tree position $x$, the source computes

$$
\operatorname{lowbit}(x)=x\mathbin{\&}(-x).
$$

This isolates the least significant set bit. Entry `c[x]` stores the sum of the one-based interval

$$
[x-\operatorname{lowbit}(x)+1,\ x].
$$

For example, `c[6]` covers positions 5 and 6 because `lowbit(6) = 2`, while `c[8]` covers positions 1 through 8 because `lowbit(8) = 8`.

These aligned partial sums support two operations:

- add a delta to one column in logarithmic time;
- calculate the sum of a row prefix in logarithmic time.

**Updating a row tree by a delta**

`tree.update(x, delta)` adds `delta` to logical one-based position `x`. It updates `c[x]` and then repeatedly advances with

`x += lowbit(x)`.

Each destination is the next larger stored interval containing the original position. The loop stops after passing the number of columns. Consequently, every partial sum affected by the point change receives the delta, and no unrelated interval changes.

The tree operation is additive. It does not mean “replace this value with `delta`.” The public matrix operation is an assignment, so the source must first translate an assignment into the correct difference.

**Reading one row prefix**

`tree.query(x)` returns the sum of the first `x` values in that row, corresponding to original columns 0 through `x - 1`.

It adds `c[x]` to an accumulator and repeatedly retreats with

`x -= lowbit(x)`.

The current entry supplies the last still-unaccounted block of the prefix. Subtracting its block length moves immediately before it. The visited blocks are disjoint and together cover one-based positions 1 through the original `x`.

For a row interval with inclusive original columns `[col1, col2]`, the source subtracts two prefixes:

$$
\operatorname{rowSum}(col1,col2)
=
\operatorname{query}(col2+1)-\operatorname{query}(col1).
$$

The first prefix includes original column `col2`; the second removes every column before `col1`.

**Constructing all row trees**

The constructor reads the common column count `n` and creates one new Fenwick tree for each matrix row. It then adds every row value `v` at position `j + 1`.

Trees are independent. An entry in the tree for row 3 never contains values from row 2 or row 4. This independence is why cell updates are fast and simple, but it is also why a tall rectangle query must visit each included row.

After construction, the original matrix is not retained. The collection of row Fenwick trees is the authoritative mutable representation.

**Turning a cell assignment into a delta**

To execute `update(row, col, val)`, the source selects `tree = self.trees[row]`.

It recovers the current value at that one cell by subtracting neighboring row prefixes:

`prev = tree.query(col + 1) - tree.query(col)`.

This isolates original column `col`. The assignment is then converted to

$$
\Delta=val-prev,
$$

and `tree.update(col + 1, val - prev)` adds that delta to all affected row blocks. The new logical value becomes

$$
prev+(val-prev)=val.
$$

No other row tree changes because a point update affects only one matrix row.

**Summing an entire rectangle**

`sumRegion` takes the row slice `self.trees[row1 : row2 + 1]`. The `+1` is required because Python's slice end is exclusive while `row2` is inclusive.

For each selected tree, it computes

`tree.query(col2 + 1) - tree.query(col1)`.

That value is the current sum of the query's columns in one row. Python's `sum` combines the row-segment totals into the rectangle total.

Every requested cell belongs to exactly one selected row and appears exactly once in that row's interval. Cells outside the requested row range have no tree in the slice. Cells before `col1` cancel through prefix subtraction, and cells after `col2` never enter the ending prefix. The result therefore contains all and only cells in the inclusive rectangle.

**Tracing the sample update**

The first query over rows 2 through 4 and columns 1 through 3 returns 8 by adding three independent row-segment sums.

The update changes cell `(3, 2)` from 0 to 2. The row-3 tree recovers `prev = 0`, computes `delta = 2`, and adds that delta at one-based column position 3. Every later row-3 range covering original column 2 increases by two; ranges that exclude it are unchanged, and all other row trees are unchanged.

Repeating the same rectangle query therefore returns $8+2=10$.

**Why the maintained structure stays correct**

During construction, each original value is added to all Fenwick intervals in its row that contain its column, establishing correct row partial sums. A public assignment adds exactly the difference between new and old values to those same containing intervals, preserving them.

Each row prefix query decomposes its requested prefix into correct, disjoint Fenwick blocks. Prefix subtraction gives an exact current horizontal interval. Summing these exact intervals over each included row gives an exact current rectangle. Thus, arbitrary interleavings of updates and region queries remain consistent.

## Complexity detail

Let $m$ be the number of rows, $n$ the number of columns, $q$ the number of public operations, and $h=row2-row1+1$ the height of one queried rectangle.

Constructing one row performs $n$ Fenwick updates, each costing $O(\log n)$. Across $m$ rows, exact construction time is $O(mn\log n)$.

A cell assignment performs two prefix queries and one point update in one row tree, so it costs $O(\log n)$.

A rectangle query performs two Fenwick queries for each of $h$ selected rows. It costs $O(h\log n)$ for $n>1$, or more uniformly $O(h(1+\log n))$ including iteration overhead. In the worst case $h=m$, so query time is $O(m(1+\log n))$.

The slice `self.trees[row1 : row2 + 1]` creates a temporary list of $h$ tree references, adding $O(h)$ temporary space during a query. The persistent trees store $m(n+1)$ integers, using $O(mn)$ space.

The manifest's $O((mn+q)\log m\log n)$ bound and “two-dimensional Fenwick tree” summary do not describe this source. There is no Fenwick aggregation over rows; operation cost depends on whether an operation is an update or on the queried height.

## Alternatives and edge cases

- **True two-dimensional Fenwick tree:** Store partial sums across both row and column lowbit ranges. Point updates and prefix rectangles then cost $O(\log m\log n)$, and inclusion-exclusion answers a rectangle with four prefix queries. This matches the manifest, but it is not the exact source.
- **Avoid the row slice:** Iterate row indices or use `itertools.islice` so a query does not allocate $O(h)$ temporary references. Time remains proportional to the number of included rows.
- **Keep a matrix of current values:** Reading `prev` becomes $O(1)$ during assignment, at the cost of another $O(mn)$ structure. The exact source instead isolates the cell with two prefix queries.
- **One segment tree per row:** It gives the same broad tradeoff: logarithmic column updates and row intervals, but linear dependence on query height.
- **Static two-dimensional prefix matrix:** Rectangle queries are $O(1)$ but a point update invalidates many prefixes and may cost $O(mn)$ to repair.
- **Direct matrix storage:** Updates are $O(1)$ while a rectangle query costs its full area $O(hw)$. Row Fenwick trees reduce width dependence to logarithmic.
- **Passing `val` as the Fenwick delta:** This would add the new value to the old one. Assignment requires `val - prev`.
- **Zero-based tree position:** Fenwick position zero cannot advance because `lowbit(0) = 0`. Column indices must be shifted by one.
- **Inclusive `row2`:** Python slicing excludes its ending index, so the exact slice must end at `row2 + 1`.
- **Inclusive `col2`:** The ending prefix must be `query(col2 + 1)` to include the final column.
- **Single-cell rectangle:** One row is selected and neighboring prefixes isolate exactly one current cell.
- **Single-row rectangle:** Only one tree contributes, so the query costs $O(\log n)$ plus constant iteration overhead.
- **All rows with a narrow column interval:** The query still visits every row because no structure aggregates row sums, even when the width is one.
- **One-column matrix:** Each tree operation is constant in practice, but a rectangle query still sums $h$ row results.
- **Negative cell values:** Fenwick trees require only additive inverses, so negative values and negative update deltas are handled exactly.
- **Assigning the existing value:** The delta is zero; all rectangle sums remain unchanged.
- **Rectangular guarantee:** Every row has the same `n`, so each row tree uses a consistent column coordinate system.
