## General

Let $m$ and $n$ be the row and column counts.

**Order the three rooks by row**

Every legal placement has a unique upper, middle, and lower rook. Fix the middle rook at row $r$ and column $c$. The upper rook may use any row before $r$, and the lower rook any row after $r$; their row constraints are then automatically satisfied. What remains is to choose two side cells whose columns differ from $c$ and from each other.

**Summarize a row region by three columns**

For every prefix of rows, maintain the maximum cell value available in each column and retain the three largest values from distinct columns. Build the analogous summaries for suffixes by scanning upward.

Only three distinct columns are necessary. When choosing an upper cell after the middle and lower columns are known, at most two columns are forbidden. Among the region's three best distinct columns, at least one remains available. Any column outside those three cannot beat that surviving candidate. The same argument applies to the lower region.

For each possible middle row and every cell in that row, combine the at most three candidates from the preceding prefix with the at most three candidates from the following suffix. Reject equal columns and maximize the resulting sum.

Any combination considered by the algorithm uses one row from each disjoint region and three distinct columns, so it is legal. Conversely, take an optimal placement and fix its middle rook. If either side rook is not in its region's top-three summary, the two columns used by the other rooks exclude at most two summarized columns; replacing that side rook with an available summarized candidate cannot lower the sum. Thus an equally good placement appears among the enumerated combinations.

## Complexity detail

Updating all column maxima and selecting three best distinct columns for every prefix and suffix costs $O(mn)$ time. Each of the $mn$ possible middle cells examines at most nine side-candidate pairs, which is also $O(mn)$. Prefix and suffix summaries store three pairs per row, while the running column maxima use $O(n)$ space, for $O(m+n)$ auxiliary space.

## Alternatives and edge cases

- **Enumerate three rows:** Keeping each row's top three cells and checking all row triples is correct but takes $O(m^3)$ time.
- **Enumerate all three cells:** Direct cell triples can require $O(m^3n^3)$ work.
- **Keep only one best cell per region:** Its column may conflict with the middle rook, hiding the best legal placement.
- **Keep two columns:** Both can be excluded by the other two rooks; three distinct columns are the necessary safe summary.
- Negative values cannot be skipped because exactly three rooks are required.
- The optimum may be below zero on an all-negative board.
- Several maximum cells in one row or column cannot all be selected.
- Rectangular boards require no transposition; prefix and suffix regions enforce rows directly.
- The sum can reach $\pm3 \times 10^9$, beyond a signed 32-bit integer.
