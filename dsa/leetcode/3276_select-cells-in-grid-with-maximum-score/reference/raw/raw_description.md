## Description

You are given a 2D matrix `grid` consisting of positive integers.

You have to select *one or more* cells from the matrix such that the following conditions are satisfied:

	- No two selected cells are in the **same** row of the matrix.

	- The values in the set of selected cells are **unique**.

Your score will be the **sum** of the values of the selected cells.

Return the **maximum** score you can achieve.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">grid = [[1,2,3],[4,3,2],[1,1,1]]</span>

**Output:** <span class="example-io">8</span>

**Explanation:**

![](images/grid1drawio.png)

We can select the cells with values 1, 3, and 4 that are colored above.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">grid = [[8,7,6],[8,3,2]]</span>

**Output:** <span class="example-io">15</span>

**Explanation:**

![](images/grid8_8drawio.png)

We can select the cells with values 7 and 8 that are colored above.

</div>

**Constraints:**

	- `1 <= grid.length, grid[i].length <= 10`

	- `1 <= grid[i][j] <= 100`
