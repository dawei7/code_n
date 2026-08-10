## General

**Split the two conditions into two collections**

A lucky number must satisfy two independent properties:

1. It is the minimum value of its row.
2. It is the maximum value of its column.

The exact solution computes the values satisfying each property separately and then intersects the two sets.

`rows = {min(row) for row in matrix}` examines every row and stores its minimum value. If the matrix has $m$ rows, this produces at most $m$ values. A matrix entry appears in `rows` exactly when it is a row minimum.

`cols = {max(col) for col in zip(*matrix)}` transposes the way the matrix is iterated. The star operator supplies all matrix rows to `zip`. The first tuple produced contains the first element of every row, which is column zero; the next tuple is column one, and so on. Taking `max` of each tuple therefore finds every column maximum.

The set intersection `rows & cols` contains values that occur in both categories. Converting it with `list(...)` produces the required list, and the arbitrary iteration order of a set is acceptable because the answer may be returned in any order.

**Why comparing values is enough here**

The code does not retain the row and column coordinates of an extremum. That is safe because all matrix elements are globally distinct. A value identifies exactly one cell.

Suppose value $x$ is in both sets. Since it occurs only once in the matrix, the row-minimum occurrence and column-maximum occurrence must be that same cell. Thus $x$ is simultaneously the minimum in its own row and the maximum in its own column, so it is lucky.

The distinctness guarantee is important. With duplicates, a value could be the minimum of one row at one coordinate and the maximum of an unrelated column at another coordinate. A value-only intersection could then report it even if neither occurrence satisfies both conditions. A coordinate-based check would be needed for that generalized input.

**Walking through the first example**

For `[[3, 7, 8], [9, 11, 13], [15, 16, 17]]`, the row minima are 3, 9, and 15, giving `rows = {3, 9, 15}`. The column maxima are 15, 16, and 17, giving `cols = {15, 16, 17}`. Their only common value is 15.

The unique cell holding 15 is the first element of the last row and the last element of the first column. It is smaller than 16 and 17 in its row, while larger than 3 and 9 in its column. The intersection returns `[15]`.

If the two sets have no common value, no cell can satisfy both requirements, and the result is an empty list.

**Why there can be at most one lucky number**

The exact code would support a set containing several common values, but under globally distinct entries the matrix actually has at most one lucky number. A contradiction proves this.

Assume distinct lucky values $x$ at row $r_1$, column $c_1$ and $y$ at row $r_2$, column $c_2$. They cannot share a row or column because each row has one distinct minimum and each column one distinct maximum. Look at the cross cell at $(r_1,c_2)$. Since $x$ is the minimum of row $r_1$, that cross value is greater than $x$. Since $y$ is the maximum of column $c_2$, the cross value is less than $y$. Therefore $x<y$.

The other cross cell at $(r_2,c_1)$ gives the reverse: it is greater than row minimum $y$ but less than column maximum $x$, so $y<x$. Both inequalities cannot hold. Hence two lucky values cannot exist.

The set method remains pleasantly direct: it does not need a special at-most-one proof in its control flow, and it naturally returns either an empty or one-element list.

**Why the algorithm is correct**

Every reported value belongs to `rows` and `cols`. Global distinctness makes its two extremum occurrences the same cell, proving every reported result is lucky. Conversely, any lucky cell's value is added when its row minimum is computed and again when its column maximum is computed, so it belongs to the intersection and cannot be missed. Therefore the returned list contains exactly all lucky numbers.

## Complexity detail

Let $m$ be the number of rows and $n$ the number of columns. Finding all row minima examines $mn$ values. Creating and reducing the column tuples also examines $mn$ values. Set intersection takes $O(m+n)$ expected time in the worst collection-size description, which is dominated by matrix scanning. Total time is $O(mn)$.

The row-minimum set holds at most $m$ values and the column-maximum set at most $n$, so the exact auxiliary storage is $O(m+n)$, plus temporary column tuples produced by `zip`. At any instant one such tuple has $m$ entries, which remains within $O(m+n)$. The manifest states $O(n)$ using a single dimension symbol for the stored extrema; with separate rectangular dimensions, $O(m+n)$ is the precise expression. The output has at most one value under the distinctness guarantee.

## Alternatives and edge cases

- **Coordinate scan with precomputed arrays:** Store each row minimum and column maximum, then test every cell against both indexed values. It is also $O(mn)$ and works even when duplicate values require coordinate awareness.
- **Max of row minima versus min of column maxima:** Under distinct entries, these two scalar values are equal exactly when a lucky number exists. This uses $O(1)$ extra scalar space but needs a less immediate proof.
- **Check every candidate from scratch:** For each cell, rescan its row and column. It is simple but costs $O(mn(m+n))$.
- **One row:** Its row minimum is lucky because every column contains only one value, making that value its column maximum only for the minimum's column.
- **One column:** The column maximum is lucky because every row contains one value and therefore that cell is its row minimum.
- **One cell:** The sole value is both minimum and maximum and is returned.
- **No intersection:** The empty set becomes an empty list, correctly indicating no lucky number.
- **Distinct values:** This guarantee makes value-set intersection equivalent to coordinate-level conjunction.
- **Duplicate values outside the contract:** A value may satisfy the two properties at different coordinates, creating a false positive; retain coordinates or test cells directly.
- **Arbitrary output order:** Set iteration order is not guaranteed, but the contract explicitly permits any order.
- **Rectangular shape:** `zip(*matrix)` works because every row has the same stated length.
- **Input mutation:** `min`, `max`, `zip`, and set construction only read the matrix.
