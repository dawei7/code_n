## General

**Simulate one row of movement at a time**

A ball entering cell `(i, j)` sees either `1` or `-1`. A `1` board directs it toward column `j + 1`; a `-1` board directs it toward `j - 1`. If the move is valid, the ball then enters the next row at that adjacent column.

The nested `dfs(i, j)` function returns the eventual exit column for a ball currently entering row `i` at column `j`, or `-1` if it becomes stuck. Although the name says DFS, there is no branching search: every cell determines at most one next state. Recursion is used to express a deterministic path.

**Recognize successful exit before reading another row**

The first condition is `if i == m: return j`. Reaching row index `m` means the ball has passed all rows because valid grid rows are zero through `m - 1`. Its current column `j` is exactly the bottom exit column.

This base case comes before all grid accesses, preventing an attempt to read `grid[m]` after a successful fall.

**Stop boards that point into a wall**

At the left boundary, a `-1` board would send the ball to column minus one. The source detects `j == 0 and grid[i][j] == -1` and returns `-1`.

At the right boundary, a `1` board would send the ball to column `n`. The condition `j == n - 1 and grid[i][j] == 1` returns `-1`.

These checks occur before inspecting either adjacent cell. That order is important in Python: it guarantees the later `j + 1` or `j - 1` access is within bounds whenever evaluated.

**Detect the two V-shaped traps**

Being directed toward an interior neighbor is not sufficient. The two boards that form the channel must slope in the same direction.

If the current value is `1` but `grid[i][j + 1] == -1`, the boards lean toward each other and form a V between columns `j` and `j + 1`. The ball cannot pass to the next row.

Symmetrically, if the current value is `-1` but `grid[i][j - 1] == 1`, a V forms between `j - 1` and `j`.

Because every cell is either one or negative one, these conditions exactly express an adjacent mismatch in the movement direction. Matching adjacent boards make a continuous diagonal channel.

**Recurse to the only legal next state**

After all stuck cases have been ruled out, the source chooses

`dfs(i + 1, j + 1)` when the current board is one, or

`dfs(i + 1, j - 1)` when it is negative one.

The row always increases by one, so recursion must terminate after at most $m$ calls. The column changes by the board's direction, and the preceding checks prove that new column is legal and the channel is not blocked.

**Run the same simulation for every starting column**

There is one ball above each of the $n$ columns. The list comprehension

`[dfs(0, j) for j in range(n)]`

starts each ball at row zero and its own column. Results are generated in the same left-to-right order as the required answer. A stuck path contributes `-1`; a completed path contributes its exit column.

The source does not memoize states. Two balls can eventually enter the same cell, after which their remaining path is identical, but each recursive call chain is evaluated independently. This keeps the implementation simple and still fits the $m,n\le100$ limits.

**Why each returned result is correct**

Consider `dfs(i,j)`. If `i=m`, the returned column is correct by the definition of leaving the bottom. Otherwise, the four stuck conditions cover precisely the two wall directions and the two possible interior V shapes.

If none applies, the boards provide one valid diagonal transition into row `i+1`. By assuming the recursive result correctly describes the remainder from that next state, the current call returns the correct final outcome. Backward induction from row $m$ proves the result for every cell, including every `dfs(0,j)`.

For the single-cell grid `[[-1]]`, the ball starts at `j=0`. The left-wall check immediately returns `-1`. For a row of matching `1` boards away from the right wall, the ball moves one column right and one row down exactly as the diagram rules require.

**Why checking only the current row is enough**

A board affects the ball only while it crosses that row. Once a valid channel moves it into the next row, earlier boards cannot affect it again. The recursive state therefore needs only the next row and current column, not the entire path history.

## Complexity detail

Let $m$ be the number of rows and $n$ the number of columns. Each of the $n$ balls visits at most one cell per row, so there are at most $mn$ recursive calls. Each call does constant work, giving $O(mn)$ time.

One DFS call chain has depth at most $m$, so recursion uses $O(m)$ auxiliary stack space. The output list uses $O(n)$ space. Because balls are processed sequentially, their stacks do not coexist; peak total space including output is $O(m+n)$.

The manifest states $O(n)$ space, which accounts for the answer but omits the exact Python implementation's recursive $O(m)$ stack. If output is excluded, auxiliary space is $O(m)$, not $O(n)$. The constraint $m\le100$ keeps recursion safely below Python's usual recursion limit, but it does not change the two-parameter asymptotic distinction.

## Alternatives and edge cases

- **Iterative simulation:** Loop through rows for each starting column. It keeps the same $O(mn)$ time while reducing per-ball auxiliary space to $O(1)$.
- **Bottom-up dynamic programming:** Store the eventual result for every cell, reusing the next row. It can avoid repeated suffix paths but uses $O(mn)$ storage unless rows are compressed.
- **Memoized recursion:** Cache `dfs(i,j)` so merged paths are solved once. It uses up to $O(mn)$ cache space and does not improve the worst-case cell count below $O(mn)$.
- **Single column:** Every `1` points into the right wall and every `-1` into the left wall, so every ball is stuck.
- **Left-wall trap:** A negative-one board in column zero returns `-1` before accessing column minus one.
- **Right-wall trap:** A one board in column `n-1` returns `-1` before accessing column `n`.
- **V shape `1,-1`:** A ball entering either side becomes stuck between the opposing boards.
- **Matching pair:** Adjacent `1,1` permits rightward passage, while `-1,-1` permits leftward passage.
- **Stuck early:** Recursion returns immediately and does not inspect lower rows for that ball.
- **Exit after last row:** The returned column is the column after completing all row transitions, not the last cell's original column.
- **Input preservation:** The grid is read-only; no board values are changed.
- **Independent balls:** Balls do not interact, so simulating one does not alter another's path.
