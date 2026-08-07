## Description

You are given an `m x n` binary matrix `grid`.

A row or column is considered **palindromic** if its values read the same forward and backward.

You can **flip** any number of cells in `grid` from `0` to `1`, or from `1` to `0`.

Return the **minimum** number of cells that need to be flipped to make **either** all rows **palindromic** or all columns **palindromic**.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">grid = [[1,0,0],[0,0,0],[0,0,1]]</span>

**Output:** <span class="example-io">2</span>

**Explanation:**

![](images/screenshot-from-2024-07-08-00-20-10.png)

Flipping the highlighted cells makes all the rows palindromic.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">grid = </span>[[0,1],[0,1],[0,0]]

**Output:** <span class="example-io">1</span>

**Explanation:**

![](images/screenshot-from-2024-07-08-00-31-23.png)

Flipping the highlighted cell makes all the columns palindromic.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">grid = [[1],[0]]</span>

**Output:** <span class="example-io">0</span>

**Explanation:**

All rows are already palindromic.

</div>

**Constraints:**

	- `m == grid.length`

	- `n == grid[i].length`

	- `1 <= m * n <= 2 * 10^5`

	- `0 <= grid[i][j] <= 1`
