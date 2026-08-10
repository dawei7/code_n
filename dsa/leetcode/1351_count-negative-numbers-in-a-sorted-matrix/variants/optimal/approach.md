## General

Both rows and columns are sorted in non-increasing order. Values never increase when moving right, and they never increase when moving down. This creates a boundary between nonnegative and negative cells that can be followed in a staircase path instead of inspecting the entire matrix.

The checked-in solution starts at the bottom-left cell, with `i = m - 1` and `j = 0`. From there, one comparison can eliminate either an entire remaining column segment or an entire remaining row segment.

**When the current value is nonnegative**

If `grid[i][j] >= 0`, every cell above it in column `j` is also nonnegative. Column order gives

$$
\texttt{grid}[0][j] \ge \cdots \ge \texttt{grid}[i][j] \ge 0.
$$

Therefore, column `j` contains no uncounted negative cells among rows zero through `i`. The algorithm safely advances right with `j += 1`.

Rows below `i`, if any, have already been completely handled when `i` moved upward earlier. Thus moving right does not skip unfinished cells.

**When the current value is negative**

If `grid[i][j] < 0`, row order guarantees every cell to its right is less than or equal to it and therefore also negative. The suffix from column `j` through `n - 1` contains exactly `n - j` cells, so the method adds `n - j` to `ans`.

That accounts for every unprocessed cell in the current row. The algorithm then moves up with `i -= 1`. It does not move `j` back left because columns before `j` were already proven nonnegative for all rows at or above the relevant positions during earlier right moves.

For the sample’s bottom row, the bottom-left value is already negative, so the entire row contributes four. Moving to the row above at the same column, the algorithm advances right over its nonnegative leading values until it reaches the first negative, then counts that suffix.

**The staircase invariant**

At the start of each iteration, all cells strictly below row `i` have been counted or ruled out, and all cells strictly left of column `j` in rows zero through `i` have been proved nonnegative. The unresolved region is the rectangle from row zero through `i` and column `j` through `n - 1`.

A nonnegative current cell eliminates the leftmost column of that unresolved rectangle. A negative current cell counts the bottom row of the rectangle. Each move preserves the invariant while making the unresolved rectangle smaller.

The loop ends when `i < 0`, meaning every row was accounted for, or `j == n`, meaning every remaining column was proved nonnegative. In either case, no unresolved cell remains. Every negative suffix was counted exactly once, so `ans` is the total number of negative entries.

Zero belongs to the nonnegative branch, which is correct because only values strictly below zero should be counted.

Starting at bottom-left is what makes each comparison decisive in one direction. A nonnegative value certifies the cells above it, while a negative value certifies the cells to its right. Starting in the middle would not offer those complete-row or complete-column conclusions, and starting at top-left would usually reveal only that one largest cell is nonnegative.

## Complexity detail

Let $m$ be the number of rows and $n$ the number of columns.

Every iteration either decreases `i` by one or increases `j` by one. The row pointer can move at most $m$ times and the column pointer at most $n$ times. The total time is therefore $O(m+n)$, even though the matrix contains $mn$ cells.

The method stores dimensions, two pointers, and the answer counter. It allocates no collection and uses no recursion, so auxiliary space is $O(1)$.

The input grid is read only. Counting `n - j` performs constant-time arithmetic rather than scanning the suffix that has been proven negative.

## Alternatives and edge cases

- **Binary search in each row:** Find the first negative entry per row and add the suffix length. This takes $O(m\log n)$ time and $O(1)$ space.
- **Brute-force scan:** Inspect every cell and count negatives in $O(mn)$ time. It is simple but ignores both sorting guarantees.
- **Top-right staircase:** Start at the top-right and move left or down with a symmetric invariant. It also achieves $O(m+n)$ time.
- **Only row-sorted input:** Per-row binary search remains valid, but the shared staircase pointer relies on column order too.
- **All values nonnegative:** The pointer moves right across every column and returns zero.
- **All values negative:** Each row is counted in one step from the leftmost column, producing $mn$.
- **Zeros:** They are not negative and correctly cause a right move.
- **Single row:** The traversal advances to the first negative and counts the remaining suffix.
- **Single column:** It moves right and exits if the bottom value is nonnegative, or moves upward counting one negative at a time.
- **Duplicate values:** Non-increasing order permits equality; the comparisons remain valid for repeated zeros, positives, or negatives.
- **Counting suffix without inspection:** Once the leftmost unresolved value in a row is negative, sorted order proves every cell to the right is negative.
- **Rectangular matrices:** The pointer proof does not assume equal row and column counts; it works independently for any positive `m` and `n`.
