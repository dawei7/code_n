## Description

You are given a 2D matrix `grid` of size `m x n`. You are also given a **non-negative** integer `k`.

Return the number of **submatrices** of `grid` that satisfy the following conditions:

	- The maximum element in the submatrix **less than or equal to** `k`.

	- Each row in the submatrix is sorted in **non-increasing** order.

A submatrix `(x1, y1, x2, y2)` is a matrix that forms by choosing all cells `grid[x][y]` where `x1 <= x <= x2` and `y1 <= y <= y2`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">grid = [[4,3,2,1],[8,7,6,1]], k = 3</span>

**Output:** <span class="example-io">8</span>

**Explanation:**

**

![](images/mine.png)

**

The 8 submatrices are:

	- `[[1]]`

	- `[[1]]`

	- `[[2,1]]`

	- `[[3,2,1]]`

	- `[[1],[1]]`

	- `[[2]]`

	- `[[3]]`

	- `[[3,2]]`

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">grid = [[1,1,1],[1,1,1],[1,1,1]], k = 1</span>

**Output:** <span class="example-io">36</span>

**Explanation:**

There are 36 submatrices of grid. All submatrices have their maximum element equal to 1.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">grid = [[1]], k = 1</span>

**Output:** <span class="example-io">1</span>

</div>

**Constraints:**

	- `1 <= m == grid.length <= 10^3`

	- `1 <= n == grid[i].length <= 10^3`

	- `1 <= grid[i][j] <= 10^9`

	- `1 <= k <= 10^9`

​​​​​​
