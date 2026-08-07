## Description

You are given two integers `n` and `m` representing the number of rows and columns of a grid, respectively.

You are also given a 2D integer array `sources`, where `sources[i] = [r_i, c_i, color_​​​​​​​i]` indicates that the cell `(r_i, c_i)` is initially colored with `color_i`. All other cells are initially uncolored and represented as 0.

At each time step, every currently colored cell spreads its color to all adjacent **uncolored** cells in the four directions: up, down, left, and right. All spreads happen simultaneously.

If **multiple** colors reach the same uncolored cell at the same time step, the cell takes the color with the **maximum** value.

The process continues until no more cells can be colored.

Return a 2D integer array representing the final state of the grid, where each cell contains its final color.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">n = 3, m = 3, sources = [[0,0,1],[2,2,2]]</span>

**Output:** <span class="example-io">[[1,1,2],[1,2,2],[2,2,2]]</span>

**Explanation:**

The grid at each time step is as follows:

![](images/g50new.png)

​​​​​​​

At time step 2, cells `(0, 2)`, `(1, 1)`, and `(2, 0)` are reached by both colors, so they are assigned color 2 as it has the maximum value among them.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">n = 3, m = 3, sources = [[0,1,3],[1,1,5]]</span>

**Output:** <span class="example-io">[[3,3,3],[5,5,5],[5,5,5]]</span>

**Explanation:**

The grid at each time step is as follows:

![](images/g51new.png)

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">n = 2, m = 2, sources = [[1,1,5]]</span>

**Output:** <span class="example-io">[[5,5],[5,5]]</span>

**Explanation:**

The grid at each time step is as follows:

![](images/g52new.png)

​​​​​​​

Since there is only one source, all cells are assigned the same color.

</div>

**Constraints:**

	- `1 <= n, m <= 10^5`

	- `1 <= n * m <= 10^5`

	- `1 <= sources.length <= n * m`

	- `sources[i] = [r_i, c_i, color_i]`

	- `0 <= r_i <= n - 1`

	- `0 <= c_i <= m - 1`

	- `1 <= color_i <= 10^6​​​​​​​`

	- All `(r_i, c_i​​​​​​​)` in `sources` are distinct.
