## Description

You are given an `m x n` binary matrix `grid`.

A row or column is considered **palindromic** if its values read the same forward and backward.

You can **flip** any number of cells in `grid` from `0` to `1`, or from `1` to `0`.

Return the **minimum** number of cells that need to be flipped to make **all** rows and columns **palindromic**, and the total number of `1`'s in `grid` **divisible** by `4`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">grid = [[1,0,0],[0,1,0],[0,0,1]]</span>

**Output:** <span class="example-io">3</span>

**Explanation:**

![](images/image.png)

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">grid = [[0,1],[0,1],[0,0]]</span>

**Output:** <span class="example-io">2</span>

**Explanation:**

![](images/screenshot-from-2024-07-09-01-37-48.png)

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">grid = [[1],[1]]</span>

**Output:** <span class="example-io">2</span>

**Explanation:**

![](images/screenshot-from-2024-08-01-23-05-26.png)

</div>

**Constraints:**

	- `m == grid.length`

	- `n == grid[i].length`

	- `1 <= m * n <= 2 * 10^5`

	- `0 <= grid[i][j] <= 1`
