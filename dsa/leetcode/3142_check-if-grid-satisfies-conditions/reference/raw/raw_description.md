## Description

You are given a 2D matrix `grid` of size `m x n`. You need to check if each cell `grid[i][j]` is:

	- Equal to the cell below it, i.e. `grid[i][j] == grid[i + 1][j]` (if it exists).

	- Different from the cell to its right, i.e. `grid[i][j] != grid[i][j + 1]` (if it exists).

Return `true` if **all** the cells satisfy these conditions, otherwise, return `false`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">grid = [[1,0,2],[1,0,2]]</span>

**Output:** <span class="example-io">true</span>

**Explanation:**

**

![](images/examplechanged.png)

**

All the cells in the grid satisfy the conditions.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">grid = [[1,1,1],[0,0,0]]</span>

**Output:** <span class="example-io">false</span>

**Explanation:**

**

![](images/example21.png)

**

All cells in the first row are equal.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">grid = [[1],[2],[3]]</span>

**Output:** <span class="example-io">false</span>

**Explanation:**

![](images/changed.png)

Cells in the first column have different values.

</div>

**Constraints:**

	- `1 <= n, m <= 10`

	- `0 <= grid[i][j] <= 9`
