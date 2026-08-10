## General

**Place exactly one queen in each row**

A queen attacks along its row, column, and both diagonal directions. The recursion assigns rows in increasing order, and each call `dfs(i)` chooses the queen's column for row `i`. Because the algorithm makes exactly one choice before recursing to the next row, two queens can never share a row. No row-occupancy structure is needed.

The remaining work is to reject a column if an earlier queen attacks it vertically or diagonally. Once one queen has been placed in every row without those conflicts, the board is a complete solution.

**How diagonal coordinates become array indices**

Cells on a diagonal running from top-right to bottom-left have the same row-plus-column value. Thus `i + j` identifies that diagonal. Its range is 0 through $2n-2$, so `dg[i + j]` can record whether it already contains a queen.

Cells on a diagonal running from top-left to bottom-right have the same column-minus-row value `j - i`. That value may be negative, so the code adds `n` and indexes `udg[n - i + j]`. The possible indices range from 1 through $2n-1$. The arrays have length `2 * n`; every used index is valid, although index 0 of `udg` is unused.

`col[j]` records vertical occupancy. Each entry in all three arrays is either zero or one. The expression

`col[j] + dg[i + j] + udg[n - i + j] == 0`

is true precisely when all three relevant lines are unoccupied. If any one contains a queen, the sum is positive and the candidate is skipped.

**The recursive state invariant**

At entry to `dfs(i)`, rows 0 through `i - 1` contain exactly one queen each, rows `i` through `n - 1` contain only dots, and the three occupancy arrays describe exactly the queens in the filled prefix. Those queens do not attack one another.

The initial call `dfs(0)` satisfies the invariant: the grid is all dots and every occupancy entry is zero. For a safe column `j`, the algorithm writes `"Q"` into `g[i][j]` and marks the corresponding column and two diagonals. These updates happen before recursion so deeper rows see the new queen as an obstacle.

Since the safety test ruled out every attack with an earlier queen, the child state remains non-attacking. The child also moves to `i + 1`, so its filled prefix is one row longer and the invariant is preserved.

**Backtracking must restore both representations**

After the child has generated every solution extending `(i, j)`, the source clears all three occupancy markers and writes `"."` back into the grid cell. The grid and marker arrays are two synchronized representations of the current path, so both need restoration.

If a marker were left set, sibling branches would incorrectly believe a removed queen was still attacking them. If the grid character were left as `"Q"`, a later completed snapshot could contain an obsolete queen even though the marker state was correct. Restoring both makes the next column trial start from exactly the parent state.

**Constructing a stable board at a leaf**

When `i == n`, all rows have one non-attacking queen. The grid currently consists of mutable lists of one-character strings, while the required board is a list of row strings. The comprehension joins each row and creates a new list:

`["".join(row) for row in g]`.

This conversion also freezes the solution. Later backtracking mutates `g`, but strings are immutable and the newly created row list is independent, so an answer already appended to `ans` cannot change.

**A small placement trace**

For $n=4$, suppose row 0 chooses column 1. The algorithm marks column 1, diagonal index 1, and shifted diagonal index 5. In row 1, columns sharing any of those identifiers are rejected. If row 1 chooses column 3, its markers are added and the search continues.

When a later row has no safe column, its loop makes no recursive call. Control returns to the previous row, removes that row's queen, and tries its next safe column. This is how a placement that is locally legal but cannot be completed is abandoned without losing other possibilities.

**Why the search finds every solution once**

Every recorded board is valid. Row-by-row recursion gives one queen per row, `col` gives at most one per column, and the two diagonal arrays give at most one per diagonal. Reaching `i == n` means exactly $n$ queens have been placed.

For completeness, take any valid board. Its queen in row 0 occupies some column that the root loop tries. Once that is selected, its queen in row 1 is safe relative to the prefix and is tried by the next loop. Repeating this reasoning follows a recursion path matching every row of the board.

For uniqueness, two different recursion leaves have a first row where they chose different columns. Their serialized boards differ in that row, so they cannot be the same configuration. Each solution is therefore returned exactly once.

**Source-accurate storage rather than only the manifest claim**

The selected implementation allocates `g` as an $n \times n$ list of characters. That is $O(n^2)$ auxiliary storage even before answers are counted. The column and diagonal arrays and recursion stack are only $O(n)$, but they do not dominate the grid. Therefore, the manifest's $O(n)$ space claim does not match this exact source.

A path storing only the chosen column in each row could construct strings at leaves and use $O(n)$ active-search storage. That is not what this implementation does, so the explanation reports the actual $O(n^2)$ bound.

## Complexity detail

Column uniqueness alone reduces full placement orders to at most $n!$, and diagonal checks prune many of them. Let $S$ be the number of valid solutions and let $V$ be the number of partial states visited. Each state scans up to $n$ columns, so search work is $O(nV)$, with $V=O(n!)$ as a conventional coarse bound.

Every valid leaf converts $n$ rows of length $n$ into strings, costing $\Theta(n^2)$ time. A source-accurate output-sensitive bound is

$$
O(nV + S n^2).
$$

Since $S \le n!$, a conservative broad bound is $O(n^2 n!)$. The manifest's $O(n!)$ is the customary simplified search-tree description, but it omits per-board materialization and candidate-loop factors.

The mutable grid occupies $\Theta(n^2)$ space. Markers and recursion use $O(n)$, so auxiliary space is $O(n^2)$. Returned boards require $\Theta(Sn^2)$ output storage and are separate from the auxiliary figure.

## Alternatives and edge cases

- **Column path plus sets:** Store one column per row and three occupied sets. This reduces the active board representation, but Python sets still need linear state and board strings must be created at each solution.
- **Boolean arrays with no full grid:** Keep the same conflict checks but store only `curr[row] = column`. It achieves $O(n)$ auxiliary search space and constructs the board only at leaves.
- **Bit-mask backtracking:** Represent columns and diagonals as integers, derive all available positions with bit operations, and recurse on set bits. It is compact and fast but less beginner-friendly.
- **Check the grid by scanning:** Testing an entire column and two diagonals for every tentative queen avoids marker arrays but increases each safety check to $O(n)$.
- **`n = 1`:** The only cell is safe, the leaf serializes `["Q"]`, and one solution is returned.
- **Rows with no safe column:** The empty remainder of the loop is the dead-end signal; ordinary return triggers rollback in the parent.
- **Odd and even dimensions:** No special geometric case is needed. Diagonal formulas cover every square uniformly.
- **Negative diagonal differences:** The `n` offset prevents negative indexing from being used as a different Python list position.
- **Input mutation:** The only input is integer `n`; all board state is internal.
- **Answer order:** Depth-first increasing-column order determines presentation, but the contract accepts any order.
