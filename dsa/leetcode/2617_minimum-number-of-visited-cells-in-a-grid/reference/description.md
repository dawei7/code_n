## Description

You are given a **0-indexed** `m x n` integer matrix `grid`. Your initial position is at the **top-left** cell `(0, 0)`.

Starting from the cell `(i, j)`, you can move to one of the following cells:

<ul>
	<li>Cells `(i, k)` with `j < k <= grid[i][j] + j` (rightward movement), or</li>
	<li>Cells `(k, j)` with `i < k <= grid[i][j] + i` (downward movement).</li>
</ul>

Return *the minimum number of cells you need to visit to reach the **bottom-right** cell* `(m - 1, n - 1)`. If there is no valid path, return `-1`.
