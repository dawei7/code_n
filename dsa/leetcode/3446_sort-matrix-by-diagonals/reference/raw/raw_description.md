## Description

You are given an `n x n` square matrix of integers `grid`. Return the matrix such that:

	- The diagonals in the **bottom-left triangle** (including the middle diagonal) are sorted in **non-increasing order**.

	- The diagonals in the **top-right triangle** are sorted in **non-decreasing order**.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">grid = [[1,7,3],[9,8,2],[4,5,6]]</span>

**Output:** <span class="example-io">[[8,2,3],[9,6,7],[4,5,1]]</span>

**Explanation:**

![](images/4052example1drawio.png)

The diagonals with a black arrow (bottom-left triangle) should be sorted in non-increasing order:

	- `[1, 8, 6]` becomes `[8, 6, 1]`.

	- `[9, 5]` and `[4]` remain unchanged.

The diagonals with a blue arrow (top-right triangle) should be sorted in non-decreasing order:

	- `[7, 2]` becomes `[2, 7]`.

	- `[3]` remains unchanged.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">grid = [[0,1],[1,2]]</span>

**Output:** <span class="example-io">[[2,1],[1,0]]</span>

**Explanation:**

![](images/4052example2adrawio.png)

The diagonals with a black arrow must be non-increasing, so `[0, 2]` is changed to `[2, 0]`. The other diagonals are already in the correct order.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">grid = [[1]]</span>

**Output:** <span class="example-io">[[1]]</span>

**Explanation:**

Diagonals with exactly one element are already in order, so no changes are needed.

</div>

**Constraints:**

	- `grid.length == grid[i].length == n`

	- `1 <= n <= 10`

	- `-10^5 <= grid[i][j] <= 10^5`
