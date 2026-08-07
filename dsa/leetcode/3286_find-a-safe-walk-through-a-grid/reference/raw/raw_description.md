## Description

You are given an `m x n` binary matrix `grid` and an integer `health`.

You start on the upper-left corner `(0, 0)` and would like to get to the lower-right corner `(m - 1, n - 1)`.

You can move up, down, left, or right from one cell to another adjacent cell as long as your health *remains* **positive**.

Cells `(i, j)` with `grid[i][j] = 1` are considered **unsafe** and reduce your health by 1.

Return `true` if you can reach the final cell with a health value of 1 or more, and `false` otherwise.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">grid = [[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]], health = 1</span>

**Output:** <span class="example-io">true</span>

**Explanation:**

The final cell can be reached safely by walking along the gray cells below.

![](images/3868_examples_1drawio.png)

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">grid = [[0,1,1,0,0,0],[1,0,1,0,0,0],[0,1,1,1,0,1],[0,0,1,0,1,0]], health = 3</span>

**Output:** <span class="example-io">false</span>

**Explanation:**

A minimum of 4 health points is needed to reach the final cell safely.

![](images/3868_examples_2drawio.png)

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">grid = [[1,1,1],[1,0,1],[1,1,1]], health = 5</span>

**Output:** <span class="example-io">true</span>

**Explanation:**

The final cell can be reached safely by walking along the gray cells below.

![](images/3868_examples_3drawio.png)

Any path that does not go through the cell `(1, 1)` is unsafe since your health will drop to 0 when reaching the final cell.

</div>

**Constraints:**

	- `m == grid.length`

	- `n == grid[i].length`

	- `1 <= m, n <= 50`

	- `<font face="monospace">2 <= m * n</font>`

	- `1 <= health <= m + n`

	- `grid[i][j]` is either 0 or 1.
