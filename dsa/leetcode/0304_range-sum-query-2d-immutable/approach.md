## General

The matrix is immutable, and up to many thousands of region queries may follow. Summing every cell inside each requested rectangle would repeat the same additions. The source instead preprocesses a two-dimensional prefix-sum table so that each query needs only four table reads and three arithmetic operations.

The prefix table has one extra zero row at the top and one extra zero column at the left. For prefix coordinates $R$ and $C$, define

$$
\texttt{s}[R][C]
=
\sum_{0\le i<R}\sum_{0\le j<C}\texttt{matrix}[i][j].
$$

Thus, `s[R][C]` contains the rectangle of original cells whose row indices are strictly less than `R` and whose column indices are strictly less than `C`. In half-open notation, it summarizes original rectangle `[0, R) x [0, C)`.

This means:

- `s[0][C] = 0` for every `C`, because there are no original rows before prefix row 0;
- `s[R][0] = 0` for every `R`, because there are no original columns before prefix column 0;
- original cell `(i, j)` lies at the new lower-right boundary `(i + 1, j + 1)`.

The zero border makes formulas at the top and left edges identical to formulas in the interior.

**Building one prefix entry**

Suppose the constructor is processing original value `v = matrix[i][j]`. The desired `s[i + 1][j + 1]` must contain every cell from the origin through `(i, j)` inclusively.

Two already-computed rectangles cover almost all of that area:

- `s[i][j + 1]` covers all included columns in rows above `i`;
- `s[i + 1][j]` covers all included rows in columns left of `j`.

Adding them counts their shared top-left rectangle `s[i][j]` twice. Subtracting that overlap once restores a single copy. Finally, add the current cell `v`, which belongs to neither earlier rectangle:

$$
\texttt{s}[i+1][j+1]
=
\texttt{s}[i][j+1]
+
\texttt{s}[i+1][j]
-
\texttt{s}[i][j]
+
\texttt{matrix}[i][j].
$$

This is inclusion-exclusion during construction: add the region above, add the region to the left, remove their double-counted overlap, and add the new corner cell.

**Why the loop order supplies every dependency**

The constructor processes rows from top to bottom and columns within a row from left to right.

When it computes `s[i + 1][j + 1]`, the entries in prefix row `i` were completed while processing earlier original rows. The entry `s[i + 1][j]` was completed one column earlier in the current row. The diagonal overlap `s[i][j]` is also already available. No future value is needed, so one forward pass fills the whole table.

**Deriving a query by inclusion-exclusion**

A query includes original rows `row1` through `row2` and columns `col1` through `col2`. Because the prefix table uses exclusive ending boundaries, the origin-based rectangle through the query's lower-right cell is

`s[row2 + 1][col2 + 1]`.

This rectangle includes the desired region, but it also includes cells above it and to its left.

First subtract the left strip:

`s[row2 + 1][col1]`.

It contains rows before `row2 + 1` but only columns before `col1`.

Then subtract the upper strip:

`s[row1][col2 + 1]`.

It contains rows before `row1` across all columns through `col2`.

The top-left rectangle `s[row1][col1]` belongs to both removed strips. It was present once in the original large prefix, then subtracted twice, leaving it counted negative once. Add it back once to make its net contribution zero.

The final query formula is

$$
\begin{aligned}
\operatorname{sumRegion}
={}&\texttt{s}[row2+1][col2+1]\\
&-\texttt{s}[row2+1][col1]\\
&-\texttt{s}[row1][col2+1]\\
&+\texttt{s}[row1][col1].
\end{aligned}
$$

Every cell inside the requested rectangle remains once. Cells only above or only left are removed once. Cells in the top-left overlap are added, removed twice, and restored once, for a net count of zero.

**Tracing a sample query**

For the example matrix, consider `sumRegion(1, 1, 2, 2)`. The desired cells are

`[[6, 3], [2, 0]]`,

whose sum is 11.

Using prefix values:

- `s[3][3] = 21` covers original rows 0 through 2 and columns 0 through 2;
- `s[3][1] = 9` is the left strip in original column 0;
- `s[1][3] = 4` is the upper strip in original row 0;
- `s[1][1] = 3` is their top-left overlap.

The formula gives

$$
21-9-4+3=11.
$$

The overlap value 3 must be restored because it was part of both 9 and 4.

**Why inclusive query coordinates use plus one**

The query's lower bounds, `row1` and `col1`, already describe how many rows or columns lie before the rectangle. They are valid prefix boundaries directly.

The upper bounds, `row2` and `col2`, are inclusive original indices. To include those cells in a half-open prefix, the ending boundaries must be `row2 + 1` and `col2 + 1`. Omitting either plus one would exclude the rectangle's final row or column.

For a single-cell query `(i, j, i, j)`, inclusion-exclusion reduces to that cell because the four surrounding prefix corners cancel everything else. For a query starting at row or column zero, the zero border supplies the required empty-strip totals without conditional branches.

**Why preprocessing stays correct**

The matrix never changes after `NumMatrix` is constructed. Each prefix entry therefore remains an exact summary of the same data for every later query. If updates were allowed, many prefix entries would become stale; the immutable contract is what supports constant-time queries after one preprocessing pass.

## Complexity detail

Let $m$ be the number of rows, $n$ the number of columns, and $q$ the number of calls to `sumRegion`.

The constructor visits each of the $mn$ matrix cells once and performs constant arithmetic for each. Preprocessing time is $O(mn)$.

Each query reads exactly four prefix entries and combines them with two subtractions and one addition. Its time is $O(1)$ regardless of the rectangle's height or width. Across all queries, query work is $O(q)$, so the complete construction-and-query time is $O(mn+q)$.

The prefix table has $(m+1)(n+1)$ integer entries. This is $O(mn)$ space. Individual queries allocate no structure proportional to the matrix or requested region and use $O(1)$ temporary space.

Python integers handle negative totals and grow beyond fixed-width overflow limits as needed. With the problem's bounded dimensions and cell values, arithmetic remains straightforward.

## Alternatives and edge cases

- **Sum every query cell:** It uses no prefix storage but costs $O(hw)$ for a queried rectangle of height $h$ and width $w$, reaching $O(mn)$ per query.
- **One prefix array per row:** Precompute horizontal sums, then subtract two prefixes for each row in the query. Construction is $O(mn)$ and space is $O(mn)$, but each query still costs $O(row2-row1+1)$.
- **Precompute every rectangle:** Constant-time lookup is possible, but the number of possible row and column boundary pairs leads to $O(m^2n^2)$ time and space.
- **Two-dimensional Fenwick tree:** It supports updates and region queries in logarithmic time. With no updates, the static prefix matrix gives simpler and faster $O(1)$ queries.
- **Two-dimensional segment tree:** It also supports mutable data but is far more complex and cannot improve on constant-time immutable queries.
- **Forgetting the overlap restoration:** Subtracting the upper and left strips removes their shared top-left rectangle twice. Failing to add it back makes the answer too small or otherwise numerically wrong when values are negative.
- **Using `row2` or `col2` without plus one:** The prefix convention is half-open, so this excludes the last requested row or column.
- **Adding one to the lower boundaries:** `row1` and `col1` already count the rows and columns before the query. Incrementing them would fail to subtract part of the unwanted prefix.
- **Single cell:** The four-corner formula isolates exactly that value, including when it is negative or zero.
- **Full matrix:** With upper-left `(0, 0)`, all subtractive border terms are zero, and the result is `s[m][n]`.
- **First row only:** `row1 = 0` makes both upper-prefix terms refer to zero row 0, so no special case is needed.
- **First column only:** `col1 = 0` similarly uses the zero column.
- **One-row matrix:** The method becomes the one-dimensional leading-zero prefix pattern while retaining the same formula.
- **One-column matrix:** It likewise reduces to vertical prefix subtraction.
- **Negative values:** Prefix totals are not required to be monotone. Inclusion-exclusion relies on exact addition and subtraction, not ordering.
- **Immutable-data requirement:** Changing one matrix entry after construction would invalidate every prefix covering that cell. This class deliberately exposes no update operation.
- **Valid query bounds:** The source omits defensive checks because the contract guarantees ordered, in-range inclusive corners.
